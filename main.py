def mash_line(arg, arg1):
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    import pandas as pd
    from sklearn import linear_model as lm
    import numpy as np

    df = pd.read_csv('city.csv')
    df1 = df[(df['Country'] == arg)]
    df1 = df1.drop('City', 1)
    df1 = df1.drop('Region', 1)
    df1 = df1.drop('Country', 1)

    for j in range(0,10):
        count = 0
        for i in df1.values:
            count += i[j]
        if count == 0:
            df1 = df1.drop(df1.columns[j], 1)
    df2 = df1.sum() / df1.where(df1 > 0).count()
    df4 = []
    for i in df2.index.tolist():
        mass = [j for j in i if j.isdigit()]
        df4.append(int(''.join(mass)))

    reg = lm.LinearRegression()
    reg.fit(np.array(df4).reshape(-1, 1), df2)

    print('\033[1m''Данные по городам', arg, ',которыми мы обладаем:''\033[0m')
    for i in range(len(df4)):
        print('\033[91m',df4[i],'\033[0m' ' - ', df2[i], ' USD')
    print('\033[1m''В', arg, ',в''\033[91m', arg1,'\033[0m''\033[1m' 'году, интернет будет стоить - ', reg.predict([[arg1]])[0], 'USD''\033[0m')

mash_line('New Zealand', 2000)
