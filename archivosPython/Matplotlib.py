#from matplotlib import plot as plt
import matplotlib.pyplot as plt

def lineplots(x, y, **kwargs): # LINEPLOTS

    ''' ==============================
    | color: (color de la linea)
    | 'b' blue
    | 'g' green
    | 'r' red
    | 'c' cyan
    | 'm' magenta
    | 'y' yellow
    | 'k' black
    | 'w' white
    |
    | ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
    =============================== '''

    ''' ===============================
    | marker: (tipo de marcador)
    | '.' point marker
    | ',' pixel marker
    | 'o' circle marker
    | 'v' triangle_down marker
    | '^' triangle_up marker
    | '<' triangle_left marker
    | '>' triangle_right marker
    | '1' tri_down marker
    | '2' tri_up marker
    | '3' tri_left marker
    | '4' tri_right marker
    | 's' square marker
    | 'p' pentagon marker
    | '*' star marker
    | 'h' hexagon1 marker
    | 'H' hexagon2 marker
    | '+' plus marker
    | 'x' x marker
    | 'D' diamond marker
    | 'd' thin_diamond marker
    | '|' vline marker
    | '_' hline marker
    | 'None' no marker
    |
    | ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_', 'None']
    =============================== '''

    ''' ===============================
    | linestyle: (tipo de linea)
    | '-' solid line style
    | '--' dashed line style
    | '-.' dash-dot line style
    | ':' dotted line style
    |
    | ['-', '--', '-.', ':']
    =============================== '''

    # plt.figure(figsize=(10, 5)) # (ancho, alto) # para cambiar el tamaño de la figura
    
    plt.plot(x, y, marker='o', linestyle='--', color='g', label='pais 1') # parametros opcionales: color, marker, linestyle, label
    
    if kwargs:
        plt.plot(kwargs['x2'], kwargs['y2'], marker='d', linestyle='-', color='r', label='pais 2')

    plt.xlabel('Año')
    plt.ylabel('Cantidad de personas')
    plt.title('Cantidad de personas que viven en cada año')
    # plt.yticks([numeros de eje y]) # para cambiar los numeros de eje y
    plt.legend() # paramatros opcionales: loc, numpoints, prop, frameon, borderaxespad, labelspacing, handlelength, handletextpad, borderaxespad, columnspacing, ncol

    ''' ===============================
    | loc: (ubicacion de la leyenda)
    | Location String - Location code
    | 'best'           0
    | 'upper right'    1
    | 'upper left'     2
    | 'lower left'     3
    | 'lower right'    4
    | 'right'          5
    | 'center left'    6
    | 'center right'   7
    | 'lower center'   8
    | 'upper center'   9
    | 'center'         10
    |
    | ['best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center']
    | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    =============================== '''
    
    plt.show() # O tambien plt.ion() para que se muestre en tiempo real

def barplots(x, y, **kwargs): # BARPLOTS
    
    plt.bar(x, y)
    plt.show()

def piecharts(x, y): # PIECHARTS
    plt.pie(y, labels=x)
    plt.axis('equal')
    plt.show()

def histograms(x, y): # HISTOGRAMS
    plt.hist(x, bins=y)
    plt.show()

def boxplots(x): # BOXPLOTS
    plt.boxplot(x)
    plt.show()

def scatterplots(x, y): # SCATTERPLOTS
    plt.scatter(x, y)
    plt.show()

def subplots(x, y, x2, y2): # SUBPLOTS
    fig, ax = plt.subplots(1, 2, sharey=True)
    ax[0].plot(x, y, color='g')
    ax[1].plot(x2, y2, color='r')
    plt.show()


def main():

    ''' ===============================
    LINEPLOTS:
    # pais 1
    x = [2016, 2017, 2018, 2019, 2020,2021]
    y = [45, 46, 47, 48, 50, 51]

    # pais 2
    x2 = [2016, 2017, 2018, 2019, 2020,2021]
    y2 = [45, 46, 47, 48, 50, 51]

    lineplots(x, y, x2=x2, y2=y2)
    =============================== '''

    ''' ===============================
    BARPLOTS:
    x = ['Argentina', 'Colombia', 'Peru']
    y = [40, 50, 33]
    barplots(x, y)
    =============================== '''

    ''' ===============================
    PIECHARTS:
    x = ['Argentina', 'Colombia', 'Peru']
    y = [40, 50, 33]
    piecharts(x, y)
    =============================== '''

    ''' ===============================
    HISTOGRAMS:
    edades = [15, 16, 17, 28, 21, 21, 22, 23, 24, 25, 26, 30, 32, 35]
    bins = [15, 20, 25, 30, 35]
    histograms(edades, bins, edgecolor='black')
    =============================== '''

    ''' ===============================
    BOXPLOTS:
    edades = [15, 16, 17, 28, 21, 21, 22, 23, 24, 25, 26, 30, 32, 35, 77]
    boxplots(edades)
    =============================== '''

    ''' ===============================
    SCATTERPLOTS:
    a = [1, 2, 3, 4, 5, 4, 2, 4, 7, 2, 5, 9, 4]
    b = [7, 6, 2, 9, 2, 3, 2, 6, 9, 4, 5, 7, 2]
    scatterplots(a, b)
    =============================== '''

    ''' ===============================
    SUBPLOTS:
    =============================== '''
    # pais 1
    x = [2016, 2017, 2018, 2019, 2020,2021]
    y = [45, 46, 47, 48, 50, 51]

    # pais 2
    x2 = [2016, 2017, 2018, 2019, 2020,2021]
    y2 = [45, 46, 47, 48, 50, 51]
    subplots(x, y, x2, y2)

main()