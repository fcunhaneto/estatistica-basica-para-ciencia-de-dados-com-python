import pandas as pd
import numpy as np


def quant(dataframe, column: str, amplitude: float, vmin=None, vmax=None):
    """
    Creates a frequency table for quantitative values

    :param dataframe: pandas dataframe
    :param column: nome da coluna
    :param amplitude: distancia entre as classes
    :param vmin: valor minimo
    :param vmax: valor máximo
    :return: pandas dataframe
    """

    if vmin is None:
        limit_vmin = np.floor(dataframe[column].min())
    else:
        limit_vmin = vmin

    if vmax is None:
        limit_vmax = np.ceil(dataframe[column].max())
    else:
        limit_vmax = vmax

    classes = []
    classes_str = []
    lower_limit = limit_vmin


    while lower_limit <= limit_vmax:
        classes.append([lower_limit, lower_limit + amplitude])

        if amplitude == 1:
            classes_str.append(lower_limit)
        else:
            classes_str.append(f'[{lower_limit: .2f}, {lower_limit + amplitude: .2f})', )


        lower_limit = lower_limit + amplitude

    total = dataframe[column].count()
    classes_values = []
    frequency_values = []
    frequency_aggregate = []
    accumulated = 0
    i = 0
    for c in classes:

        filter_ = dataframe[column].loc[(dataframe[column] >= c[0]) & (dataframe[column] < c[1])]
        total_classe = filter_.count()

        classes_values.append(total_classe)
        frequency_values.append(total_classe/total)
        accumulated = accumulated + filter_.count()

        if classes_values[i] != 0:
            frequency_aggregate.append(accumulated/total)
        else:
            frequency_aggregate.append(0)

        i = i + 1

    table = pd.DataFrame({column: classes_str, 'ni': classes_values, 'fi': frequency_values, 'fi.ac': frequency_aggregate})

    return table


def ticks(tmin: int, tmax: int, bins=None, amplitude=None):
    """

    :param amplitude:
    :param tmin:
    :param tmax:
    :param bins:
    :return:
    """

    if amplitude is None:
        amplitude = (tmax - tmin) / bins

    tick = tmin
    ticks_list = [tick]
    while tick < tmax:
        tick = tick + amplitude
        ticks_list.append(tick)

    return ticks_list


def qual(dataframe, column: str):
    """
    Create a frequency table for qualitative values

    :param dataframe: pandas dataframe
    :param column: nome da coluna
    :return: pandas dataframe
    """

    x = dataframe[column].to_numpy()
    y, t = np.unique(x, return_counts=True)
    table = pd.DataFrame({column: y, 'ni': t})

    table['fi'] = table['ni'] / table['ni'].sum()
    table['fi'] = table['fi'].round(2)

    return table


if __name__ == '__main__':
    df = pd.read_csv('data/questionario.csv')
    print(df.head(), '\n\n')

    frq = quant(df, 'Alt', 0.05, 1.45, 1.85)
    print(frq, '\n\n')

    frq = qual(df, 'Tole')
    print(frq, '\n\n')

    frq = quant(df, 'Idade', 1)
    print(frq, '\n\n')

    frq = quant(df, 'Peso', 10, 40, 95)
    print(frq, '\n\n')

    tk = ticks(40, 100, 6)
    print(tk, '\n\n')
