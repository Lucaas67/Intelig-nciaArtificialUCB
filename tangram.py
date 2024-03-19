import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Função para desenhar o Tangram montado em um quadrado
def desenhar_tangram_quadrado():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Definir as coordenadas do quadrado
    quadrado = [(0, 0), (4, 0), (4, 4), (0, 4)]

    # Definir as coordenadas de cada peça do Tangram
    coordenadas = {
        'triangulo_grande1': [(0, 0), (2, 2), (0, 4)],
        'triangulo_grande2': [(0, 4), (2, 2), (4, 4)],
        'triangulo_medio': [(2, 2), (4, 0), (4, 2)],
        'triangulo_pequeno1': [(0, 0), (1, 1), (2, 0)],
        'triangulo_pequeno2': [(2, 0), (4, 0), (3, 1)],
        'quadrado': [(1, 1), (2, 0), (3, 1), (2, 2)],
        'paralelogramo': [(2, 0), (4, 0), (3, 1), (1, 1)]
    }

    # Cores para cada peça do Tangram
    cores = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown']

    # Desenhar cada peça do Tangram
    for i, (peca, vertices) in enumerate(coordenadas.items()):
        polygon = Polygon(vertices, closed=True, edgecolor='black', facecolor=cores[i])
        ax.add_patch(polygon)

    # Desenhar o quadrado
    polygon = Polygon(quadrado, closed=True, edgecolor='black', facecolor='none')
    ax.add_patch(polygon)

    plt.xlim(-0.5, 4.5)
    plt.ylim(-0.5, 4.5)
    plt.show()

# Desenhar o Tangram montado em um quadrado
desenhar_tangram_quadrado()
