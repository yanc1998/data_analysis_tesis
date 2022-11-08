import matplotlib.pyplot as plt
import numpy as np
from os import getcwd


def autolabel(rects, ax):
    """Funcion para agregar una etiqueta con el valor en cada barra"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def graphic_bar(value):
    times = list(map(lambda x: x.time, value.values))
    counts = list(map(lambda x: x.count, value.values))
    title = f'Gráfica para n = {value.n} y k = {value.k}'
    # Obtenemos la posicion de cada etiqueta en el eje de X
    x = np.arange(len(counts))
    # tamaño de cada barra
    width = 0.5

    fig, ax = plt.subplots()

    # Generamos las barras para el conjunto de hombres
    rects1 = ax.bar(x, times, width, label='Tiempo')

    # Añadimos las etiquetas de identificacion de valores en el grafico
    ax.set_ylabel('Tiempo en segundos')
    ax.set_xlabel('count')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(counts)
    # Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
    ax.legend()

    # Añadimos las etiquetas para cada barra
    autolabel(rects1, ax)
    fig.tight_layout()
    path = getcwd() + '/output/' + title + '.png'
    plt.savefig(path)
    plt.close(fig)
    # Mostramos la grafica con el metodo show()
    # plt.show()


def plot(value):
    times = list(map(lambda x: x.time, value.values))
    counts = list(map(lambda x: x.count, value.values))
    title = f'Gráfica para n = {value.n} y k = {value.k}'
    plt.title(title)
    plt.ylabel('Tiempo en segundos')
    plt.xlabel('count')
    plt.plot(counts, times)
    path = getcwd() + '/output/functions_data/' + title + '.png'
    plt.savefig(path)
    plt.close()
    # plt.show()


def graphic_bar_des(value, i):
    times = list(map(lambda x: float(x), value.values))
    counts = list(map(lambda x: x + 1, range(len(value.values))))
    title = f'Gráfica para n = {value.n} y k = {value.k} DES numero {i}'
    # Obtenemos la posicion de cada etiqueta en el eje de X
    x = np.arange(len(counts))
    # tamaño de cada barra
    width = 0.5

    fig, ax = plt.subplots()

    # Generamos las barras para el conjunto de hombres
    rects1 = ax.bar(x, times, width, label='Promedio de Cambios')

    # Añadimos las etiquetas de identificacion de valores en el grafico
    ax.set_ylabel('Promedio de Cambios')
    ax.set_xlabel('k')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(counts)
    # Añadimos un legen() esto permite mmostrar con colores a que pertence cada valor.
    ax.legend()

    # Añadimos las etiquetas para cada barra
    autolabel(rects1, ax)
    fig.tight_layout()
    path = getcwd() + '/output/output_des/' + title + '.png'
    plt.savefig(path)
    plt.close(fig)
    # Mostramos la grafica con el metodo show()
    # plt.show()
