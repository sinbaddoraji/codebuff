from antlr4 import *
from JavaLexer import JavaLexer
from JavaParser import JavaParser
from CollectTokenFeatures import CollectTokenFeatures
from ProcessTokens import ProcessTokens
from sklearn.feature_extraction import DictVectorizer
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path

INVALID_RULE_INDEX = 9999
PREDICTOR_VAR = "inject newline"
# FEATURE_NAMES = ["token type", "column", "length", "enclosing rule",
#                  "earliest ancestor rule", "earliest ancestor length",
#                  "prev token type", "prev token column",
#                  "prev token last char column"]
FEATURE_NAMES = ["prev token type", "prev token column", "enclosing rule"]

def node_features(tokens, node):
    curToken = node.symbol
    prevToken = None
    if curToken.tokenIndex>=1:
        prevToken = tokens[curToken.tokenIndex-1]
    ruleIndex = node.getParent().getRuleIndex()
    ruleName = JavaParser.ruleNames[ruleIndex]
    earliestAncestor = earliestAncestorStartingAtToken(node.getParent(),
                                                            curToken)
    earliestAncestorName = 'none'
    earliestAncestorWidth = 0
    if earliestAncestor is not None:
        earliestAncestorRuleIndex = earliestAncestor.getRuleIndex()
        earliestAncestorName = JavaParser.ruleNames[earliestAncestorRuleIndex]
        earliestAncestorWidth = earliestAncestor.stop.stop - earliestAncestor.start.start + 1
    if prevToken is not None:
        vars = [JavaLexer.symbolicNames[prevToken.type], prevToken.column, ruleName]
    else:
        vars = ['None', 0, ruleName] # first token of file

    # vars = [JavaLexer.symbolicNames[curToken.type], curToken.column,
    #         len(curToken.text),
    #         ruleName, earliestAncestorName, earliestAncestorWidth]
    # if prevToken is not None:
    #     endofprevtoken = prevToken.column + len(prevToken.text) - 1
    #     vars += [JavaLexer.symbolicNames[prevToken.type], prevToken.column,
    #              endofprevtoken]
    # else:
    #     vars += ['None', -1, 0]
    return vars


def extract_data(code):
    """
    Parse a code string and collect features with a CollectTokenFeatures.
    Returns (tokens:list, inject_newlines:boolean[], features:list<object[]>)
    """
    input = InputStream(code)
    lexer = JavaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = JavaParser(stream)
    tree = parser.compilationUnit()
    collector = CollectTokenFeatures(stream)
    walker = ParseTreeWalker()
    walker.walk(collector, tree)
    return (stream.tokens, collector.inject_newlines, collector.features)


def earliestAncestorStartingAtToken(node, token):
    """
    Walk upwards from node while p.start == token
    """
    p = node
    prev = None
    while p is not None and p.start == token:
        prev = p
        p = p.parentCtx

    return prev


def analyze_corpus(dir):
    """
    Return inject_newlines:boolean[], features:list<object[]> collected
    from all corpus files found recursively under dir.
    """
    inject_newlines = []
    features = []
    for fname in files(dir):
        print fname
        with open(fname, 'r') as f:
            code = f.read()
            tokens, nl, predictors = extract_data(code)
            inject_newlines += nl
            features += predictors
    return (inject_newlines, features)


def convert_categorical_data(features):
    """
    From a list of feature vectors, convert category data to use
    multiple binary dummy variables using a DictVectorizer.
    Return the DictVectorizer and new list of feature vectors.
    The DictVectorizer must be used to tranform future testing
    feature vectors for prediction purposes.
    """
    asdict = todict(features)
    vec = DictVectorizer(sort=False)
    features_with_dummy_vars = vec.fit_transform(asdict).toarray()
    print "number new vars", len(vec.get_feature_names())
    #print vec.get_feature_names()
    return vec, features_with_dummy_vars


def todict(features):
    """
    From features:list<object[]>, convert to a list<dict> using
    FEATURE_NAMES as the keys.
    """
    records = []
    n = len(FEATURE_NAMES)
    for record in features:
        d = dict((FEATURE_NAMES[i], record[i]) for i in range(0, n))
        records += [d]
    return records


def format_code(forest, vec, code):
    """
    Tokenize code and then, one token at a time, predict newline or not.
    Do prediction of newline on the fly, adjusting token line/column.
    """

    # tokenize and wack location info in tokens
    input = InputStream(code)
    lexer = JavaLexer(input)
    stream = CommonTokenStream(lexer)
    stream.fill()
    # wipe out token location information in sample
    for t in stream.tokens:
        t.line = 0
        t.column = 0

    # parse to get parse tree
    parser = JavaParser(stream)
    tree = parser.compilationUnit()

    # compute feature vector for each token and adjust line/column as we walk tree
    collector = ProcessTokens(forest, vec, stream)
    walker = ParseTreeWalker()
    walker.walk(collector, tree)


def files(dir):
    """
    Return a list of filenames under dir (with dir as prefix of names)
    """
    list = []
    if os.path.isfile(dir): # oops, it's a file
        return [dir]
    for dirpath, dirs, files in os.walk(dir):
        for f in files:
            qf = dirpath + "/" + f
            list.append(qf)
    return list


def graph_importance(forest, feature_names):
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
    indices = np.argsort(importances)[::-1]

    fig, ax = plt.subplots(1,1)
    plt.title("Feature importances")
    xlabels = [feature_names[int(i)] for i in indices]
    dims = len(importances)
    plt.bar(range(dims), importances[indices],
            color="r", yerr=std[indices], align="center")
    plt.xticks(range(dims), xlabels, rotation=15)
    plt.xlim([-1, dims])
    plt.ylim([0, 1])

    for tick in ax.xaxis.get_major_ticks():
        tick.tick1line.set_markersize(0)
        tick.tick2line.set_markersize(0)
        tick.label1.set_horizontalalignment('right')

    plt.show()


def print_importances(forest, feature_names):
    importances = forest.feature_importances_
    indices = np.argsort(importances)[::-1]
    dims = len(feature_names)
    for f in range(0,dims if dims<10 else 10):
        print("%d. feature %30s (%f)" %
              (f + 1, feature_names[indices[f]], importances[indices[f]]))
