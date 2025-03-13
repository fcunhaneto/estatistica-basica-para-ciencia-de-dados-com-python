import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def generate_ticks(values, bars):
    values.sort()
    vmin = values[0]
    vmax = values[-1]
    amplitude = (vmax - vmin) / bars
    ticks = [vmin]
    last = vmin+amplitude
    ticks.append(last)
    for x in range(bars - 1):
        last += amplitude
        ticks.append(last)
    return ticks


def generate_frequency(total,yticks):
    freq_rel = []
    for item in yticks:
        x = item/total
        freq_rel.append(x*100)
    return freq_rel


def freq_hist(bars, data_series, title, unit, dpi=100, w=10, h=5):
    l = data_series.values
    label_format = '{:,.2f}%'
    ax = data_series.plot.hist(bins=bars, rwidth=0.95)

    yticks = ax.get_yticks()
    total = len(l)
    freq_rel = generate_frequency(total, yticks)
    ticks_loc = yticks.tolist()
    ax.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
    ax.set_yticklabels([label_format.format(x) for x in freq_rel])
    ax.set_yticks(ax.get_yticks().tolist())

    fig = plt.gcf()
    fig.set_size_inches(w, h)
    fig.set_dpi(dpi)

    ticks = generate_ticks(l, bars)
    plt.xticks(ticks)
    plt.title(title)
    plt.xlabel(unit)
    plt.ylabel('Frequência')
    plt.grid(axis='y')

    plt.show()


if __name__ == '__main__':
    # km = pd.Series([4,6,6,7,11,13,18,19,21,24,26,27,35,36,36,42,43,45,49])
    # freq_hist(5,km,'Distância','km')

    df = pd.read_csv('data/questionario.csv')

    peso = df['Peso']
    freq_hist(10, peso, 'Peso', 'Kg')

    # altura = df['Alt']
    # freq_hist(10, altura, 'Altura', 'metro')

    # import numpy as np
    # valores = np.random.normal(loc=0, scale=1, size=50)
    # arr = pd.Series(valores)
    # gera_histograma(10, arr, 'Altura', 'metro')