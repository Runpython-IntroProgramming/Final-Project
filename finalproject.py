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