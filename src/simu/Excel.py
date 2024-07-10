import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))

parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)
import simu.main as main
import pandas as pd
import openpyxl



a={'Frequentation': {'HP': [30.0, 30.6, 31.2, 31.8, 32.4, 33.0, 33.6, 34.2, 34.8, 35.4, 36.0, 36.6, 37.2, 37.8, 38.4, 39.0, 39.6, 40.2, 40.8, 41.4, 42.0, 42.6, 43.2, 43.8, 44.4, 45.0, 45.6, 46.2, 46.8, 47.4, 48.0, 48.6, 49.4, 50.2, 51.0, 51.8, 52.4, 52.8, 53.2, 53.6, 54.0, 54.0, 54.0, 54.0, 54.0, 54.0, 54.0, 54.0], 'HC': [14.0, 14.7, 14.7, 15.0, 15.3, 15.7, 16.0, 16.3, 16.7, 16.7, 17.0, 17.7, 17.7, 18.0, 18.3, 18.7, 19.0, 19.3, 19.7, 19.7, 20.0, 20.7, 20.7, 21.0, 21.3, 21.7, 22.0, 22.3, 22.7, 22.7, 23.0, 23.7, 23.7, 24.0, 24.3, 24.3, 24.7, 25.0, 25.0, 25.0, 25.3, 25.7, 25.7, 26.0, 26.3, 26.3, 26.7, 27.0], 'VacantHP': [30.0, 29.4, 28.8, 28.2, 27.6, 27.0, 26.4, 25.8, 25.2, 24.6, 24.0, 23.4, 22.8, 22.2, 21.6, 21.0, 20.4, 19.8, 19.2, 18.6, 18.0, 17.4, 16.8, 16.2, 15.6, 15.0, 14.4, 13.8, 13.2, 12.6, 12.0, 11.4, 10.6, 9.8, 9.0, 8.2, 7.6, 7.2, 6.8, 6.4, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0], 'VacantHC': [16.0, 15.3, 15.3, 15.0, 14.7, 14.3, 14.0, 13.7, 13.3, 13.3, 13.0, 12.3, 12.3, 12.0, 11.7, 11.3, 11.0, 10.7, 10.3, 10.3, 10.0, 9.3, 9.3, 9.0, 8.7, 8.3, 8.0, 7.7, 7.3, 7.3, 7.0, 6.3, 6.3, 6.0, 5.7, 5.7, 5.3, 5.0, 5.0, 5.0, 4.7, 4.3, 4.3, 4.0, 3.7, 3.7, 3.3, 3.0], 'Anniversaires': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, 'Revenus': {'Five': [3660.0, 3794.0, 3848.0, 3902.0, 4036.0, 4090.0, 4144.0, 4278.0, 4332.0, 4386.0, 4440.0, 4574.0, 4628.0, 4682.0, 4816.0, 4870.0, 4924.0, 5058.0, 5112.0, 5166.0, 5220.0, 5354.0, 5408.0, 5462.0, 5596.0, 5650.0, 5704.0, 5838.0, 5892.0, 5946.0, 6000.0, 6134.0, 6188.0, 6242.0, 6376.0, 6430.0, 6484.0, 6618.0, 6672.0, 6726.0, 6780.0, 6860.0, 6860.0, 6860.0, 6940.0, 6940.0, 6940.0, 7020.0], 'Beach': [3310.0, 3358.0, 3406.0, 3524.0, 3572.0, 3620.0, 3738.0, 3786.0, 3834.0, 3882.0, 4000.0, 4048.0, 4096.0, 4214.0, 4262.0, 4310.0, 4428.0, 4476.0, 4524.0, 4572.0, 4690.0, 4738.0, 4786.0, 4904.0, 4952.0, 5000.0, 5118.0, 5166.0, 5214.0, 5262.0, 5380.0, 5428.0, 5476.0, 5594.0, 5642.0, 5690.0, 5808.0, 5856.0, 5904.0, 5952.0, 6070.0, 6070.0, 6070.0, 6140.0, 6140.0, 6140.0, 6210.0, 6210.0], 'Padel': [1744.0, 1800.0, 1824.0, 1848.0, 1872.0, 1928.0, 1952.0, 1976.0, 2032.0, 2056.0, 2080.0, 2136.0, 2160.0, 2184.0, 2208.0, 2264.0, 2288.0, 2312.0, 2368.0, 2392.0, 2416.0, 2472.0, 2496.0, 2520.0, 2544.0, 2600.0, 2624.0, 2648.0, 2704.0, 2728.0, 2752.0, 2808.0, 2856.0, 2904.0, 2952.0, 3000.0, 3024.0, 3024.0, 3024.0, 3024.0, 3024.0, 3024.0, 3024.0, 3024.0, 3024.0, 3024.0, 3024.0, 3024.0], 'Bar': [3369.0, 3445.2000000000003, 3479.3999999999996, 3528.6000000000004, 3592.7999999999997, 3639.0, 3688.2000000000003, 3752.3999999999996, 3798.6000000000004, 3832.7999999999997, 3882.0, 3958.2000000000003, 3992.3999999999996, 4041.6000000000004, 4105.799999999999, 4152.0, 4201.200000000001, 4265.4, 4311.6, 4345.799999999999, 4395.0, 4471.200000000001, 4505.4, 4554.6, 4618.799999999999, 4665.0, 4714.200000000001, 4778.4, 4824.6, 4858.799999999999, 4908.0, 4984.200000000001, 5025.6, 5082.0, 5153.4, 5194.799999999999, 5244.0, 5301.0, 5328.0, 5355.0, 5397.0, 5427.0, 5427.0, 5442.0, 5472.0, 5472.0, 5487.0, 5517.0], 'Abonnements': [0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998, 0, 0, 0, 1998.9999999999998], 'Evenement Club House': [0, 0, 0, 252.04285714285714, 0, 0, 0, 268.0285714285714, 0, 0, 0, 282.7285714285715, 0, 0, 0, 296.57142857142856, 0, 0, 0, 310.4142857142857, 0, 0, 0, 325.3285714285714, 0, 0, 0, 341.3142857142857, 0, 0, 0, 356.0142857142858, 0, 0, 0, 371.0571428571428, 0, 0, 0, 382.5, 0, 0, 0, 388.7142857142858, 0, 0, 0, 394.07142857142856], 'Abo loss': [-1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0, -1625.0]}, 'Total revenus': {'': [10458.0, 10772.2, 10932.4, 13428.642857142857, 11447.8, 11652.0, 11897.2, 14434.42857142857, 12371.6, 12531.8, 12777.0, 15372.928571428572, 13251.4, 13496.6, 13766.8, 16266.571428571428, 14216.2, 14486.4, 14690.6, 17160.214285714286, 15096.0, 15410.2, 15570.400000000001, 18139.92857142857, 16085.8, 16290.0, 16535.2, 19145.714285714286, 17009.6, 17169.8, 17415.0, 20084.214285714286, 17920.6, 18197.0, 18498.4, 21059.85714285714, 18935.0, 19174.0, 19303.0, 21813.5, 19646.0, 19756.0, 19756.0, 22228.714285714286, 19951.0, 19951.0, 20036.0, 22539.071428571428]}, 'Charges': {'Eau': [0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0, 0, 0, 0, 2000.0], 'Electricite': [0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0], 'Nettoyage': [0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0, 0, 0, 0, 100.0], 'Abonnements': [0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0], 'Mat riels': [0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0, 0, 0, 0, 1000.0], 'Salaires': [0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0, 0, 0, 0, 3000.0], 'Assurance': [0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0, 0, 0, 0, 200.0], 'Securite': [0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0, 0, 0, 0, 150.0], 'Conso bar': [1981.764705882353, 2026.5882352941178, 2046.705882352941, 2075.6470588235297, 2113.4117647058824, 2140.5882352941176, 2169.5294117647063, 2207.2941176470586, 2234.4705882352946, 2254.5882352941176, 2283.529411764706, 2328.3529411764707, 2348.470588235294, 2377.4117647058824, 2415.176470588235, 2442.3529411764707, 2471.2941176470595, 2509.0588235294117, 2536.2352941176473, 2556.3529411764703, 2585.294117647059, 2630.117647058824, 2650.235294117647, 2679.1764705882356, 2716.941176470588, 2744.1176470588234, 2773.058823529412, 2810.8235294117644, 2838.0000000000005, 2858.117647058823, 2887.0588235294117, 2931.882352941177, 2956.2352941176473, 2989.4117647058824, 3031.4117647058824, 3055.7647058823527, 3084.7058823529414, 3118.2352941176473, 3134.1176470588234, 3150.0, 3174.7058823529414, 3192.3529411764707, 3192.3529411764707, 3201.1764705882356, 3218.823529411765, 3218.823529411765, 3227.6470588235293, 3245.294117647059], 'IS': [3020.75, 3099.3, 3139.35, 3200.65, 3268.2, 3319.25, 3380.55, 3448.1, 3499.15, 3539.2, 3600.5, 3679.05, 3719.1, 3780.4, 3847.95, 3899.0, 3960.3, 4027.85, 4078.9, 4118.95, 4180.25, 4258.8, 4298.85, 4360.15, 4427.7, 4478.75, 4540.05, 4607.6, 4658.65, 4698.7, 4760.0, 4838.55, 4886.4, 4955.5, 5030.85, 5078.7, 5140.0, 5199.75, 5232.0, 5264.25, 5317.75, 5345.25, 5345.25, 5366.5, 5394.0, 5394.0, 5415.25, 5442.75], 'TVA': [2416.6, 2479.4400000000005, 2511.48, 2560.5200000000004, 2614.56, 2655.4, 2704.4400000000005, 2758.48, 2799.32, 2831.36, 2880.4, 2943.2400000000002, 2975.28, 3024.32, 3078.36, 3119.2000000000003, 3168.2400000000002, 3222.28, 3263.1200000000003, 3295.16, 3344.2000000000003, 3407.0400000000004, 3439.0800000000004, 3488.12, 3542.16, 3583.0, 3632.0400000000004, 3686.0800000000004, 3726.92, 3758.96, 3808.0, 3870.84, 3909.12, 3964.4, 4024.6800000000003, 4062.96, 4112.0, 4159.8, 4185.6, 4211.400000000001, 4254.2, 4276.2, 4276.2, 4293.2, 4315.2, 4315.2, 4332.2, 4354.2], 'Communication': [522.9, 538.61, 546.62, 671.4321428571429, 572.39, 582.6, 594.86, 721.7214285714285, 618.58, 626.59, 638.85, 768.6464285714287, 662.57, 674.83, 688.34, 813.3285714285714, 710.8100000000001, 724.32, 734.5300000000001, 858.0107142857144, 754.8000000000001, 770.5100000000001, 778.5200000000001, 906.9964285714285, 804.29, 814.5, 826.7600000000001, 957.2857142857143, 850.48, 858.49, 870.75, 1004.2107142857144, 896.03, 909.85, 924.9200000000001, 1052.992857142857, 946.75, 958.7, 965.1500000000001, 1090.675, 982.3000000000001, 987.8000000000001, 987.8000000000001, 1111.4357142857143, 997.5500000000001, 997.5500000000001, 1001.8000000000001, 1126.9535714285714]}, 'Total charges': {'': [7942.014705882353, 8143.938235294118, 8244.155882352941, 16058.249201680672, 8568.56176470588, 8697.838235294117, 8849.379411764708, 16685.595546218487, 9151.520588235295, 9251.738235294119, 9403.279411764706, 17269.2893697479, 9705.420588235294, 9856.961764705882, 10029.826470588236, 17823.881512605043, 10310.64411764706, 10483.508823529412, 10612.785294117648, 18378.473655462185, 10864.54411764706, 11066.467647058826, 11166.685294117648, 18984.442899159665, 11491.091176470589, 11620.367647058823, 11771.908823529413, 19611.78924369748, 12074.05, 12174.267647058821, 12325.808823529413, 20195.483067226894, 12647.785294117648, 12819.161764705883, 13011.861764705884, 20800.41756302521, 13283.45588235294, 13436.485294117647, 13516.867647058823, 21266.325, 13728.95588235294, 13801.602941176468, 13801.602941176468, 21522.31218487395, 13925.573529411766, 13925.573529411766, 13976.897058823528, 21719.197689075634]}, 'Resultat': {'': [2515.985294117647, 2628.2617647058823, 2688.2441176470584, -2629.606344537815, 2879.2382352941186, 2954.161764705883, 3047.8205882352922, -2251.166974789916, 3220.0794117647056, 3280.0617647058807, 3373.7205882352937, -1896.3607983193288, 3545.979411764705, 3639.638235294118, 3736.9735294117636, -1557.3100840336156, 3905.555882352941, 4002.891176470588, 4077.8147058823524, -1218.2593697478987, 4231.4558823529405, 4343.732352941175, 4403.714705882354, -844.5143277310963, 4594.70882352941, 4669.632352941177, 4763.291176470588, -466.0749579831936, 4935.549999999999, 4995.532352941178, 5089.191176470587, -111.26878151260826, 5272.814705882351, 5377.838235294117, 5486.538235294118, 259.43957983193104, 5651.5441176470595, 5737.514705882353, 5786.132352941177, 547.1749999999993, 5917.0441176470595, 5954.397058823532, 5954.397058823532, 706.4021008403361, 6025.426470588234, 6025.426470588234, 6059.102941176472, 819.8737394957934]}}
def dictToDataFrame(dic):

    df = pd.DataFrame.from_dict({(level1, level2): value 
							for level1, inner_dict in dic.items() 
							for level2, value in inner_dict.items()}, orient='index')
    df.index=pd.MultiIndex.from_tuples(df.index) 
    print(df)
    df.to_excel('ajout_amo.xlsx', index = True)
    return df






