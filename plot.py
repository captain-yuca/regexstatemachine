import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def animate(i):
    colors = ['r', 'b', 'g', 'y', 'w', 'm']
    plt.pause(0.5)
    return nx.draw_circular(G, node_color=[random.choice(colors) for j in range(4)])

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')])
nx.draw_circular(G)
fig = plt.gcf()

# Animator call
anim = animation.FuncAnimation(fig, animate, frames=20, interval=20, blit=True)
plt.show()
# color_values = ['lightblue' for node in G.nodes()]

# Specify the edges you want here

# red_edges = [('A', 'C'), ('E', 'C')]
# edge_colours = ['black' if not edge in red_edges else 'red'
#                 for edge in G.edges()]
#
#
# black_edges = [edge for edge in G.edges() if edge not in red_edges]




# Need to create a layout when doing
# separate calls to draw nodes and edges
# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
#                        node_color = color_values, node_size = 500)
# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
# plt.show()
# color_values = ['red' for node in G.nodes()]
# nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
#                        node_color = color_values, node_size = 500)
# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
# plt.show()
