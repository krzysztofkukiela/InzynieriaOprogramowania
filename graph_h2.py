import networkx as nx
import matplotlib.pyplot as plt
import pylab

#dane stworzone na potrzeby grafu, (już są zbędne, ale zostawiam żeby był podgląd na to w jakiej formie czyta graf)
#data_to_graph=(('funkcja_1', 'dodaj'), ('funkcja_1', 'odejmij'), ('funkcja_2', 'pomnoz'), ('funkcja_3', 'podziel'), ('funkcja_3', 'podziel'), ('funkcja_4', 'dodaj'), ('funkcja_4', 'dodaj'))  #w formie tuple
#after_calc=(('funkcja_1', 'dodaj'), ('funkcja_1', 'odejmij'), ('funkcja_2', 'pomnoz'), ('funkcja_3', 'podziel'),  ('funkcja_4', 'dodaj')) # w formie tuple (te dane są wynikiem znalezienia w data_to_graph powtorzen, kazdemu elementowi jest przypisywana ilosc powtorzen, nie ma elementu z 0 liczba powtorzen)
#wage_to_graph=[1, 1, 1, 2, 2] #lista z liczbami powtorzen

def wage_graph(dane, wagi):
    '''graf do historyjki 2'''

    G=nx.DiGraph()
    u=0
    for y in dane:
        tab_y=[]
        tab_y.append(y)
        data=[dane for dane in tab_y]
        count=wagi[u]
        G.add_edges_from(data, weight=count)
        u+=1
    edge_labels=dict([((u,v,),d['weight'])
            for u,v,d in G.edges(data=True)])
    pos=nx.circular_layout(G)               #zmiana aby była lepsza widoczność 
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw(G,pos, with_labels=True, font_weight='bold', node_size=1500,edge_cmap=plt.cm.Reds)
    pylab.show()

def historyjka_3(dane, wagi):
    G=nx.DiGraph()
    u=0
    for y in dane:
        tab_y=[]
        tab_y.append(y)
        data=[dane for dane in tab_y]
        count=wagi[u]
        G.add_edges_from(data,weight=count)
        u+=1
    edge_labels=dict([((u,v,),d['weight'])
            for u,v,d in G.edges(data=True)])
    pos=nx.circular_layout(G)
    fig = plt.figure()
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw(G,pos, with_labels=True,
                   font_weight='bold',
                   node_size=350,
                   node_color='#2F8500',
                   edge_color='white')
    fig.set_facecolor("#7FA05B")
    pylab.show()
