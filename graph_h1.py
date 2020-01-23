import networkx as nx
import matplotlib.pyplot as plt

def rysuj_graf(dane):
    for zaleznosci in dane:
        zaleznosci[1] = zaleznosci[1] + '.py'
    graf = nx.DiGraph(dane)
    nx.draw(graf, with_labels=True, font_weight='bold')
    plt.show()
