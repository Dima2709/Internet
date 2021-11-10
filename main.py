def mash_line(arg, arg1):
    #1) импорт библиотек, import warnings - чтобы избежать в выводе FutureWarning.
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    import pandas as pd
    from sklearn import linear_model as lm
    import numpy as np


    #2) читаем файл
    df = pd.read_csv('city.csv')
    #3) находим интересующую страну,сохраняем в другую переменную - df1, иначе не поменяется.
    df1 = df[(df['Country'] == arg)]
    #4) удаляем столбцы, которые нас не интересуют, вот из-за этого как раз вылетала FutureWarning
    df1 = df1.drop('City', 1)
    df1 = df1.drop('Region', 1)# <------ 1 если хочешь удалить колонку, 0 строку.
    df1 = df1.drop('Country', 1)

    #5) удаляем столбцы, где нет данных(стоят нули во всей колонке), j range (0,10), для индекса - 10 колонок(2010-2020)
    for j in range(0,10):
    #6) count для подсчета суммы колонки, если он 0, тогда дропаем этот год
        count = 0
        for i in df1.values:
            count += i[j]
        if count == 0:
            df1 = df1.drop(df1.columns[j], 1)
    #7) считаем среднее арифметическое каждого года, без учета 0 (df1.where(df1 > 0).count()), чтобы была более точная цифра. получается серия(serias), кладем ее в переменную (Это Y в нашем случае)
    df2 = df1.sum() / df1.where(df1 > 0).count()
    #8) достаем года, это X в нашем случае.
    df4 = []
    for i in df2.index.tolist():
        mass = [j for j in i if j.isdigit()]
        df4.append(int(''.join(mass)))

    #9) Создаем объект linear_model
    reg = lm.LinearRegression()
    #10) даем наши данные на тренировку, np.array(df4).reshape(-1, 1) - это X (года), df2 - это Y (цена).
    reg.fit(np.array(df4).reshape(-1, 1), df2)

    print('\n','\033[1m''Данные по городам', arg, ',которыми мы обладаем:''\033[0m')
    for i in range(len(df4)):
        print('\033[91m',df4[i],'\033[0m' ' - ', df2[i], ' USD')

        #11) Выводим результат reg.predict([[arg1]])[0], можно без нуля, там массив на выходе просто.
    print('\n''\033[1m''В', arg, ',в''\033[91m', arg1,'\033[0m''\033[1m' 'году, интернет будет стоить - ', reg.predict([[arg1]])[0], 'USD''\033[0m')

#12) Формула выглядит так - y = kx + b, т.е прямая линия, если коэффициент положительный, тогда она идет наверх, если = 0, тогда прямо, если отрицательный то вниз.

# reg.coef_ - можно посмотреть коэффициент. df2.corr() корреляция (зависимости величин друг от друга, чем меньше, меньше влияет)

# Получается, главная задача найти x и y в нашем датафрейме. Ну и скормить их.

mash_line('Belgium', 3500)
