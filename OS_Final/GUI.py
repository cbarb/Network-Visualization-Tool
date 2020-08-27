import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data2.txt", sep=" ", names=["A", "B", "C", "D"])

cols = [0, 1]
df.drop(df.columns[cols], axis=1, inplace=True)
print(df)


def show_mpl():
    df = pd.read_csv("data2.txt", sep=" ", names=["A", "B", "C", "D"])

    cols = [0, 1]
    df.drop(df.columns[cols], axis=1, inplace=True)
    print(df)
    df['weight'] = df.groupby(['C', 'D'])['C'].transform('size')
    G = nx.from_pandas_edgelist(
        df, 'C', 'D', create_using=nx.DiGraph(), edge_attr='weight')
    pos = nx.circular_layout(G)
    print(nx.info(G))
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(
        u, v): d for u, v, d in G.edges(data="weight")}, label_pos=.66)
    plt.draw()
    plt.pause(0.5)
    plt.clf()


try:
    while True:
        show_mpl()
except KeyboardInterrupt:
    pass
