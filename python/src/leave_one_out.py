#
# AUTO-GENERATED FILE. DO NOT EDIT
# CodeBuff 1.4.19 'Fri Jun 17 13:08:15 PDT 2016'
#
import matplotlib.pyplot as plt
import pylab

sqlite_noisy_err = [0.13043478, 0.05154639, 0.15294118, 0.19277108, 0.21489972, 0.22946176, 0.15879828, 0.3082353, 0.19762845, 0.18139535, 0.2877698, 0.37349397, 0.17948718, 0.22535211, 0.14634146, 0.08958485, 0.2345679, 0.1450285, 0.16030534, 0.13525836, 0.0790378, 0.34254143, 0.2638037, 0.17747441, 0.12962963, 0.12195122, 0.15044248, 0.18137255, 0.19936709, 0.16006884, 0.20842105, 0.2451613, 0.16241299, 0.171875, 0.24350336, 0.19052088]
tsql_noisy_err = [0.13333334, 0.20731707, 0.05102041, 0.19318181, 0.2746479, 0.24431819, 0.18859649, 0.2, 0.22891566, 0.24884793, 0.23404256, 0.16788322, 0.21917808, 0.39112905, 0.20987654, 0.16666667, 0.12280702, 0.12691131, 0.35359117, 0.19109747, 0.26993865, 0.07020548, 0.083333336, 0.25, 0.112068966, 0.11873351, 0.1407767, 0.13291536, 0.20754717, 0.082474224, 0.18769231, 0.24183007, 0.11627907, 0.1375, 0.18386492, 0.21345165]
java_st_err = [0.027777778, 0.05496625, 0.08366534, 0.028478438, 0.183, 0.0623608, 0.11627907, 0.025316456, 0.05620438, 0.013661202, 0.22580644, 0.053435113, 0.0583691, 0.15625, 0.018867925, 0.015873017, 0.026402641, 0.10743801, 0.023002421, 0.035958905, 0.06918239, 0.028037382, 0.11784512, 0.072289154, 0.046296295, 0.021052632, 0.14925373, 0.01843318, 0.14925373, 0.21081081, 0.07917059, 0.036, 0.009708738, 0.07159353, 0.09047619, 0.12662722, 0.0375, 0.053097345, 0.033088237, 0.05376344, 0.05352798, 0.009433962, 0.0, 0.053030305, 0.0, 0.054545455, 0.018348623, 0.05263158, 0.07090464, 0.056986302, 0.024449877, 0.024922118, 0.054247696, 0.04506699, 0.059734512, 0.12195122, 0.0415625, 0.047557004, 0.061060857]
java8_st_err = [0.0, 0.184, 0.03168156, 0.07968128, 0.0545657, 0.11627907, 0.051923078, 0.060761347, 0.025316456, 0.013661202, 0.060944207, 0.18478261, 0.06870229, 0.21164021, 0.018867925, 0.015873017, 0.17094018, 0.026402641, 0.036020584, 0.062893085, 0.024213076, 0.10213243, 0.028037382, 0.060240965, 0.046296295, 0.036842104, 0.19402985, 0.01843318, 0.19402985, 0.036, 0.19459459, 0.009708738, 0.07728558, 0.11438679, 0.059768066, 0.050808314, 0.034375, 0.08243548, 0.029411765, 0.05109489, 0.05376344, 0.0, 0.016949153, 0.054545455, 0.0, 0.043560605, 0.018348623, 0.07017544, 0.047131147, 0.07334963, 0.04506699, 0.02200489, 0.046728972, 0.08943089, 0.04605263, 0.0570958, 0.042852674, 0.044960905, 0.044123713]
java_guava_err = [0.009090909, 0.0, 0.057142857, 0.01891253, 0.027108435, 0.055555556, 0.027272727, 0.042682927, 0.021084337, 0.014760148, 0.029596413, 0.021934759, 0.04347826, 0.02173913, 0.0, 0.026415095, 0.02173913, 0.045498546, 0.02173913, 0.011904762, 0.01971831, 0.008370535, 0.032857142, 0.028827038, 0.016604178, 0.030075189, 0.030571992, 0.0, 0.018518519, 0.034146342, 0.026216686, 0.012658228, 0.012048192, 0.027314112, 0.01986755, 0.018856065, 0.014102564, 0.027123848, 0.011956521, 0.0, 0.008358663, 0.022227112, 0.027888447, 0.032, 0.008130081, 0.041841004, 0.02718676, 0.00990099, 0.003322259, 0.012096774, 0.014102564, 0.034313727, 0.040697675, 0.016216217, 0.0091743115, 0.010256411, 0.10204082, 0.015503876, 0.026785715, 0.059541985, 0.0, 0.005952381, 0.020833334, 0.028409092, 0.039408866, 0.02173913, 0.015384615, 0.006779661, 0.014577259, 0.07768469, 0.029891305, 0.013937282, 0.01671123, 0.0065312046, 0.016649324, 0.0056369784, 0.0020325202, 0.01875, 0.03163017, 0.015384615, 0.015873017, 0.012411779, 0.025773196, 0.007304602, 0.016806724, 0.0192, 0.030120483, 0.013565891, 0.0068897638, 0.06122449, 0.011661808, 0.01396648, 0.01724138, 0.018957347, 0.0076045627, 0.012941176, 0.0114613185, 0.01146789, 0.014925373, 0.03125, 0.027171277, 0.010365854, 0.030674847, 0.020007696, 0.027237354, 0.052863438, 0.030776093, 0.022109918, 0.008720931, 0.023076924, 0.010309278, 0.0070339977, 0.023088023, 0.029411765, 0.03846154, 0.011292347, 0.01208981, 0.008213553, 0.020224718, 0.022801302, 0.012924667, 0.0091743115, 0.008032128, 0.0121555915, 0.055555556, 0.013020833, 0.048387095, 0.021276595, 0.0055762082, 0.008583691, 0.013977128, 0.07317073, 0.0038834952, 0.015492254, 0.0, 0.021276595, 0.0, 0.013333334, 0.016620498, 0.0044444446, 0.014563107, 0.0123152705, 0.019292604, 0.0028089888, 0.025551684, 0.017449664, 0.036793694, 0.039473683, 0.012738854, 0.02173913, 0.012552301, 0.022530328, 0.009334889, 0.00896861, 0.015873017, 0.0014245014, 0.02668938, 0.02, 0.0091047045, 0.024193548, 0.009057971, 0.008403362, 0.0141187925, 0.016611295, 0.013268999, 0.021903323, 0.02153846, 0.022857143, 0.018549748, 0.01724138, 0.014771049, 0.035799522, 0.019434629, 0.014925373, 0.0121630505, 0.018009478, 0.012345679, 0.020652622, 0.01636444, 0.018989379, 0.018196415, 0.01746507, 0.015415549, 0.033950616, 0.025889968, 0.031948883, 0.01591512, 0.028753994, 0.022144811, 0.018708508, 0.0, 0.02009329, 0.025510008, 0.018932875, 0.008219178, 0.008287293, 0.011363637, 0.016627869, 0.0123854345, 0.013295832, 0.011764706, 0.01183432, 0.013644453, 0.011353899, 0.021132713, 0.009639564, 0.020057306, 0.0118733505, 0.026113672, 0.026595745, 0.01898734, 0.013888889, 0.011940299, 0.007832898, 0.0078125, 0.016073687, 0.007858546, 0.0, 0.010752688, 0.021857923, 0.024656067, 0.00877193, 0.012912482, 0.024829932, 0.019278096, 0.022304833, 0.028831564, 0.017301038, 0.024096385, 0.024523161, 0.019933555, 0.02096436, 0.014506769, 0.017832648, 0.011281225, 0.01811806, 0.024007387, 0.009940358, 0.00862069, 0.008064516, 0.024597919, 0.010256411, 0.00973236, 0.023809524, 0.028735632, 0.017857144, 0.039473683, 0.011952192, 0.036697246, 0.049953748, 0.008130081, 0.07017544, 0.01827957, 0.015789473, 0.019398643, 0.02413273, 0.016746411, 0.0116959065, 0.0091759, 0.009006391, 0.008064516, 0.020966802, 0.02739726, 0.010601719, 0.009015122, 0.025974026, 0.013314313, 0.007743363, 0.014030612, 0.036697246, 0.009708738, 0.028571429, 0.0047393367, 0.020836597, 0.032663316, 0.026845638, 0.027726432, 0.01622718, 0.030927835, 0.01438849, 0.029816514, 0.0, 0.027777778, 0.011627907, 0.015384615, 0.038416762, 0.029940119, 0.03587444, 0.011627907, 0.025032938, 0.0, 0.040229887, 0.045380875, 0.07692308, 0.036956523, 0.03277635, 0.023465704, 0.015503876, 0.020100502, 0.004878049, 0.007317073, 0.0151351355, 0.020833334, 0.023169601, 0.03108108, 0.019125683, 0.011052551, 0.033557046, 0.1, 0.035714287, 0.17948718, 0.027431421, 0.024066092, 0.0, 0.023131672, 0.01, 0.009615385, 0.011904762, 0.01908397, 0.033557046, 0.05952381, 0.049382716, 0.02112676, 0.0, 0.017216643, 0.020618556, 0.011019284, 0.005524862, 0.0042432817, 0.0046296297, 0.004733728, 0.014247552, 0.026463512, 0.013192612, 0.037037037, 0.100890204, 0.008498584, 0.0085796, 0.029940119, 0.033472802, 0.027582478, 0.0065789474, 0.028481012, 0.025531914, 0.03133903, 0.00862069, 0.019902699, 0.013906447, 0.020427112, 0.0, 0.014364641, 0.0060975607, 0.026515152, 0.06944445, 0.0, 0.022403259, 0.06477733, 0.06278027, 0.010526316, 0.020833334, 0.014173228, 0.016, 0.010302198, 0.010384216, 0.012376934, 0.013335613, 0.012738854, 0.012351327, 0.034802783, 0.016438356, 0.028037382, 0.018382354, 0.03125, 0.00896861, 0.022988506, 0.030303031, 0.024725275, 0.020066889, 0.021518987, 0.01425332, 0.0118811885, 0.014925373, 0.0, 0.016216217, 0.022796353, 0.03409091, 0.028633406, 0.02283342, 0.03685092, 0.015065913, 0.025477707, 0.0, 0.028304921, 0.01726264, 0.024930747, 0.015609756, 0.024049217, 0.023870418, 0.02432886, 0.037527595, 0.10616438, 0.043164168, 0.0, 0.02568982, 0.034401875, 0.07865169, 0.013209393, 0.009484292, 0.023342175, 0.03508772, 0.008350731, 0.009410802, 0.008287293, 0.0, 0.00983965, 0.025423728, 0.017405063, 0.0128410915, 0.01101393, 0.0074247755, 0.030955585, 0.014054054, 0.03163017, 0.01859628, 0.031390134, 0.016466118, 0.014221861, 0.0131752305, 0.019969279, 0.0, 0.008324662, 0.022146508, 0.022102747, 0.013114754, 0.039215688, 0.02183406, 0.018181818, 0.021063905, 0.030470913, 0.021847345, 0.021341464, 0.03802589, 0.028241334, 0.01754386, 0.028455285, 0.035714287, 0.031860225, 0.022238975, 0.036741216, 0.03649635, 0.02870067, 0.014084507, 0.028571429, 0.030063292, 0.03277175, 0.024504084, 0.01058201, 0.028313253, 0.019572955, 0.013605442, 0.0272, 0.03539823, 0.016806724, 0.030303031, 0.0030395137, 0.03311258, 0.025270758, 0.013490725, 0.014492754, 0.03237519, 0.019512195, 0.024691358, 0.016853932, 0.028065894, 0.027777778, 0.021186441, 0.027083334, 0.012345679, 0.036764707, 0.02016129, 0.014492754, 0.017021276, 0.026595745, 0.030508475, 0.0, 0.048780486, 0.037037037, 0.022522522, 0.031578947, 0.034596376, 0.020533253, 0.010666667, 0.029689608, 0.010204081, 0.026219714, 0.021472393, 0.03076923, 0.011437909, 0.047003526, 0.01640135, 0.025452489, 0.03469388, 0.029612755, 0.022813689, 0.0, 0.033613447, 0.014336918, 0.020346647, 0.016949153, 0.0, 0.015015015]
java8_guava_err = [0.0, 0.055555556, 0.057142857, 0.009090909, 0.024096385, 0.014184397, 0.027272727, 0.042682927, 0.015060241, 0.012300123, 0.022502251, 0.016374929, 0.046671767, 0.02173913, 0.017924529, 0.0, 0.02173913, 0.036929056, 0.02173913, 0.011904762, 0.01690141, 0.007254464, 0.03884892, 0.028827038, 0.01658641, 0.019875236, 0.027613413, 0.033962265, 0.0, 0.018518519, 0.034146342, 0.012658228, 0.009638554, 0.018209409, 0.013245033, 0.015718328, 0.025076766, 0.008974359, 0.0, 0.010881393, 0.026079334, 0.009893456, 0.032, 0.028368793, 0.0312, 0.033333335, 0.008130081, 0.01210121, 0.006644518, 0.012096774, 0.020512821, 0.039386403, 0.039506175, 0.016216217, 0.0091743115, 0.010256411, 0.019302152, 0.06122449, 0.035019454, 0.059633028, 0.0, 0.005952381, 0.020833334, 0.022727273, 0.014778325, 0.02173913, 0.074809164, 0.012741652, 0.010169491, 0.011661808, 0.024456521, 0.017482517, 0.012032085, 0.005805515, 0.012486992, 0.0033783785, 0.0020325202, 0.01875, 0.02919708, 0.010256411, 0.010596027, 0.010598124, 0.020618556, 0.00658376, 0.012605042, 0.014446228, 0.030120483, 0.01195863, 0.005905512, 0.040816326, 0.005830904, 0.011173184, 0.01724138, 0.014218009, 0.022813689, 0.014117647, 0.0057306592, 0.014925373, 0.010157274, 0.02478134, 0.0, 0.00976801, 0.012269938, 0.028608583, 0.020030817, 0.030837005, 0.010704728, 0.0029069767, 0.0037926675, 0.0038387715, 0.01029601, 0.008196721, 0.0043290043, 0.0, 0.0, 0.0037641155, 0.008635579, 0.0061601643, 0.013483146, 0.019543974, 0.006116208, 0.008032128, 0.00849649, 0.004862237, 0.007832898, 0.033333335, 0.016129032, 0.017761989, 0.0074487897, 0.008583691, 0.003811944, 0.0038834952, 0.0, 0.016516516, 0.0, 0.0, 0.0, 0.013333334, 0.011080332, 0.008928572, 0.019512195, 0.012345679, 0.00857449, 0.0028089888, 0.012775842, 0.0067069083, 0.010512483, 0.039473683, 0.006369427, 0.02173913, 0.012552301, 0.01559792, 0.008158508, 0.01910828, 0.00896861, 0.0028490028, 0.033714287, 0.01, 0.0075872536, 0.016129032, 0.007246377, 0.01046738, 0.008403362, 0.009966778, 0.019637462, 0.012062727, 0.020015396, 0.011428571, 0.010344828, 0.0067453627, 0.0221881, 0.014771049, 0.013473546, 0.021582734, 0.0059701493, 0.0053003533, 0.004115226, 0.015807778, 0.011470709, 0.02125775, 0.02153846, 0.016475286, 0.013517863, 0.016029922, 0.01782711, 0.032258064, 0.031948883, 0.028753994, 0.015044248, 0.01810501, 0.01918764, 0.017581629, 0.0, 0.017211704, 0.008219178, 0.008287293, 0.011363637, 0.014985015, 0.0074149836, 0.015155279, 0.011764706, 0.01183432, 0.015037594, 0.012017167, 0.018596787, 0.011344538, 0.020057306, 0.013192612, 0.018708354, 0.026595745, 0.012658228, 0.011904762, 0.0089552235, 0.007832898, 0.010416667, 0.01519262, 0.0088408645, 0.010752688, 0.02078316, 0.0, 0.016393442, 0.00877193, 0.02449813, 0.022304833, 0.0136494255, 0.0123152705, 0.026636226, 0.0034602077, 0.013623978, 0.01628468, 0.011168682, 0.01330377, 0.013592233, 0.008385744, 0.015068493, 0.019320844, 0.026951673, 0.009940358, 0.008064516, 0.010344828, 0.010256411, 0.02347418, 0.00729927, 0.017006803, 0.022988506, 0.013157895, 0.0076923077, 0.007968128, 0.036697246, 0.03941338, 0.008130081, 0.03508772, 0.016146393, 0.015789473, 0.013574661, 0.01848249, 0.016746411, 0.007100797, 0.0058479533, 0.012912482, 0.00929692, 0.004032258, 0.015151516, 0.0107421875, 0.005041202, 0.012125535, 0.025974026, 0.007743363, 0.036363635, 0.010049449, 0.0058139535, 0.02138701, 0.028571429, 0.0047393367, 0.03517588, 0.023489933, 0.03986135, 0.014198783, 0.02877698, 0.025878003, 0.0, 0.028636884, 0.037037037, 0.011627907, 0.015384615, 0.029940119, 0.03882353, 0.032884903, 0.011785202, 0.011627907, 0.025099074, 0.0, 0.029268293, 0.011494253, 0.0, 0.030166881, 0.028138528, 0.020100502, 0.007751938, 0.004878049, 0.019855596, 0.004878049, 0.01923077, 0.035326086, 0.013661202, 0.012972973, 0.025974026, 0.018535681, 0.033557046, 0.1, 0.18421052, 0.024875622, 0.0, 0.030357143, 0.017985612, 0.01, 0.024802301, 0.009615385, 0.0246085, 0.035714287, 0.037037037, 0.01908397, 0.0, 0.021276595, 0.014347202, 0.005509642, 0.013745705, 0.0036832413, 0.0056577087, 0.0046296297, 0.008284024, 0.02760463, 0.007915568, 0.021582734, 0.099406525, 0.009065156, 0.037037037, 0.023978202, 0.0066730217, 0.033472802, 0.0065789474, 0.018929152, 0.022151899, 0.017021276, 0.018125553, 0.005172414, 0.041266795, 0.0076045627, 0.018570103, 0.0, 0.013259669, 0.0060975607, 0.02264151, 0.0625, 0.0, 0.014256619, 0.06477733, 0.06278027, 0.010526316, 0.018828452, 0.0062992126, 0.011000344, 0.018072288, 0.011295567, 0.012102448, 0.0062305294, 0.012738854, 0.012362638, 0.008219178, 0.018691588, 0.030267753, 0.018382354, 0.03125, 0.004484305, 0.022988506, 0.025252525, 0.021978023, 0.017207792, 0.021518987, 0.020066889, 0.00990099, 0.0, 0.0074626864, 0.016216217, 0.022796353, 0.03503788, 0.026064292, 0.033557046, 0.025467776, 0.011299435, 0.03821656, 0.025764896, 0.0, 0.013580247, 0.018450184, 0.014533259, 0.014634146, 0.01802935, 0.017902814, 0.04210336, 0.03532009, 0.10616438, 0.0, 0.029495718, 0.033646323, 0.07865169, 0.009300049, 0.008298756, 0.022781458, 0.033102766, 0.007518797, 0.0073589534, 0.009087318, 0.00837582, 0.0, 0.021186441, 0.01584786, 0.0113562625, 0.011235955, 0.0062524425, 0.020188425, 0.018629808, 0.0097402595, 0.023114355, 0.033783782, 0.020939086, 0.009222661, 0.012596506, 0.015360983, 0.008316008, 0.0, 0.01966627, 0.01362862, 0.013114754, 0.009803922, 0.01746725, 0.018181818, 0.04432133, 0.020795984, 0.016044261, 0.021341464, 0.043265305, 0.033376124, 0.02303523, 0.01754386, 0.03208556, 0.023782559, 0.030832477, 0.02435217, 0.03858521, 0.036615133, 0.014084507, 0.028571429, 0.036489606, 0.030063292, 0.023337223, 0.01058201, 0.025903614, 0.021352313, 0.013605442, 0.02907916, 0.030264817, 0.008403362, 0.03311258, 0.0030395137, 0.020100502, 0.02166065, 0.016835017, 0.023354564, 0.014492754, 0.024390243, 0.024691358, 0.011235955, 0.027439024, 0.027777778, 0.019830028, 0.022916667, 0.012345679, 0.036764707, 0.02016129, 0.014492754, 0.023608768, 0.004201681, 0.036842104, 0.0, 0.024390243, 0.037037037, 0.019837692, 0.021052632, 0.0144039225, 0.016474465, 0.02793482, 0.030852504, 0.008, 0.010204081, 0.023541454, 0.018062398, 0.03787879, 0.03533569, 0.019323671, 0.034979425, 0.025510205, 0.011363637, 0.019011406, 0.0, 0.033613447, 0.018839488, 0.013559322, 0.014336918, 0.0, 0.021021022]
antlr_err = [0.19101124, 0.20839813, 0.12890625, 0.42857143, 0.11182565, 0.16949153, 0.15467626, 0.060859643, 0.093333334, 0.16694611, 0.20300354, 0.055256933]
sqlite_err = [0.02173913, 0.22033899, 0.13095239, 0.13043478, 0.09915612, 0.11413044, 0.20430107, 0.07312253, 0.107569724, 0.15833333, 0.067567565, 0.091254756, 0.07446808, 0.098684214, 0.15326633, 0.09756097, 0.102564104, 0.101620026, 0.03827751, 0.09140894, 0.12921348, 0.1433121, 0.11308562, 0.060869563, 0.092269324, 0.116935484, 0.045454547, 0.06465517, 0.08645533, 0.12256809, 0.13764511, 0.09800919, 0.10973085, 0.087064676, 0.10776256, 0.16355556]
tsql_err = [0.02173913, 0.105882354, 0.067226894, 0.14893617, 0.100271, 0.12903225, 0.14194915, 0.10358566, 0.09090909, 0.08431373, 0.09885932, 0.040268455, 0.071428575, 0.11764706, 0.071428575, 0.11, 0.08486239, 0.09867452, 0.061904762, 0.086021505, 0.106687896, 0.09396434, 0.052173913, 0.119873814, 0.06779661, 0.007575758, 0.107860014, 0.047826085, 0.13372093, 0.11731844, 0.06622516, 0.07373272, 0.0822335, 0.0862069, 0.07537012, 0.110918544]
quorum_err = [0.04347826, 0.05882353, 0.08695652, 0.09677419, 0.01980198, 0.0625, 0.0, 0.0625, 0.029535865, 0.0625, 0.0, 0.0625, 0.0392562, 0.023255814, 0.0, 0.0625, 0.039215688, 0.11594203, 0.07692308, 0.0625, 0.020408163, 0.026666667, 0.03420523, 0.060606062, 0.028571429, 0.011627907, 0.02173913, 0.048611112, 0.14285715, 0.04597701, 0.078947365, 0.04597701, 0.044692736, 0.048611112, 0.01010101, 0.06666667, 0.06716418, 0.046153847, 0.046153847, 0.07317073, 0.054263566, 0.09166667, 0.00990099, 0.06699752, 0.044444446, 0.044612218, 0.044444446, 0.035714287, 0.035897437, 0.0974359, 0.035714287, 0.059679765, 0.120508984, 0.035714287, 0.03373494, 0.05263158, 0.027842227, 0.086666666, 0.027027028, 0.041526373, 0.032258064, 0.06954437, 0.032258064, 0.0, 0.0, 0.0040816325, 0.037456445, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02982555, 0.032258064, 0.0, 0.023076924, 0.093023255, 0.02690583, 0.09803922, 0.041800644, 0.05, 0.030150754, 0.04901961, 0.011111111, 0.02027027, 0.009933775, 0.024390243, 0.0, 0.08130081, 0.03529412, 0.1, 0.05357143, 0.01923077, 0.05901639, 0.072972976, 0.037037037, 0.043624163, 0.043149944, 0.009708738, 0.020942409, 0.0546875, 0.022727273, 0.04404145, 0.05574913, 0.10724638, 0.042043086]


language_data = [antlr_err, java_st_err, java8_st_err, java_guava_err, java8_guava_err, sqlite_err, tsql_err, sqlite_noisy_err, tsql_noisy_err]
labels = ["antlr\nn=12", "java_st\nn=59", "java8_st\nn=59", "java_guava\nn=511", "java8_guava\nn=511", "sqlite\nn=36", "tsql\nn=36", "sqlite_noisy\nn=36", "tsql_noisy\nn=36"]
fig = plt.figure()
ax = plt.subplot(111)
ax.boxplot(language_data,
           whis=[10, 90], # 10 and 90 % whiskers
           widths=.35,
           labels=labels,
           showfliers=False)
ax.set_xticklabels(labels, rotation=60, fontsize=12)
plt.xticks(range(1,len(labels)+1), labels, rotation=60)
pylab.ylim([0,.28])
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xlabel("Grammar and corpus size", fontsize=14)
ax.set_ylabel("Misclassification Error Rate", fontsize=14)
# ax.set_title("Leave-one-out Validation Using Edit Distance / Error Rate\nBetween Formatted and Original File")
plt.tight_layout()
fig.savefig('images/leave_one_out.pdf', format='pdf')
plt.show()
