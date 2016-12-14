
currencies = {'Euro':.942218, 'Pound':.794856, 'Rupee':67.412529, 
'Australian Dollar':1.341483, 'Canadian Dollar':1.320036, 'Singapore Dollar':1.424582, 
'Swiss Franc':1.016520, 'Malaysian Rinnggit':4.420300, 'Japanese Yen':114.212492, 
'Chinese Yuan Renminbi':6.880900, 'Argentine Peso':15.994313, 'Bahraini Dinar':0.377000, 
'Botswana Pula':10.834236, 'Brazilian Real':3.376349, 
'Bruneian Dollar':1.424582, 'Bulgarian Lev':1.843010, 'Chilean Peso':654.800000, 
'Colombian Peso':3003.499994, 'Croatian Kuna':7.102514, 'Czech Koruna':25.489149, 
'Danish Krone':7.009617, 'Emirati Dirham':3.673000, 'Hong Kong Dollar':7.756443, 
'Hungarian Forint':296.213068, 'Icelandic Krona':111.510000, 
'Indonesian Rupiah':13352.062264, 'Iranian Rial':32150.000001, 'Israeli Shekel':3.813926, 
'Kazakhstani Tenge':334.570007, 'Kuwaiti Dinar':0.304875, 'Latvian Lat':0.662191, 'Libyan Dinar':1.417500, 'Lithuanian Litas':3.253290,
'Mexican Peso':20.315152, 'Nepalese Rupee':107.699997, 'New Zealand Dollar':1.393270, 'Norwegian Krone':8.433343, 'Omani Rial':0.384900, 
'Pakistani Rupee':104.750000, 'Philippine Peso':49.750000, 'Polish Zloty':4.184430, 'Qatari Riyal':3.641200, 'Romanian New Leu':4.240725, 'Russian Ruble':63.498941, 
'Saudi Arabian Riyal':3.750250, 'South African Rand':13.654455, 'South Korean Won':1164.612381, 'Sri Lankan Rupee':148.320007, 
'Swedish Krona':9.128824, 'Taiwan New Dollar':31.756537, 'Thai Baht':35.647564, 'Trinidadian Dollar':6.680000, 'Turkish Lira':3.452651, 'Venezuelan Bolivar':9.975000}

user=input("Enter amount of US Dollars to convert.")
user1=input("Enter name of currency you want to convert to.")
if user1 in currencies:
    k=(currencies[user1])
    l=user
    m=k*(float(l))
    print(m)
    print(user1)

    
    
    
    
    