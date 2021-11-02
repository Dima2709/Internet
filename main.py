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
    df2 = df1.sum() / df1.where(df1 > 0).count()
    df4 = []
    for i in df2.index.tolist():
        mass = [j for j in i if j.isdigit()]
        df4.append(int(''.join(mass)))

    reg = lm.LinearRegression()
    reg.fit(np.array(df4).reshape(-1, 1), df2)

    print('\033[1m''Данные по городам', arg, ',которыми мы обладаем:''\033[0m')
    count = 0
    for i in df2:
        print('\033[91m',2010 + count,'\033[0m'' - ', i, 'USD')
        count += 1
    print('\033[1m''В', arg, ',в''\033[91m', arg1,'\033[0m''\033[1m' 'году, интернет будет стоить - ', reg.predict([[arg1]])[0], 'USD''\033[0m')

mash_line('Norway', 2050)
