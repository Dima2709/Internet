def mash_line(arg, arg1):
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    import pandas as pd
    from sklearn import linear_model as lm
    import numpy as np
    df = pd.read_csv('city.csv')
    reg = lm.LinearRegression()
    df1 = df[(df['Country'] == arg)]
    df1 = df1.drop('City', 1)
    df1 = df1.drop('Region', 1)
    df1 = df1.drop('Country', 1)
    df2 = df1.sum() / df1.where(df1 > 0).count()
    df3 = df2.index.tolist()
    df4 = []
    for i in df3:
        mass = []
        for j in i:
            if j.isdigit():
                mass.append(j)
        df4.append(int(''.join(mass)))
    reg.fit(np.array(df4).reshape(-1, 1), df2)
    print('\033[1m''Данные по городам', arg, ',где есть интернет:''\033[0m')
    count = 0
    for i in df1.sum() / df1.where(df1 > 0).count():
        print('\033[91m',2010 + count,'\033[0m'' - ', i)
        count += 1
    print('\033[1m''В', arg, ',в''\033[91m', arg1,'\033[0m''\033[1m' 'году, интернет будет стоить - ', reg.predict([[arg1]])[0], 'USD''\033[0m')

mash_line('Russia', 2045)