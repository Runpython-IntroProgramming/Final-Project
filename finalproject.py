question=input("Enter name of currency.")
if question is "US Dollar":
    user=input("Enter amount of US Dollars to convert.")
    currencies = {'Euro':.942218, 'Pound':.794856, 'Rupee':67.412529, 
'Australian Dollar':1.341483, 'Canadian Dollar':1.320036, 'Singapore Dollar':1.424582, 
'Swiss Franc':1.016520, 'Malaysian Rinnggit':4.420300, 'Japanese Yen':114.212492, 'Chinese Yuan Renminbi':6.880900, 'Argentine Peso':15.994313, 'Bahraini Dinar':0.377000, 
'Botswana Pula':10.834236, 'Brazilian Real':3.376349, 'Bruneian Dollar':1.424582, 'Bulgarian Lev':1.843010, 'Chilean Peso':654.800000, 
'Colombian Peso':3003.499994, 'Croatian Kuna':7.102514, 'Czech Koruna':25.489149, 'Danish Krone':7.009617, 'Emirati Dirham':3.673000, 'Hong Kong Dollar':7.756443, 'Hungarian Forint':296.213068, 'Icelandic Krona':111.510000, 
'Indonesian Rupiah':13352.062264, 'Iranian Rial':32150.000001, 'Israeli Shekel':3.813926, 'Kazakhstani Tenge':334.570007, 'Kuwaiti Dinar':0.304875, 'Latvian Lat':0.662191, 'Libyan Dinar':1.417500, 'Lithuanian Litas':3.253290,'Mexican Peso':20.315152, 'Nepalese Rupee':107.699997, 'New Zealand Dollar':1.393270, 'Norwegian Krone':8.433343, 'Omani Rial':0.384900, 
'Pakistani Rupee':104.750000, 'Philippine Peso':49.750000, 'Polish Zloty':4.184430, 'Qatari Riyal':3.641200, 'Romanian New Leu':4.240725, 'Russian Ruble':63.498941, 
'Saudi Arabian Riyal':3.750250, 'South African Rand':13.654455, 'South Korean Won':1164.612381, 'Sri Lankan Rupee':148.320007, 'Swedish Krona':9.128824, 'Taiwan New Dollar':31.756537, 'Thai Baht':35.647564, 'Trinidadian Dollar':6.680000, 'Turkish Lira':3.452651, 'Venezuelan Bolivar':9.975000}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies:
        k=(currencies[user1])
    l=user
    m=k*(float(l))
    n=print(round(m,2))
    print(user1 +"s")
if question is "Euro":
    user=input("Enter amount of Euros to convert.")
    currencies1 = {'US Dollar':1.0444611,'Pound':0.841020, 'Rupee':70.874008, 
'Australian Dollar':1.439401, 'Canadian Dollar':1.399551, 'Singapore Dollar':1.511327, 'Swiss Franc':1.068884, 'Malaysian Rinnggit':4.677768, 'Japanese Yen':121.910452, 
'Chinese Yuan Renminbi':7.259663, 'Argentine Peso':16.549375, 'Bahraini Dinar':0.393871, 
'Botswana Pula':11.338444, 'Brazilian Real':3.520775, 'Bruneian Dollar':1.511327, 'Bulgarian Lev':1.956431, 'Chilean Peso':707.568341, 'Colombian Peso':3146.212774, 'Croatian Kuna':7.531657, 'Czech Koruna':27.022209, 'Danish Krone':7.434797, 'Emirati Dirham':3.836961, 'Hong Kong Dollar':8.113706, 
'Hungarian Forint':311.688823, 'Icelandic Krona':118.725100, 'Indonesian Rupiah':13959.519837, 'Iranian Rial':33729.771931, 'Israeli Shekel':4.031584, 
'Kazakhstani Tenge':350.095382, 'Kuwaiti Dinar':0.319648, 'Latvian Lat':0.702800, 'Libyan Dinar':1.498800, 'Lithuanian Litas':3.452800,'Mexican Peso':21.315080, 'Nepalese Rupee':113.355307, 'New Zealand Dollar':1.504826, 'Norwegian Krone':9.048759, 'Omani Rial':0.402175, 'Pakistani Rupee':109.496068, 'Philippine Peso':52.217003, 'Polish Zloty':4.420556, 'Qatari Riyal':3.803115, 'Romanian New Leu':4.520514, 'Russian Ruble':64.652624, 
'Saudi Arabian Riyal':3.918885, 'South African Rand':14.712153, 'South Korean Won':1240.730986, 'Sri Lankan Rupee':155.720127, 'Swedish Krona':9.761674, 'Taiwan New Dollar':33.425181, 'Thai Baht':37.454247, 'Trinidadian Dollar':7.039503, 'Turkish Lira':3.689053, 'Venezuelan Bolivar':10.435727}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies1:
        k1=(currencies1[user1])
    l1=user
    m1=k1*(float(l1))
    n=print(round(m1,2))
    print(user1 +"s")
if question is "Pound":
    user=input("Enter amount of Pounds to convert.")
    currencies2 = {'US Dollar':1.242148,'Euro':1.188863, 'Rupee':84.274008, 
'Australian Dollar':1.711932, 'Canadian Dollar':1.664254, 'Singapore Dollar':1.795829, 
'Swiss Franc':1.270752, 'Malaysian Rinnggit':5.562338, 'Japanese Yen':144.989071, 
'Chinese Yuan Renminbi':8.632587, 'Argentine Peso':19.679903, 'Bahraini Dinar':0.468352, 
'Botswana Pula':13.482490, 'Brazilian Real':4.186473, 
'Bruneian Dollar':1.795829, 'Bulgarian Lev':2.326363, 'Chilean Peso':842.155239, 
'Colombian Peso':3734.064349, 'Croatian Kuna':8.954631, 'Czech Koruna':32.119829, 
'Danish Krone':8.839208, 'Emirati Dirham':4.562527, 'Hong Kong Dollar':9.647794, 
'Hungarian Forint':370.540300, 'Icelandic Krona':141.169343, 
'Indonesian Rupiah':16639.918787, 'Iranian Rial':40108.102146, 'Israeli Shekel':4.793840, 
'Kazakhstani Tenge':416.298708, 'Kuwaiti Dinar':0.380093, 'Latvian Lat':0.835533, 'Libyan Dinar':1.782224, 'Lithuanian Litas':4.104906,
'Mexican Peso':25.316616, 'Nepalese Rupee':134.790890, 'New Zealand Dollar':1.789247, 'Norwegian Krone':10.758439, 'Omani Rial':0.478226, 
'Pakistani Rupee':130.203721, 'Philippine Peso':62.087035, 'Polish Zloty':5.257402, 'Qatari Riyal':4.522040, 'Romanian New Leu':5.372440, 'Russian Ruble':76.891957, 
'Saudi Arabian Riyal':4.659887, 'South African Rand':17.500093, 'South Korean Won':1474.791124, 'Sri Lankan Rupee':185.166932, 
'Swedish Krona':11.609221, 'Taiwan New Dollar':39.737169, 'Thai Baht':44.556956, 'Trinidadian Dollar':8.370679, 'Turkish Lira':4.379305, 'Venezuelan Bolivar':12.409117}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies2:
        k2=(currencies2[user1])
    l2=user
    m2=k2*(float(l2))
    n=print(round(m2,2))
    print(user1 +"s")
if question is "Rupee":
    user=input("Enter amount of Rupees to convert.")
    currencies3 = {'US Dollar':0.014714,'Euro':0.014156, 'Pound':0.011910, 'Australian Dollar':0.020277, 'Canadian Dollar':0.019672, 'Singapore Dollar':0.021256, 'Swiss Franc':0.015133, 'Malaysian Rinnggit':0.065916, 'Japanese Yen':1.7334631, 'Chinese Yuan Renminbi':0.102251, 'Argentine Peso':0.233074, 'Bahraini Dinar':0.005547, 'Botswana Pula':0.159656, 'Brazilian Real':0.049256, 
'Bruneian Dollar':0.021256, 'Bulgarian Lev':0.027702, 'Chilean Peso':9.941914, 'Colombian Peso':44.04222, 'Croatian Kuna':0.106630, 'Czech Koruna':0.382511, 'Danish Krone':0.105244, 'Emirati Dirham':0.054036, 'Hong Kong Dollar':0.114270, 
'Hungarian Forint':4.400956, 'Icelandic Krona':1.679694, 'Indonesian Rupiah':198.046513, 'Iranian Rial':475.875894, 'Israeli Shekel':0.056592, 'Kazakhstani Tenge':4.931819, 'Kuwaiti Dinar':0.004508, 'Latvian Lat':0.009949, 'Libyan Dinar':0.021153, 'Lithuanian Litas':0.048879,'Mexican Peso':0.300681, 'Nepalese Rupee':1.601510, 'New Zealand Dollar':0.021245, 'Norwegian Krone':0.128048, 'Omani Rial':0.005660, 'Pakistani Rupee':1.541534, 'Philippine Peso':0.734572, 'Polish Zloty':0.062510, 'Qatari Riyal':0.053575, 'Romanian New Leu':0.063880, 'Russian Ruble':0.903881, 'Saudi Arabian Riyal':0.055189, 'South African Rand':0.205299, 'South Korean Won':17.560662, 'Sri Lankan Rupee':2.197315, 
'Swedish Krona':0.137682, 'Taiwan New Dollar':0.472263, 'Thai Baht':0.529890, 'Trinidadian Dollar':0.098879, 'Turkish Lira':0.051952, 'Venezuelan Bolivar':0.146868}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies3:
        k3=(currencies3[user1])
    l3=user
    m3=k3*(float(l3))
    n=print(round(m3,2))
    print(user1 +"s")

if question is "Australian Dollar":
    user=input("Enter amount of Australian Dollars to convert.")
    currencies4 = {'US Dollar':0.725529,'Euro':0.698169, 'Pound':0.587141, 'Rupee':49.300586, 'Canadian Dollar':0.969983, 'Singapore Dollar':1.048157, 'Swiss Franc':0.746332, 'Malaysian Rinnggit':3.248919, 'Japanese Yen':85.501910, 'Chinese Yuan Renminbi':5.043007, 'Argentine Peso':11.495702, 'Bahraini Dinar':0.273521, 'Botswana Pula':7.872715, 'Brazilian Real':2.428877, 'Bruneian Dollar':1.048157, 'Bulgarian Lev':1.365990, 'Chilean Peso':490.461954, 'Colombian Peso':2166.865670, 'Croatian Kuna':5.258816, 'Czech Koruna':18.863067, 'Danish Krone':5.190633, 'Emirati Dirham':2.664723, 'Hong Kong Dollar':5.634337, 
'Hungarian Forint':217.053114, 'Icelandic Krona':82.826384, 'Indonesian Rupiah':9755.782661, 'Iranian Rial':23456.350721, 'Israeli Shekel':2.789593, 'Kazakhstani Tenge':243.175551, 'Kuwaiti Dinar':0.222375, 'Latvian Lat':0.490673, 'Libyan Dinar':1.033879, 'Lithuanian Litas':2.410637,'Mexican Peso':14.824184, 'Nepalese Rupee':78.971114, 'New Zealand Dollar':1.047752, 'Norwegian Krone':6.316391, 'Omani Rial':0.279038, 'Pakistani Rupee':76.071710, 'Philippine Peso':36.280075, 'Polish Zloty':3.085081, 'Qatari Riyal':2.641832, 'Romanian New Leu':3.150981, 'Russian Ruble':44.567401, 'Saudi Arabian Riyal':2.721822, 'South African Rand':10.122442, 'South Korean Won':865.698332, 'Sri Lankan Rupee':108.350492, 
'Swedish Krona':6.789464, 'Taiwan New Dollar':23.275421, 'Thai Baht':26.130672, 'Trinidadian Dollar':4.861268, 'Turkish Lira':2.561928, 'Venezuelan Bolivar':7.251662}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies4:
        k4=(currencies4[user1])
    l4=user
    m4=k4*(float(l4))
    n=print(round(m4,2))
    print(user1 + "s")
if question is "Canadian Dollar":
    user=input("Enter amount of Canadian Dollars to convert.")
    currencies5 = {'US Dollar':0.744763,'Euro':0.714333, 'Pound':0.607716, 'Rupee':50.923156, 'Australian Dollar':1.029404, 'Singapore Dollar':1.078676, 'Swiss Franc':0.764258, 'Malaysian Rinnggit':3.343985, 'Japanese Yen':87.430071, 'Chinese Yuan Renminbi':5.184071, 'Argentine Peso':11.871294, 'Bahraini Dinar':0.280478, 'Botswana Pula':7.983113, 'Brazilian Real':2.425726, 'Bruneian Dollar':1.078676, 'Bulgarian Lev':1.398359, 'Chilean Peso':502.324360, 'Colombian Peso':2219.347526, 'Croatian Kuna':5.404572, 'Czech Koruna':19.303507, 'Danish Krone':5.310478, 'Emirati Dirham':2.735142, 'Hong Kong Dollar':5.776539, 
'Hungarian Forint':221.013959, 'Icelandic Krona':85.141290, 'Indonesian Rupiah':10016.672725, 'Iranian Rial':24110.952861, 'Israeli Shekel':2.877903, 'Kazakhstani Tenge':248.177336, 'Kuwaiti Dinar':0.228568, 'Latvian Lat':0.502033, 'Libyan Dinar':1.070075, 'Lithuanian Litas':2.466447,'Mexican Peso':15.578824, 'Nepalese Rupee':81.423413, 'New Zealand Dollar':1.073969, 'Norwegian Krone':6.438324, 'Omani Rial':0.286361, 'Pakistani Rupee':77.991568, 'Philippine Peso':37.066848, 'Polish Zloty':3.138504, 'Qatari Riyal':2.711160, 'Romanian New Leu':3.231597, 'Russian Ruble':45.441002, 'Saudi Arabian Riyal':2.793605, 'South African Rand':10.261239, 'South Korean Won':899.851990, 'Sri Lankan Rupee':111.699534, 
'Swedish Krona':6.812450, 'Taiwan New Dollar':24.121380, 'Thai Baht':26.755235, 'Trinidadian Dollar':4.989166, 'Turkish Lira':2.667641, 'Venezuelan Bolivar':7.428861}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies5:
        k5=(currencies5[user1])
    l5=user
    m5=k5*(float(l5))
    n=print(round(m5,2))
    print(user1 + "s")
if question is "Singapore Dollar":
    user=input("Enter amount of Singapore Dollars to convert.")
    currencies6 = {'US Dollar':0.690433,'Euro':0.662120, 'Pound':0.563418, 'Rupee':47.176378, 'Australian Dollar':0.954510, 'Canadian Dollar':0.926764, 'Swiss Franc':0.708379, 'Malaysian Rinnggit':3.100044, 'Japanese Yen':81.026341, 'Chinese Yuan Renminbi':4.805897, 'Argentine Peso':11.006243, 'Bahraini Dinar':0.260017, 'Botswana Pula':7.400752, 'Brazilian Real':2.248522, 'Bruneian Dollar':1.000000, 'Bulgarian Lev':1.297079, 'Chilean Peso':465.409136, 'Colombian Peso':2056.869334, 'Croatian Kuna':5.010122, 'Czech Koruna':17.887233, 'Danish Krone':4.922229, 'Emirati Dirham':2.535615, 'Hong Kong Dollar':5.355262, 
'Hungarian Forint':204.855165, 'Icelandic Krona':78.930305, 'Indonesian Rupiah':9288.533459, 'Iranian Rial':22352.079074, 'Israeli Shekel':2.667729, 'Kazakhstani Tenge':230.073008, 'Kuwaiti Dinar':0.211894, 'Latvian Lat':0.465338, 'Libyan Dinar':0.992014, 'Lithuanian Litas':2.286166,'Mexican Peso':14.445158, 'Nepalese Rupee':75.483643, 'New Zealand Dollar':0.996089, 'Norwegian Krone':5.967550, 'Omani Rial':0.265471, 'Pakistani Rupee':72.302148, 'Philippine Peso':34.362852, 'Polish Zloty':2.910657, 'Qatari Riyal':2.513383, 'Romanian New Leu':2.995556, 'Russian Ruble':42.117349, 'Saudi Arabian Riyal':2.589676, 'South African Rand':9.511847, 'South Korean Won':834.254680, 'Sri Lankan Rupee':103.551147, 
'Swedish Krona':6.316758, 'Taiwan New Dollar':22.373123, 'Thai Baht':24.802027, 'Trinidadian Dollar':4.625211, 'Turkish Lira':2.473636, 'Venezuelan Bolivar':6.886932}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies6:
        k6=(currencies6[user1])
    l6=user
    m6=k6*(float(l6))
    n=print(round(m6,2))
    print(user1 + "s") 
if question is "Swiss Franc":
    user=input("Enter amount of Swiss Francs to convert.")
    currencies7 = {'US Dollar':0.973175,'Euro':0.935232, 'Pound':0.795319, 'Rupee':66.442235, 'Australian Dollar':1.348506, 'Canadian Dollar':1.306463, 'Singapore Dollar':1.411304, 'Malaysian Rinnggit':4.369555, 'Japanese Yen':114.542010, 'Chinese Yuan Renminbi':6.773922, 'Argentine Peso':15.512837, 'Bahraini Dinar':0.366011, 'Botswana Pula':10.431159, 'Brazilian Real':3.177778, 'Bruneian Dollar':1.411304, 'Bulgarian Lev':1.827937, 'Chilean Peso':655.630002, 'Colombian Peso':2898.212424, 'Croatian Kuna':7.074774, 'Czech Koruna':25.261529, 'Danish Krone':6.953093, 'Emirati Dirham':3.573985, 'Hong Kong Dollar':7.548526, 
'Hungarian Forint':289.362015, 'Icelandic Krona':111.035992, 'Indonesian Rupiah':13097.056690, 'Iranian Rial':31505.565939, 'Israeli Shekel':3.761411, 'Kazakhstani Tenge':324.291100, 'Kuwaiti Dinar':0.298765, 'Latvian Lat':0.657281, 'Libyan Dinar':1.397966, 'Lithuanian Litas':3.229171,'Mexican Peso':20.548755, 'Nepalese Rupee':106.398617, 'New Zealand Dollar':1.406581, 'Norwegian Krone':8.426143, 'Omani Rial':0.374186, 'Pakistani Rupee':101.910882, 'Philippine Peso':48.405724, 'Polish Zloty':4.103338, 'Qatari Riyal':3.542649, 'Romanian New Leu':4.230461, 'Russian Ruble':59.368387, 'Saudi Arabian Riyal':3.650667, 'South African Rand':13.431637, 'South Korean Won':1174.184755, 'Sri Lankan Rupee':145.956685, 
'Swedish Krona':8.919020, 'Taiwan New Dollar':31.386352, 'Thai Baht':34.967044, 'Trinidadian Dollar':6.519591, 'Turkish Lira':3.496224, 'Venezuelan Bolivar':9.707226}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies7:
        k7=(currencies7[user1])
    l7=user
    m7=k7*(float(l7))
    n=print(round(m7,2))
    print(user1 + "s")
if question is "Malaysian Rinnggit":
    user=input("Enter amount of Malaysian Rinnggits to convert.")
    currencies8 = {'US Dollar':0.222717,'Euro':0.213942, 'Pound':0.181947, 'Rupee':15.207061, 'Australian Dollar':0.308522, 'Canadian Dollar':0.299024, 'Singapore Dollar':0.322989, 'Swiss Franc':0.228773, 'Japanese Yen':26.207078, 'Chinese Yuan Renminbi':1.550245, 'Argentine Peso':3.550010, 'Bahraini Dinar':0.083764, 'Botswana Pula':2.387236, 'Brazilian Real':0.727217, 'Bruneian Dollar':0.322989, 'Bulgarian Lev':0.418353, 'Chilean Peso':149.937650, 'Colombian Peso':663.273998, 'Croatian Kuna':1.618672, 'Czech Koruna':5.781765, 'Danish Krone':1.590734, 'Emirati Dirham':0.817929, 'Hong Kong Dollar':1.727463, 
'Hungarian Forint':66.194431, 'Icelandic Krona':25.411280, 'Indonesian Rupiah':2996.764607, 'Iranian Rial':7210.245356, 'Israeli Shekel':0.860835, 'Kazakhstani Tenge':74.216042, 'Kuwaiti Dinar':0.068371, 'Latvian Lat':0.150359, 'Libyan Dinar':0.319933, 'Lithuanian Litas':0.738700,'Mexican Peso':4.704074, 'Nepalese Rupee':24.349987, 'New Zealand Dollar':0.321850, 'Norwegian Krone':1.927784, 'Omani Rial':0.085635, 'Pakistani Rupee':23.322941, 'Philippine Peso':11.084842, 'Polish Zloty':0.938799, 'Qatari Riyal':0.810757, 'Romanian New Leu':0.967954, 'Russian Ruble':13.582624, 'Saudi Arabian Riyal':0.835568, 'South African Rand':3.077225, 'South Korean Won':268.676592, 'Sri Lankan Rupee':33.403098, 
'Swedish Krona':2.040698, 'Taiwan New Dollar':7.180775, 'Thai Baht':7.995301, 'Trinidadian Dollar':1.492049, 'Turkish Lira':0.800093, 'Venezuelan Bolivar':2.221559}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies8:
        k8=(currencies8[user1])
    l8=user
    m8=k8*(float(l8))
    n=print(round(m8,2))
    print(user1 + "s")
if question is "Japanese Yen":
    user=input("Enter amount of Japanese Yens to convert.")
    currencies9 = {'US Dollar':0.008500,'Euro':0.008163, 'Pound':0.006943, 'Rupee':0.580342, 'Australian Dollar':0.011762, 'Canadian Dollar':0.011409, 'Singapore Dollar':0.012320, 'Swiss Franc':0.008727, 'Malaysian Rinnggit':0.038163, 'Chinese Yuan Renminbi':0.059163, 'Argentine Peso':0.135470, 'Bahraini Dinar':0.003197, 'Botswana Pula':0.091104, 'Brazilian Real':0.027756, 'Bruneian Dollar':0.006943, 'Bulgarian Lev':0.015968, 'Chilean Peso':5.721866, 'Colombian Peso':25.312374, 'Croatian Kuna':0.061749, 'Czech Koruna':0.220544, 'Danish Krone':0.060691, 'Emirati Dirham':0.031214, 'Hong Kong Dollar':0.065927, 
'Hungarian Forint':2.525330, 'Icelandic Krona':0.969765, 'Indonesian Rupiah':114.343902, 'Iranian Rial':275.162942, 'Israeli Shekel':0.032841, 'Kazakhstani Tenge':2.832290, 'Kuwaiti Dinar':0.002600, 'Latvian Lat':0.005737, 'Libyan Dinar':0.012210, 'Lithuanian Litas':0.028186,'Mexican Peso':0.179441, 'Nepalese Rupee':0.929263, 'New Zealand Dollar':0.012287, 'Norwegian Krone':0.073527, 'Omani Rial':0.003268, 'Pakistani Rupee':0.890068, 'Philippine Peso':0.423105, 'Polish Zloty':0.035817, 'Qatari Riyal':0.030941, 'Romanian New Leu':0.036935, 'Russian Ruble':0.518305, 'Saudi Arabian Riyal':0.031885, 'South African Rand':0.117441, 'South Korean Won':10.251957, 'Sri Lankan Rupee':1.274755, 
'Swedish Krona':0.077856, 'Taiwan New Dollar':0.274037, 'Thai Baht':0.305140, 'Trinidadian Dollar':0.056941, 'Turkish Lira':0.030538, 'Venezuelan Bolivar':0.084781}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies9:
        k9=(currencies9[user1])
    l9=user
    m9=k9*(float(l9))
    n=print(round(m9,2))
    print(user1 + "s")
if question is "Chinese Yuan Renminbi":
    user=input("Enter amount of Chinese Yuan Renminbis to convert.")
    currencies10 = {'US Dollar':0.143661,'Euro':0.137894, 'Pound':0.117353, 'Rupee':9.809119, 'Australian Dollar':0.198710, 'Canadian Dollar':0.192787, 'Singapore Dollar':0.208210, 'Swiss Franc':0.147427, 'Malaysian Rinnggit':0.645039, 'Japanese Yen':16.899543, 'Argentine Peso':2.290101, 'Bahraini Dinar':0.054031, 'Botswana Pula':1.539860, 'Brazilian Real':0.468948, 'Bruneian Dollar':0.208210, 'Bulgarian Lev':0.269893, 'Chilean Peso':96.712765, 'Colombian Peso':427.837626, 'Croatian Kuna':1.041790, 'Czech Koruna':3.725886, 'Danish Krone':1.025231, 'Emirati Dirham':0.527596, 'Hong Kong Dollar':1.114302, 
'Hungarian Forint':42.660468, 'Icelandic Krona':16.391268, 'Indonesian Rupiah':1933.265428, 'Iranian Rial':4650.889780, 'Israeli Shekel':0.555053, 'Kazakhstani Tenge':47.872245, 'Kuwaiti Dinar':0.044062, 'Latvian Lat':0.096912, 'Libyan Dinar':0.206369, 'Lithuanian Litas':0.476120,'Mexican Peso':3.033484, 'Nepalese Rupee':15.706693, 'New Zealand Dollar':0.207538, 'Norwegian Krone':1.242086, 'Omani Rial':0.055238, 'Pakistani Rupee':15.044208, 'Philippine Peso':7.151458, 'Polish Zloty':0.604990, 'Qatari Riyal':0.522970, 'Romanian New Leu':0.036935, 'Russian Ruble':0.623792, 'Saudi Arabian Riyal':0.538874, 'South African Rand':1.983725, 'South Korean Won':173.333456, 'Sri Lankan Rupee':21.546302, 
'Swedish Krona':1.315163, 'Taiwan New Dollar':4.631855, 'Thai Baht':5.156067, 'Trinidadian Dollar':0.962487, 'Turkish Lira':0.516095, 'Venezuelan Bolivar':1.432992}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies10:
        k10=(currencies10[user1])
    l10=user
    m10=k10*(float(l10))
    n=print(round(m10,2))
    print(user1 + "s")
if question is "Argentine Peso":
    user=input("Enter amount of Argentine Pesos to convert.")
    currencies11 = {'US Dollar':0.062046,'Euro':0.059202, 'Pound':0.050327, 'Rupee':4.211320, 'Australian Dollar':0.085286, 'Canadian Dollar':0.082455, 'Singapore Dollar':0.089351, 'Swiss Franc':0.063378, 'Malaysian Rinnggit':0.279053, 'Japanese Yen':7.275564, 'Chinese Yuan Renminbi':0.430712, 'Bahraini Dinar':0.023382, 'Botswana Pula':0.662539, 'Brazilian Real':0.199880, 'Bruneian Dollar':0.089351, 'Bulgarian Lev':0.115849, 'Chilean Peso':41.616027, 'Colombian Peso':183.806238, 'Croatian Kuna':0.448426, 'Czech Koruna':1.599880, 'Danish Krone':0.440113, 'Emirati Dirham':0.227902, 'Hong Kong Dollar':0.481162, 
'Hungarian Forint':18.225711, 'Icelandic Krona':7.024834, 'Indonesian Rupiah':828.582175, 'Iranian Rial':2008.561892, 'Israeli Shekel':0.239288, 'Kazakhstani Tenge':20.725580, 'Kuwaiti Dinar':0.019007, 'Latvian Lat':0.041607, 'Libyan Dinar':0.089516, 'Lithuanian Litas':0.204412,'Mexican Peso':1.326625, 'Nepalese Rupee':6.761294, 'New Zealand Dollar':0.089245, 'Norwegian Krone':0.533243, 'Omani Rial':0.023894, 'Pakistani Rupee':6.502752, 'Philippine Peso':3.076887, 'Polish Zloty':0.258604, 'Qatari Riyal':0.225890, 'Romanian New Leu':0.266924, 'Russian Ruble':3.754101, 'Saudi Arabian Riyal':0.232751, 'South African Rand':0.845539, 'South Korean Won':74.362848, 'Sri Lankan Rupee':9.311879, 
'Swedish Krona':0.564988, 'Taiwan New Dollar':1.998218, 'Thai Baht':2.222874, 'Trinidadian Dollar':0.418554, 'Turkish Lira':0.221829, 'Venezuelan Bolivar':0.617344}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies11:
        k11=(currencies11[user1])
    l11=user
    m11=k11*(float(l11))
    n=print(round(m11,2))
    print(user1 + "s")
if question is "Bahraini Dinar":
    user=input("Enter amount of Bahraini Dinars to convert.")
    currencies12 = {'US Dollar':2.653577,'Euro':2.533523, 'Pound':2.154014, 'Rupee':180.116643, 'Australian Dollar':3.649014, 'Canadian Dollar':3.527731, 'Singapore Dollar':3.822857, 'Swiss Franc':2.713025, 'Malaysian Rinnggit':11.934460, 'Japanese Yen':311.361999, 'Chinese Yuan Renminbi':18.420600, 'Argentine Peso':42.726963, 'Botswana Pula':28.335346, 'Brazilian Real':8.550423, 'Bruneian Dollar':3.822857, 'Bulgarian Lev':4.954889, 'Chilean Peso':1779.709726, 'Colombian Peso':7862.096034, 'Croatian Kuna':19.190855, 'Czech Koruna':68.455374, 'Danish Krone':18.835305, 'Emirati Dirham':9.746853, 'Hong Kong Dollar':20.578644, 
'Hungarian Forint':780.021754, 'Icelandic Krona':300.437352, 'Indonesian Rupiah':35439.532657, 'Iranian Rial':85904.074458, 'Israeli Shekel':10.231944, 'Kazakhstani Tenge':886.387032, 'Kuwaiti Dinar':0.813025, 'Latvian Lat':1.780560, 'Libyan Dinar':3.828393, 'Lithuanian Litas':8.747748,'Mexican Peso':56.725339, 'Nepalese Rupee':289.165554, 'New Zealand Dollar':3.818086, 'Norwegian Krone':22.821749, 'Omani Rial':1.021891, 'Pakistani Rupee':278.108276, 'Philippine Peso':131.499648, 'Polish Zloty':11.067588, 'Qatari Riyal':9.660078, 'Romanian New Leu':11.425114, 'Russian Ruble':160.170760, 'Saudi Arabian Riyal':9.954163, 'South African Rand':36.159594, 'South Korean Won':3180.339469, 'Sri Lankan Rupee':398.248397, 
'Swedish Krona':24.172583, 'Taiwan New Dollar':85.466739, 'Thai Baht':95.089612, 'Trinidadian Dollar':17.900607, 'Turkish Lira':9.489030, 'Venezuelan Bolivar':26.402423}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies12:
        k12=(currencies12[user1])
    l12=user
    m12=k12*(float(l12))
    n=print(round(m12,2))
    print(user1 + "s")
if question is "Botswana Pula":
    user=input("Enter amount of Botswana Pulas to convert.")
    currencies13 = {'US Dollar':0.093649,'Euro':0.089340, 'Pound':0.075993, 'Rupee':6.357354, 'Australian Dollar':0.128655, 'Canadian Dollar':0.124621, 'Singapore Dollar':0.134825, 'Swiss Franc':0.095661, 'Malaysian Rinnggit':0.421186, 'Japanese Yen':10.995923, 'Chinese Yuan Renminbi':0.649469, 'Argentine Peso':1.505670, 'Bahraini Dinar':0.035268, 'Brazilian Real':0.301182, 'Bruneian Dollar':0.134825, 'Bulgarian Lev':0.174747, 'Chilean Peso':62.866586, 'Colombian Peso':278.043940, 'Croatian Kuna':0.676613, 'Czech Koruna':2.414286, 'Danish Krone':0.664167, 'Emirati Dirham':0.343926, 'Hong Kong Dollar':0.726290, 
'Hungarian Forint':27.518510, 'Icelandic Krona':10.597293, 'Indonesian Rupiah':1251.321313, 'Iranian Rial':3031.793373, 'Israeli Shekel':0.361315, 'Kazakhstani Tenge':31.269407, 'Kuwaiti Dinar':0.028722, 'Latvian Lat':0.062788, 'Libyan Dinar':0.134948, 'Lithuanian Litas':0.308473,'Mexican Peso':2.016038, 'Nepalese Rupee':10.205120, 'New Zealand Dollar':0.134558, 'Norwegian Krone':0.805490, 'Omani Rial':0.036008, 'Pakistani Rupee':9.807862, 'Philippine Peso':4.640740, 'Polish Zloty':0.390352, 'Qatari Riyal':0.340892, 'Romanian New Leu':0.403064, 'Russian Ruble':5.660186, 'Saudi Arabian Riyal':0.351247, 'South African Rand':1.277628, 'South Korean Won':112.039068, 'Sri Lankan Rupee':14.054830, 
'Swedish Krona':0.853048, 'Taiwan New Dollar':3.008104, 'Thai Baht':3.353619, 'Trinidadian Dollar':0.628319, 'Turkish Lira':0.334574, 'Venezuelan Bolivar':0.934130}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies13:
        k13=(currencies13[user1])
    l13=user
    m13=k13*(float(l13))
    n=print(round(m13,2))
    print(user1 + "s")
if question is "Brazilian Real":
    user=input("Enter amount of Brazilian Reals to convert.")
    currencies14 = {'US Dollar':0.310936,'Euro':0.296422, 'Pound':0.252326, 'Rupee':21.107770, 'Australian Dollar':0.427000, 'Canadian Dollar':0.413655, 'Singapore Dollar':0.447478, 'Swiss Franc':0.317408, 'Malaysian Rinnggit':1.398433, 'Japanese Yen':36.466225, 'Chinese Yuan Renminbi':2.156370, 'Argentine Peso':4.999998, 'Bahraini Dinar':0.1170988, 'Botswana Pula':3.320223, 'Bruneian Dollar':0.447478, 'Bulgarian Lev':0.580604, 'Chilean Peso':208.731068, 'Colombian Peso':923.167575, 'Croatian Kuna':2.244836, 'Czech Koruna':8.010821, 'Danish Krone':2.203609, 'Emirati Dirham':1.141911, 'Hong Kong Dollar':2.411494, 
'Hungarian Forint':91.288163, 'Icelandic Krona':35.185373, 'Indonesian Rupiah':4153.978548, 'Iranian Rial':10066.229304, 'Israeli Shekel':1.199378, 'Kazakhstani Tenge':103.821397, 'Kuwaiti Dinar':0.095364, 'Latvian Lat':0.208326, 'Libyan Dinar':0.448058, 'Lithuanian Litas':1.023487,'Mexican Peso':6.688780, 'Nepalese Rupee':33.883272, 'New Zealand Dollar':0.446431, 'Norwegian Krone':2.673447, 'Omani Rial':0.119555, 'Pakistani Rupee':32.564287, 'Philippine Peso':15.409968, 'Polish Zloty':1.294672, 'Qatari Riyal':1.131837, 'Romanian New Leu':1.337356, 'Russian Ruble':18.798847, 'Saudi Arabian Riyal':1.166553, 'South African Rand':4.233931, 'South Korean Won':371.866177, 'Sri Lankan Rupee':46.665167, 
'Swedish Krona':2.830699, 'Taiwan New Dollar':9.990487, 'Thai Baht':11.132616, 'Trinidadian Dollar':2.086160, 'Turkish Lira':1.110795, 'Venezuelan Bolivar':3.101521}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies14:
        k14=(currencies14[user1])
    l14=user
    m14=k14*(float(l14))
    n=print(round(m14,2))
    print(user1 + "s")
if question is "Bruneian Dollar":
    user=input("Enter amount of Bruneian Dollars to convert.")
    currencies15 = {'US Dollar':0.694417,'Euro':0.662462, 'Pound':0.563823, 'Rupee':47.137084, 'Australian Dollar':0.954227, 'Canadian Dollar':0.924421, 'Singapore Dollar':1.000000, 'Swiss Franc':0.709346, 'Malaysian Rinnggit':3.123138, 'Japanese Yen':81.500696, 'Chinese Yuan Renminbi':4.820463, 'Argentine Peso':11.162940, 'Bahraini Dinar':0.261689, 'Botswana Pula':7.415096, 'Brazilian Real':2.233383, 'Bulgarian Lev':1.296217, 'Chilean Peso':466.208871, 'Colombian Peso':2062.182395, 'Croatian Kuna':5.018996, 'Czech Koruna':17.896399, 'Danish Krone':4.924802, 'Emirati Dirham':2.550657, 'Hong Kong Dollar':5.385793, 
'Hungarian Forint':203.980358, 'Icelandic Krona':78.551909, 'Indonesian Rupiah':9273.973611, 'Iranian Rial':22480.307368, 'Israeli Shekel':2.678558, 'Kazakhstani Tenge':231.958536, 'Kuwaiti Dinar':0.212480, 'Latvian Lat':0.465578, 'Libyan Dinar':1.001845, 'Lithuanian Litas':2.287349,'Mexican Peso':14.946990, 'Nepalese Rupee':75.671950, 'New Zealand Dollar':0.997669, 'Norwegian Krone':5.974570, 'Omani Rial':0.267416, 'Pakistani Rupee':72.777946, 'Philippine Peso':34.411700, 'Polish Zloty':2.892447, 'Qatari Riyal':2.527331, 'Romanian New Leu':2.989131, 'Russian Ruble':41.997598, 'Saudi Arabian Riyal':2.604949, 'South African Rand':9.465600, 'South Korean Won':830.304370, 'Sri Lankan Rupee':104.217921, 
'Swedish Krona':6.326381, 'Taiwan New Dollar':22.337618, 'Thai Baht':24.873862, 'Trinidadian Dollar':4.684171, 'Turkish Lira':2.480859, 'Venezuelan Bolivar':6.909409}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies15:
        k15=(currencies15[user1])
    l15=user
    m15=k15*(float(l15))
    n=print(round(m15,2))
    print(user1 + "s")
if question is "Bulgarian Lev":
    user=input("Enter amount of Bulgarian Levs to convert.")
    currencies16 = {'US Dollar':0.535960,'Euro':0.511011, 'Pound':0.435058, 'Rupee':36.366382, 'Australian Dollar':0.735823, 'Canadian Dollar':0.713346, 'Singapore Dollar':0.771553, 'Swiss Franc':0.547319, 'Malaysian Rinnggit':2.410481, 'Japanese Yen':62.857746, 'Chinese Yuan Renminbi':3.720529, 'Argentine Peso':8.616244, 'Bahraini Dinar':0.201977, 'Botswana Pula':5.723075, 'Brazilian Real':1.723850, 'Bruneian Dollar':0.771553, 'Chilean Peso':359.830500, 'Colombian Peso':1591.393512, 'Croatian Kuna':3.870158, 'Czech Koruna':13.805558, 'Danish Krone':3.798859, 'Emirati Dirham':1.968635, 'Hong Kong Dollar':4.156809, 
'Hungarian Forint':157.373350, 'Icelandic Krona':60.627694, 'Indonesian Rupiah':7159.627876, 'Iranian Rial':17300.883508, 'Israeli Shekel':2.067303, 'Kazakhstani Tenge':179.038975, 'Kuwaiti Dinar':0.163984, 'Latvian Lat':0.359138, 'Libyan Dinar':0.773246, 'Lithuanian Litas':1.764417,'Mexican Peso':11.530968, 'Nepalese Rupee':58.405530, 'New Zealand Dollar':0.769438, 'Norwegian Krone':4.608772, 'Omani Rial':0.206398, 'Pakistani Rupee':56.171321, 'Philippine Peso':26.562237, 'Polish Zloty':2.230956, 'Qatari Riyal':1.950734, 'Romanian New Leu':2.305396, 'Russian Ruble':32.394657, 'Saudi Arabian Riyal':2.010347, 'South African Rand':7.305742, 'South Korean Won':640.896551, 'Sri Lankan Rupee':80.438001, 
'Swedish Krona':4.880845, 'Taiwan New Dollar':17.246246, 'Thai Baht':19.194515, 'Trinidadian Dollar':3.615503, 'Turkish Lira':1.913889, 'Venezuelan Bolivar':5.332671}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies16:
        k16=(currencies16[user1])
    l16=user
    m16=k16*(float(l16))
    n=print(round(m16,2))
    print(user1 + "s")
if question is "Chilean Peso":
    user=input("Enter amount of Chilean Pesos to convert.")
    currencies17 = {'US Dollar':0.001510,'Euro':0.001425, 'Pound':0.001216, 'Rupee':0.102321, 'Australian Dollar':0.002058, 'Canadian Dollar':0.001996, 'Singapore Dollar':0.002158, 'Swiss Franc':0.001526, 'Malaysian Rinnggit':0.006774, 'Japanese Yen':0.174435, 'Chinese Yuan Renminbi':0.010405, 'Argentine Peso':0.024109, 'Bahraini Dinar':0.000569, 'Botswana Pula':0.016086, 'Brazilian Real':0.004837, 'Bruneian Dollar':0.002158, 'Bulgarian Lev':0.002784, 'Colombian Peso':4.426630, 'Croatian Kuna':0.010787, 'Czech Koruna':0.038489, 'Danish Krone':0.010593, 'Emirati Dirham':0.005547, 'Hong Kong Dollar':0.011713, 
'Hungarian Forint':0.438829, 'Icelandic Krona':0.170305, 'Indonesian Rupiah':20.120833, 'Iranian Rial':48.896969, 'Israeli Shekel':0.005810, 'Kazakhstani Tenge':0.502701, 'Kuwaiti Dinar':0.000461, 'Latvian Lat':0.001001, 'Libyan Dinar':0.002162, 'Lithuanian Litas':0.004920,'Mexican Peso':0.032379, 'Nepalese Rupee':0.164275, 'New Zealand Dollar':0.002150, 'Norwegian Krone':0.012826, 'Omani Rial':0.000581, 'Pakistani Rupee':0.158152, 'Philippine Peso':0.074496, 'Polish Zloty':0.006217, 'Qatari Riyal':0.005499, 'Romanian New Leu':0.006424, 'Russian Ruble':0.089953, 'Saudi Arabian Riyal':0.005668, 'South African Rand':0.020574, 'South Korean Won':1.788762, 'Sri Lankan Rupee':0.224260, 
'Swedish Krona':0.013587, 'Taiwan New Dollar':0.048018, 'Thai Baht':0.053890, 'Trinidadian Dollar':0.010136, 'Turkish Lira':0.005428, 'Venezuelan Bolivar':0.015067}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies17:
        k17=(currencies17[user1])
    l17=user
    m17=k17*(float(l17))
    n=print(round(m17,2))
    print(user1 + "s")
if question is "Colombian Peso":
    user=input("Enter amount of Colombian Pesos to convert.")
    currencies18 = {'US Dollar':0.000341,'Euro':0.000322, 'Pound':0.000275, 'Rupee':0.023116, 'Australian Dollar':0.000465, 'Canadian Dollar':0.000451, 'Singapore Dollar':0.000488, 'Swiss Franc':0.000345, 'Malaysian Rinnggit':0.001531, 'Japanese Yen':0.039436, 'Chinese Yuan Renminbi':0.002351, 'Argentine Peso':0.005446, 'Bahraini Dinar':0.000129, 'Botswana Pula':0.003634, 'Brazilian Real':0.001092, 'Bruneian Dollar':0.000488, 'Bulgarian Lev':0.000629, 'Chilean Peso':0.225945, 'Croatian Kuna':0.002440, 'Czech Koruna':0.008703, 'Danish Krone':0.002394, 'Emirati Dirham':0.001253, 'Hong Kong Dollar':0.002646, 
'Hungarian Forint':0.099180, 'Icelandic Krona':0.038477, 'Indonesian Rupiah':4.546401, 'Iranian Rial':11.046841, 'Israeli Shekel':0.001313, 'Kazakhstani Tenge':0.113574, 'Kuwaiti Dinar':0.000104, 'Latvian Lat':0.000226, 'Libyan Dinar':0.000488, 'Lithuanian Litas':0.001112,'Mexican Peso':0.007310, 'Nepalese Rupee':0.037114, 'New Zealand Dollar':0.000486, 'Norwegian Krone':0.002899, 'Omani Rial':0.000131, 'Pakistani Rupee':0.035730, 'Philippine Peso':0.016831, 'Polish Zloty':0.001405, 'Qatari Riyal':0.001242, 'Romanian New Leu':0.001452, 'Russian Ruble':0.020334, 'Saudi Arabian Riyal':0.001280, 'South African Rand':0.004647, 'South Korean Won':0.404327, 'Sri Lankan Rupee':0.050666, 
'Swedish Krona':0.003071, 'Taiwan New Dollar':0.010849, 'Thai Baht':0.012177, 'Trinidadian Dollar':0.002290, 'Turkish Lira':0.001226, 'Venezuelan Bolivar':0.003404}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies18:
        k18=(currencies18[user1])
    l18=user
    m18=k18*(float(l18))
    n=print(round(m18,2))
    print(user1 + "s")
if question is "Croatian Kuna":
    user=input("Enter amount of Croatian Kunas to convert.")
    currencies19 = {'US Dollar':0.139774,'Euro':0.131925, 'Pound':0.112641, 'Rupee':9.468872, 'Australian Dollar':0.190624, 'Canadian Dollar':0.185033, 'Singapore Dollar':0.199880, 'Swiss Franc':0.141264, 'Malaysian Rinnggit':0.625979, 'Japanese Yen':16.154337, 'Chinese Yuan Renminbi':0.962388, 'Argentine Peso':2.230509, 'Bahraini Dinar':0.052702, 'Botswana Pula':1.474224, 'Brazilian Real':0.447138, 'Bruneian Dollar':0.199880, 'Bulgarian Lev':0.257805, 'Chilean Peso':92.443357, 'Colombian Peso':409.664837, 'Czech Koruna':3.564735, 'Danish Krone':0.980789, 'Emirati Dirham':0.513391, 'Hong Kong Dollar':1.083834, 
'Hungarian Forint':40.645874, 'Icelandic Krona':15.751098, 'Indonesian Rupiah':1862.633059, 'Iranian Rial':4524.906291, 'Israeli Shekel':0.538172, 'Kazakhstani Tenge':46.535764, 'Kuwaiti Dinar':0.042755, 'Latvian Lat':0.092717, 'Libyan Dinar':0.201657, 'Lithuanian Litas':0.455509,'Mexican Peso':2.991299, 'Nepalese Rupee':15.201506, 'New Zealand Dollar':0.199413, 'Norwegian Krone':1.186573, 'Omani Rial':0.053813, 'Pakistani Rupee':14.644860, 'Philippine Peso':6.889448, 'Polish Zloty':0.575808, 'Qatari Riyal':0.508779, 'Romanian New Leu':0.594785, 'Russian Ruble':8.296777, 'Saudi Arabian Riyal':0.524287, 'South African Rand':1.900560, 'South Korean Won':165.786875, 'Sri Lankan Rupee':20.700687, 
'Swedish Krona':1.258932, 'Taiwan New Dollar':4.457785, 'Thai Baht':4.988403, 'Trinidadian Dollar':0.942460, 'Turkish Lira':0.502313, 'Venezuelan Bolivar':0.502313}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies19:
        k19=(currencies19[user1])
    l19=user
    m19=k19*(float(l19))
    n=print(round(m19,2))
    print(user1 + "s")
if question is "Czech Koruna":
    user=input("Enter amount of Czech Korunas to convert.")
    currencies20 = {'US Dollar':0.039035,'Euro':0.037015, 'Pound':0.031753, 'Rupee':2.660333, 'Australian Dollar':0.053468, 'Canadian Dollar':0.051670, 'Singapore Dollar':0.056077, 'Swiss Franc':0.039659, 'Malaysian Rinnggit':0.174583, 'Japanese Yen':4.555000, 'Chinese Yuan Renminbi':0.270149, 'Argentine Peso':0.617132, 'Bahraini Dinar':0.014716, 'Botswana Pula':0.414729, 'Brazilian Real':0.125713, 'Bruneian Dollar':0.056077, 'Bulgarian Lev':0.072326, 'Chilean Peso':26.048497, 'Colombian Peso':114.115876, 'Croatian Kuna':0.280567, 'Danish Krone':0.275177, 'Emirati Dirham':0.143378, 'Hong Kong Dollar':0.302707, 
'Hungarian Forint':11.375360, 'Icelandic Krona':4.430819, 'Indonesian Rupiah':521.346345, 'Iranian Rial':1262.443122, 'Israeli Shekel':0.150069, 'Kazakhstani Tenge':12.933539, 'Kuwaiti Dinar':0.011937, 'Latvian Lat':0.026014, 'Libyan Dinar':0.055429, 'Lithuanian Litas':0.127805,'Mexican Peso':0.830215, 'Nepalese Rupee':4.245416, 'New Zealand Dollar':0.055998, 'Norwegian Krone':0.332895, 'Omani Rial':0.015028, 'Pakistani Rupee':4.089469, 'Philippine Peso':1.930247, 'Polish Zloty':0.161134, 'Qatari Riyal':0.142112, 'Romanian New Leu':0.166750, 'Russian Ruble':2.321197, 'Saudi Arabian Riyal':0.146405, 'South African Rand':0.535654, 'South Korean Won':46.743811, 'Sri Lankan Rupee':5.790014, 
'Swedish Krona':0.353525, 'Taiwan New Dollar':1.250502, 'Thai Baht':1.394408, 'Trinidadian Dollar':0.263383, 'Turkish Lira':0.141851, 'Venezuelan Bolivar':0.390154}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies20:
        k20=(currencies20[user1])
    l20=user
    m20=k20*(float(l20))
    n=print(round(m20,2))
    print(user1 + "s")
if question is "Danish Krone":
    user=input("Enter amount of Danish Krones to convert.")
    currencies21 = {'US Dollar':0.141806,'Euro':0.134521, 'Pound':0.115437, 'Rupee':9.665607, 'Australian Dollar':0.194235, 'Canadian Dollar':0.187730, 'Singapore Dollar':0.203893, 'Swiss Franc':0.144122, 'Malaysian Rinnggit':0.634225, 'Japanese Yen':16.584687, 'Chinese Yuan Renminbi':0.981401, 'Argentine Peso':2.241767, 'Bahraini Dinar':0.053461, 'Botswana Pula':1.506636, 'Brazilian Real':0.456875, 'Bruneian Dollar':0.203893, 'Bulgarian Lev':0.262751, 'Chilean Peso':94.629216, 'Colombian Peso':414.587195, 'Croatian Kuna':1.019577, 'Czech Koruna':3.6350527, 'Emirati Dirham':0.520851, 'Hong Kong Dollar':1.099658, 
'Hungarian Forint':41.348221, 'Icelandic Krona':16.096302, 'Indonesian Rupiah':1893.535824, 'Iranian Rial':4590.661048, 'Israeli Shekel':0.545360, 'Kazakhstani Tenge':46.985030, 'Kuwaiti Dinar':0.043364, 'Latvian Lat':0.094541, 'Libyan Dinar':0.199946, 'Lithuanian Litas':0.464473,'Mexican Peso':3.016282, 'Nepalese Rupee':15.422746, 'New Zealand Dollar':0.203536, 'Norwegian Krone':1.210155, 'Omani Rial':0.054595, 'Pakistani Rupee':14.856513, 'Philippine Peso':7.022749, 'Polish Zloty':0.586407, 'Qatari Riyal':0.516229, 'Romanian New Leu':0.605938, 'Russian Ruble':8.442317, 'Saudi Arabian Riyal':0.531863, 'South African Rand':1.944887, 'South Korean Won':170.110123, 'Sri Lankan Rupee':21.033996, 
'Swedish Krona':1.284799, 'Taiwan New Dollar':4.544167, 'Thai Baht':5.065746, 'Trinidadian Dollar':0.956757, 'Turkish Lira':0.515674, 'Venezuelan Bolivar':1.417353}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies21:
        k21=(currencies21[user1])
    l21=user
    m21=k21*(float(l21))
    n=print(round(m21,2))
    print(user1 + "s")
if question is "Emirati Dirham":
    user=input("Enter amount of Emirati Dirhams to convert.")
    currencies22 = {'US Dollar':0.272261,'Euro':0.258484, 'Pound':0.221584, 'Rupee':18.559196, 'Australian Dollar':0.373216, 'Canadian Dollar':0.360351, 'Singapore Dollar':0.391806, 'Swiss Franc':0.277080, 'Malaysian Rinnggit':1.217822, 'Japanese Yen':31.840891, 'Chinese Yuan Renminbi':1.883636, 'Argentine Peso':4.298997, 'Bahraini Dinar':0.102642, 'Botswana Pula':2.892679, 'Brazilian Real':0.877687, 'Bruneian Dollar':0.391806, 'Bulgarian Lev':0.505615, 'Chilean Peso':181.597898, 'Colombian Peso':796.907118, 'Croatian Kuna':1.958635, 'Czech Koruna':6.983732, 'Danish Krone':1.921234, 'Hong Kong Dollar':2.111559, 
'Hungarian Forint':79.522999, 'Icelandic Krona':30.956044, 'Indonesian Rupiah':3632.488871, 'Iranian Rial':8826.692441, 'Israeli Shekel':1.047134, 'Kazakhstani Tenge':90.175470, 'Kuwaiti Dinar':0.083244, 'Latvian Lat':0.181663, 'Libyan Dinar':0.390694, 'Lithuanian Litas':0.892495, 'Mexican Peso':5.778741, 'Nepalese Rupee':29.611033, 'New Zealand Dollar':0.391011, 'Norwegian Krone':2.324263, 'Omani Rial':0.104684, 'Pakistani Rupee':28.532923, 'Philippine Peso':13.480989, 'Polish Zloty':1.126634, 'Qatari Riyal':0.991233, 'Romanian New Leu':1.165140, 'Russian Ruble':16.187261, 'Saudi Arabian Riyal':1.021127, 'South African Rand':3.748721, 'South Korean Won':327.205652, 'Sri Lankan Rupee':40.384399, 
'Swedish Krona':2.465198, 'Taiwan New Dollar':8.729223, 'Thai Baht':9.729237, 'Trinidadian Dollar':1.830137, 'Turkish Lira':0.992137, 'Venezuelan Bolivar':2.718523}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies22:
        k22=(currencies22[user1])
    l22=user
    m22=k22*(float(l22))
    n=print(round(m22,2))
    print(user1 + "s")
if question is "Hong Kong Dollar":
    user=input("Enter amount of Hong Kong Dollars to convert.")
    currencies23 = {'US Dollar':0.128938,'Euro':0.122414, 'Pound':0.104939, 'Rupee':8.789334, 'Australian Dollar':0.176749, 'Canadian Dollar':0.170656, 'Singapore Dollar':0.185553, 'Swiss Franc':0.131220, 'Malaysian Rinnggit':0.576741, 'Japanese Yen':15.079329, 'Chinese Yuan Renminbi':0.892059, 'Argentine Peso':2.035935, 'Bahraini Dinar':0.048610, 'Botswana Pula':1.369926, 'Brazilian Real':0.415658, 'Bruneian Dollar':0.185553, 'Bulgarian Lev':0.239451, 'Chilean Peso':86.001818, 'Colombian Peso':377.402281, 'Croatian Kuna':0.927578, 'Czech Koruna':3.307382, 'Danish Krone':0.909865, 'Emirati Dirham':0.473584, 
'Hungarian Forint':37.660802, 'Icelandic Krona':14.660280, 'Indonesian Rupiah':1720.287790, 'Iranian Rial':4180.178322, 'Israeli Shekel':0.495906, 'Kazakhstani Tenge':42.705639, 'Kuwaiti Dinar':0.039423, 'Latvian Lat':0.086033, 'Libyan Dinar':0.185026, 'Lithuanian Litas':0.422671, 'Mexican Peso':2.736718, 'Nepalese Rupee':14.023305, 'New Zealand Dollar':0.185176, 'Norwegian Krone':1.100733, 'Omani Rial':0.049577, 'Pakistani Rupee':13.512729, 'Philippine Peso':6.384378, 'Polish Zloty':0.533556, 'Qatari Riyal':0.469432, 'Romanian New Leu':0.551791, 'Russian Ruble':7.666024, 'Saudi Arabian Riyal':0.483589, 'South African Rand':1.775333, 'South Korean Won':154.959288, 'Sri Lankan Rupee':19.125396, 
'Swedish Krona':1.167478, 'Taiwan New Dollar':4.134018, 'Thai Baht':4.607609, 'Trinidadian Dollar':0.866723, 'Turkish Lira':0.469860, 'Venezuelan Bolivar':1.287449}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies23:
        k23=(currencies23[user1])
    l23=user
    m23=k23*(float(l23))
    n=print(round(m23,2))
    print(user1 + "s")
if question is "Hungarian Forint":
    user=input("Enter amount of Hungarian Forints to convert.")
    currencies24 = {'US Dollar':0.003424,'Euro':0.003250, 'Pound':0.002786, 'Rupee':0.233381, 'Australian Dollar':0.004693, 'Canadian Dollar':0.004531, 'Singapore Dollar':0.004927, 'Swiss Franc':0.003484, 'Malaysian Rinnggit':0.015314, 'Japanese Yen':0.400399, 'Chinese Yuan Renminbi':0.023687, 'Argentine Peso':0.054060, 'Bahraini Dinar':0.001291, 'Botswana Pula':0.036375, 'Brazilian Real':0.011037, 'Bruneian Dollar':0.004927, 'Bulgarian Lev':0.006358, 'Chilean Peso':2.283590, 'Colombian Peso':10.021090, 'Croatian Kuna':0.024630, 'Czech Koruna':0.087820, 'Danish Krone':0.024159, 'Emirati Dirham':0.012575, 
'Hong Kong Dollar':0.026553, 'Icelandic Krona':0.389272, 'Indonesian Rupiah':45.678469, 'Iranian Rial':110.995467, 'Israeli Shekel':0.013168, 'Kazakhstani Tenge':1.133955, 'Kuwaiti Dinar':0.001047, 'Latvian Lat':0.002284, 'Libyan Dinar':0.004913, 'Lithuanian Litas':0.011223, 'Mexican Peso':0.072668, 'Nepalese Rupee':0.372358, 'New Zealand Dollar':0.004917, 'Norwegian Krone':0.029228, 'Omani Rial':0.001316, 'Pakistani Rupee':0.358801, 'Philippine Peso':0.169523, 'Polish Zloty':0.014167, 'Qatari Riyal':0.012465, 'Romanian New Leu':0.014652, 'Russian Ruble':0.203554, 'Saudi Arabian Riyal':0.012841, 'South African Rand':0.047140, 'South Korean Won':4.114604, 'Sri Lankan Rupee':0.507833, 
'Swedish Krona':0.031000, 'Taiwan New Dollar':0.109770, 'Thai Baht':0.122345, 'Trinidadian Dollar':0.023014, 'Turkish Lira':0.012476, 'Venezuelan Bolivar':0.034185}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies24:
        k24=(currencies24[user1])
    l24=user
    m24=k24*(float(l24))
    n=print(round(m24,2))
    print(user1 + "s")
if question is "Icelandic Krona":
    user=input("Enter amount of Icelandic Kronas to convert.")
    currencies25 = {'US Dollar':0.008795,'Euro':0.008350, 'Pound':0.007158, 'Rupee':0.599534, 'Australian Dollar':0.012056, 'Canadian Dollar':0.011641, 'Singapore Dollar':0.012657, 'Swiss Franc':0.008951, 'Malaysian Rinnggit':0.039340, 'Japanese Yen':1.028584, 'Chinese Yuan Renminbi':0.060849, 'Argentine Peso':0.138874, 'Bahraini Dinar':0.003316, 'Botswana Pula':0.093445, 'Brazilian Real':0.028353, 'Bruneian Dollar':0.012657, 'Bulgarian Lev':0.016333, 'Chilean Peso':5.866315, 'Colombian Peso':25.743184, 'Croatian Kuna':0.063271, 'Czech Koruna':0.225602, 'Danish Krone':0.062063, 'Emirati Dirham':0.032304, 
'Hong Kong Dollar':0.068212, 'Hungarian Forint':2.568901, 'Indonesian Rupiah':117.343448, 'Iranian Rial':285.136324, 'Israeli Shekel':0.033826, 'Kazakhstani Tenge':2.913017, 'Kuwaiti Dinar':0.002689, 'Latvian Lat':0.005868, 'Libyan Dinar':0.012621, 'Lithuanian Litas':0.028831, 'Mexican Peso':0.186676, 'Nepalese Rupee':0.956551, 'New Zealand Dollar':0.012631, 'Norwegian Krone':0.075083, 'Omani Rial':0.003382, 'Pakistani Rupee':0.921724, 'Philippine Peso':0.435488, 'Polish Zloty':0.036395, 'Qatari Riyal':0.032021, 'Romanian New Leu':0.037639, 'Russian Ruble':0.522911, 'Saudi Arabian Riyal':0.032986, 'South African Rand':0.121098, 'South Korean Won':10.570009, 'Sri Lankan Rupee':1.304572, 
'Swedish Krona':0.079635, 'Taiwan New Dollar':0.281988, 'Thai Baht':0.314292, 'Trinidadian Dollar':0.059120, 'Turkish Lira':0.032050, 'Venezuelan Bolivar':0.087819}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies25:
        k25=(currencies25[user1])
    l25=user
    m25=k25*(float(l25))
    n=print(round(m25,2))
    print(user1 + "s")
if question is "Indonesian Rupiah":
    user=input("Enter amount of Indonesian Rupiahs to convert.")
    currencies26 = {'US Dollar':0.000075,'Euro':0.000071, 'Pound':0.000061, 'Rupee':0.005109, 'Australian Dollar':0.000103, 'Canadian Dollar':0.000099, 'Singapore Dollar':0.000108, 'Swiss Franc':0.000076, 'Malaysian Rinnggit':0.000335, 'Japanese Yen':0.008766, 'Chinese Yuan Renminbi':0.000519, 'Argentine Peso':0.001183, 'Bahraini Dinar':0.000028, 'Botswana Pula':0.000796, 'Brazilian Real':0.000242, 'Bruneian Dollar':0.000108, 'Bulgarian Lev':0.000139, 'Chilean Peso':0.049993, 'Colombian Peso':0.219383, 'Croatian Kuna':0.000539, 'Czech Koruna':0.001923, 'Danish Krone':0.000529, 'Emirati Dirham':0.000275, 
'Hong Kong Dollar':0.000581, 'Hungarian Forint':0.021892, 'Icelandic Krona':0.008522, 'Iranian Rial':2.429930, 'Israeli Shekel':0.000288, 'Kazakhstani Tenge':0.024825, 'Kuwaiti Dinar':0.000023, 'Latvian Lat':0.000050, 'Libyan Dinar':0.000108, 'Lithuanian Litas':0.000246, 'Mexican Peso':0.001591, 'Nepalese Rupee':0.008152, 'New Zealand Dollar':0.000108, 'Norwegian Krone':0.000640, 'Omani Rial':0.000029, 'Pakistani Rupee':0.007855, 'Philippine Peso':0.003711, 'Polish Zloty':0.000310, 'Qatari Riyal':0.000273, 'Romanian New Leu':0.000321, 'Russian Ruble':0.004456, 'Saudi Arabian Riyal':0.000281, 'South African Rand':0.001032, 'South Korean Won':0.090078, 'Sri Lankan Rupee':0.011118, 
'Swedish Krona':0.000679, 'Taiwan New Dollar':0.002403, 'Thai Baht':0.002678, 'Trinidadian Dollar':0.000504, 'Turkish Lira':0.000273, 'Venezuelan Bolivar':0.000748}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies26:
        k26=(currencies26[user1])
    l26=user
    m26=k26*(float(l26))
    n=print(round(m26,2))
    print(user1 + "s")
if question is "Iranian Rial":
    user=input("Enter amount of Iranian Rials to convert.")
    currencies27 = {'US Dollar':0.000031,'Euro':0.000029, 'Pound':0.000025, 'Rupee':0.002103, 'Australian Dollar':0.000042, 'Canadian Dollar':0.000041, 'Singapore Dollar':0.000044, 'Swiss Franc':0.000031, 'Malaysian Rinnggit':0.000138, 'Japanese Yen':0.003607, 'Chinese Yuan Renminbi':0.000213, 'Argentine Peso':0.000487, 'Bahraini Dinar':0.000012, 'Botswana Pula':0.000328, 'Brazilian Real':0.000099, 'Bruneian Dollar':0.000044, 'Bulgarian Lev':0.000057, 'Chilean Peso':0.020574, 'Colombian Peso':0.090284, 'Croatian Kuna':0.000222, 'Czech Koruna':0.000791, 'Danish Krone':0.000218, 'Emirati Dirham':0.000113, 
'Hong Kong Dollar':0.000239, 'Hungarian Forint':0.009009, 'Icelandic Krona':0.003502, 'Indonesian Rupiah':0.411535, 'Israeli Shekel':0.000119, 'Kazakhstani Tenge':0.010216, 'Kuwaiti Dinar':0.000009, 'Latvian Lat':0.000021, 'Libyan Dinar':0.000044, 'Lithuanian Litas':0.000101, 'Mexican Peso':0.000655, 'Nepalese Rupee':0.003355, 'New Zealand Dollar':0.000044, 'Norwegian Krone':0.000263, 'Omani Rial':0.000012, 'Pakistani Rupee':0.003233, 'Philippine Peso':0.001527, 'Polish Zloty':0.000128, 'Qatari Riyal':0.000112, 'Romanian New Leu':0.000132, 'Russian Ruble':0.001834, 'Saudi Arabian Riyal':0.000116, 'South African Rand':0.000425, 'South Korean Won':0.037070, 'Sri Lankan Rupee':0.004575, 
'Swedish Krona':0.000279, 'Taiwan New Dollar':0.000989, 'Thai Baht':0.001102, 'Trinidadian Dollar':0.000207, 'Turkish Lira':0.000112, 'Venezuelan Bolivar':0.000308}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies27:
        k27=(currencies27[user1])
    l27=user
    m27=k27*(float(l27))
    n=print(round(m27,2))
    print(user1 + "s")
if question is "Israeli Shekel":
    user=input("Enter amount of Israeli Shekels to convert.")
    currencies28 = {'US Dollar':0.260073,'Euro':0.246108, 'Pound':0.213892, 'Rupee':17.723059, 'Australian Dollar':0.353534, 'Canadian Dollar':0.344006, 'Singapore Dollar':0.373415, 'Swiss Franc':0.264083, 'Malaysian Rinnggit':1.163696, 'Japanese Yen':30.191140, 'Chinese Yuan Renminbi':1.804256, 'Argentine Peso':4.132128, 'Bahraini Dinar':0.098054, 'Botswana Pula':2.777232, 'Brazilian Real':0.831339, 'Bruneian Dollar':0.373415, 'Bulgarian Lev':0.481407, 'Chilean Peso':174.268358, 'Colombian Peso':761.738956, 'Croatian Kuna':1.862309, 'Czech Koruna':6.650001, 'Danish Krone':1.829532, 'Emirati Dirham':0.955248, 
'Hong Kong Dollar':2.017180, 'Hungarian Forint':75.819417, 'Icelandic Krona':29.622305, 'Indonesian Rupiah':3463.130650, 'Iranian Rial':8419.323873, 'Kazakhstani Tenge':86.353330, 'Kuwaiti Dinar':0.079576, 'Latvian Lat':0.172965, 'Libyan Dinar':0.374505, 'Lithuanian Litas':0.849761, 'Mexican Peso':5.561051, 'Nepalese Rupee':28.392240, 'New Zealand Dollar':0.370796, 'Norwegian Krone':2.222811, 'Omani Rial':0.100128, 'Pakistani Rupee':27.249144, 'Philippine Peso':12.880111, 'Polish Zloty':1.077290, 'Qatari Riyal':0.946977, 'Romanian New Leu':1.105355, 'Russian Ruble':15.606808, 'Saudi Arabian Riyal':0.975552, 'South African Rand':3.552221, 'South Korean Won':312.721189, 'Sri Lankan Rupee':38.979695, 
'Swedish Krona':2.353966, 'Taiwan New Dollar':8.327761, 'Thai Baht':9.269599, 'Trinidadian Dollar':1.750698, 'Turkish Lira':0.965083, 'Venezuelan Bolivar':2.598126}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies28:
        k28=(currencies28[user1])
    l28=user
    m28=k28*(float(l28))
    n=print(round(m28,2))
    print(user1 + "s")
if question is "Kazakhstani Tenge":
    user=input("Enter amount of Kazakhstani Tenges to convert.")
    currencies29 = {'US Dollar':0.003012,'Euro':0.002850, 'Pound':0.002476, 'Rupee':0.205261, 'Australian Dollar':0.004095, 'Canadian Dollar':0.003984, 'Singapore Dollar':0.004325, 'Swiss Franc':0.003057, 'Malaysian Rinnggit':0.013476, 'Japanese Yen':0.349932, 'Chinese Yuan Renminbi':0.020894, 'Argentine Peso':0.047707, 'Bahraini Dinar':0.001135, 'Botswana Pula':0.032161, 'Brazilian Real':0.009629, 'Bruneian Dollar':0.004325, 'Bulgarian Lev':0.005575, 'Chilean Peso':2.018085, 'Colombian Peso':8.821188, 'Croatian Kuna':0.021567, 'Czech Koruna':0.076989, 'Danish Krone':0.021183, 'Emirati Dirham':0.011062, 
'Hong Kong Dollar':0.023362, 'Hungarian Forint':0.877983, 'Icelandic Krona':0.343036, 'Indonesian Rupiah':40.102846, 'Iranian Rial':97.498543, 'Israeli Shekel':0.011578, 'Kuwaiti Dinar':0.000922, 'Latvian Lat':0.002003, 'Libyan Dinar':0.004337, 'Lithuanian Litas':0.009840, 'Mexican Peso':0.064378, 'Nepalese Rupee':0.328791, 'New Zealand Dollar':0.004294, 'Norwegian Krone':0.025738, 'Omani Rial':0.001160, 'Pakistani Rupee':0.315554, 'Philippine Peso':0.149141, 'Polish Zloty':0.012474, 'Qatari Riyal':0.010966, 'Romanian New Leu':0.012817, 'Russian Ruble':0.180957, 'Saudi Arabian Riyal':0.011297, 'South African Rand':0.041146, 'South Korean Won':3.621806, 'Sri Lankan Rupee':0.451398, 
'Swedish Krona':0.027252, 'Taiwan New Dollar':0.096457, 'Thai Baht':0.107351, 'Trinidadian Dollar':0.020274, 'Turkish Lira':0.011187, 'Venezuelan Bolivar':0.030087}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies29:
        k29=(currencies29[user1])
    l29=user
    m29=k29*(float(l29))
    n=print(round(m29,2))
    print(user1 + "s")
if question is "Kuwaiti Dinar":
    user=input("Enter amount of Kuwaiti Dinars to convert.")
    currencies30 = {'US Dollar':3.274377,'Euro':3.098060, 'Pound':2.692562, 'Rupee':223.177714, 'Australian Dollar':4.453204, 'Canadian Dollar':4.333251, 'Singapore Dollar':4.702070, 'Swiss Franc':3.324297, 'Malaysian Rinnggit':14.651201, 'Japanese Yen':380.078618, 'Chinese Yuan Renminbi':22.715992, 'Argentine Peso':52.001596, 'Bahraini Dinar':1.234517, 'Botswana Pula':34.965987, 'Brazilian Real':10.467529, 'Bruneian Dollar':4.702070, 'Bulgarian Lev':6.065227, 'Chilean Peso':2194.949430, 'Colombian Peso':9574.612607, 'Croatian Kuna':23.445403, 'Czech Koruna':83.717416, 'Danish Krone':23.029058, 'Emirati Dirham':12.026788, 
'Hong Kong Dollar':25.396955, 'Hungarian Forint':954.685230, 'Icelandic Krona':372.951566, 'Indonesian Rupiah':43599.456629, 'Iranian Rial':105994.996090, 'Israeli Shekel':12.589056, 'Kazakhstani Tenge':1086.798687, 'Latvian Lat':2.177317, 'Libyan Dinar':4.715103, 'Lithuanian Litas':10.696983, 'Mexican Peso':69.995121, 'Nepalese Rupee':357.464762, 'New Zealand Dollar':4.669530, 'Norwegian Krone':27.978745, 'Omani Rial':1.258999, 'Pakistani Rupee':342.664105, 'Philippine Peso':162.081804, 'Polish Zloty':13.572080, 'Qatari Riyal':11.922662, 'Romanian New Leu':13.914525, 'Russian Ruble':196.787569, 'Saudi Arabian Riyal':12.281452, 'South African Rand':44.766320, 'South Korean Won':3937.302219, 'Sri Lankan Rupee':490.763237, 
'Swedish Krona':29.630415, 'Taiwan New Dollar':104.885069, 'Thai Baht':116.706462, 'Trinidadian Dollar':21.858892, 'Turkish Lira':12.155454, 'Venezuelan Bolivar':32.710996}
    user1=input("Enter name of currency you want to convert to.")
    if user1 in currencies30:
        k30=(currencies30[user1])
    l30=user
    m30=k30*(float(l30))
    n=print(round(m30,2))
    print(user1 + "s")
 if question is "Latvian Lat":
     user=input("Enter amount of Latvian Lats to convert.")
     
 
    


