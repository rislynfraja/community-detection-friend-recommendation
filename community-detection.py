#SELF-CONTAINED VERSION OF GIRVAN NEWMAN ALGORITHM

#import networkx and matplot to create graph displays
import networkx as nx
import matplotlib.pyplot as plt

def detect_comm(vertices, edges):

    temp = {} # holds weights and pairs before they're transferred

    #FIRST: CHECK FOR DUPLICATE EDGES (BETWEEN THE SAME USERS) AND COMBINE THEIR WEIGHTS
    for edge in edges:
        pair = tuple(sorted(edge[:2])) #sort the first two values in edge which makes sure that any repeats will look the same
        weight = edge[2] #separate the last value in the edge aka the weight of the edge

        if pair in temp: #if the pair already has an edge between them
            temp[pair] += weight #add to the weight of that edge
        else: #pair does not have an edge stored between them yet
            temp[pair] = weight #create a slot and assign the weight

    #line below transfers values with first user, second user, and weight of edge between
    #them to combined_edges
    combined_edges = [(pair[0], pair[1], weight) for pair, weight in temp.items()]

    gram = nx.Graph() #create the graph
    gram.add_nodes_from(vertices) #add vertices to the network
    for edge in combined_edges: #add combined edges to the network (no duplicates)
        gram.add_edge(edge[0], edge[1], weight=edge[2])

    def max_edge_finder(graph):
        #use built in function in networkx to get the edge betweeness
        #this is how many times the edge is on a shortest path between any two vertices
        edge_betweenness = nx.edge_betweenness_centrality(graph)
        return max(edge_betweenness, key=edge_betweenness.get) #return edge w/ highest edge_betweenness

    def check_split(graph):
        #gets the split up pieces in the graph using networkx built in connected_components
        pieces = list(nx.connected_components(graph))

        if len(pieces) <= 1: #if the graph is split into only one piece = graph has not been split yet
            return False #continue splitting

        else: #graph has been split into multiple pieces
            #line below creates a dictionary to hold the nodes and the piece that they are in
            node_piece = {node: x for x, piece in enumerate(pieces) for node in piece}

            k_in = 0 #edges inside the piece of the graph
            k_out = 0 #edges that lead outside of the piece of the graph

            for x, y in graph.edges():
                if node_piece[x] == node_piece[y]:
                    k_in += 1
                else:
                    k_out += 1

        return k_in > k_out # will return true if strong community

    while True:
        need_removal = max_edge_finder(gram)
        gram.remove_edge(*need_removal)

        if check_split(gram) == True:
            gram.add_edge(*need_removal)
            break #end the loop because the graph has been split with strong communities

    #DISPLAY GRAPH
    pos = nx.spring_layout(gram, seed=7, scale=2, k=0.5)
    nx.draw_networkx_nodes(gram, pos, node_size = 400, node_color = 'pink')
    nx.draw_networkx_edges(gram, pos, width=1.5, alpha=0.8)
    nx.draw_networkx_labels(gram, pos, font_size=10, font_weight='bold')

    plt.axis('off')
    plt.show()

#CODE FOR TESTING GOES BELOW
vertices = list(range(1,35))
edges = [(1,2,4),(1,3,5),(1,4,3),(1,5,3),(1,6,3),(1,7,3),(1,8,2),(1,9,2),(1,11,2),(1,12,3),(1,13,1),
         (1,14,3),(1,18,2),(1,20,2),(1,22,2),(1,32,2),(2,1,4),(2,3,6),(2,4,3),(2,8,4),(2,14,5),(2,18,1),
         (2,20,2),(2,22,2),(2,31,2),(3,1,5),(3,2,6),(3,4,3),(3,8,4),(3,9,5),(3,10,1),(3,14,3),(3,28,2),(3,29,2),
         (3,33,2),(4,1,3),(4,2,3),(4,3,3),(4,8,3),(4,13,3),(4,14,3),(5,1,3),(5,7,2),(5,11,3),(6,1,3),(6,7,5),
         (6,11,3),(6,17,3),(7,1,3),(7,5,2),(7,6,5),(7,17,3),(8,1,2),(8,2,4),(8,3,4),(8,4,3),(9,1,2),(9,3,5),(9,31,3),
         (9,33,3),(9,34,4),(10,3,1),(10,34,2),(11,1,2),(11,5,3),(11,6,3),(12,1,3),(13,1,1),(13,4,3),(14,1,3),
         (14,2,5),(14,3,3),(14,4,3),(14,34,3),(15,33,3),(15,34,2),(16,33,3),(16,34,4),(17,6,3),(17,7,3),(18,1,2),
         (18,2,1),(19,33,1),(19,34,2),(20,1,2),(20,2,2),(20,34,1),(21,33,3),(21,34,1),(22,1,2),(22,2,2),(23,33,2),
         (23,34,3),(24,26,5),(24,28,4),(24,30,3),(24,33,5),(24,34,4),(25,26,2),(25,28,3),(25,32,2),(26,24,5),(26,25,2),
         (26,32,7),(27,30,4),(27,34,2),(28,3,2),(28,24,4),(28,25,3),(28,34,1),(29,3,2),(29,32,2),(29,34,2),(30,24,3),
         (30,27,4),(30,33,4),(30,34,2),(31,2,2),(31,9,3),(31,33,3),(31,34,3),(32,1,2),(32,25,2),(32,26,7),(32,29,2),
         (32,33,4),(32,34,4),(33,3,2),(33,9,3),(33,15,3),(33,16,3),(33,19,1),(33,21,3),(33,23,2),(33,24,5),(33,30,4),
         (33,31,3),(33,32,4),(33,34,5),(34,9,4),(34,10,2),(34,14,3),(34,15,2),(34,16,4),(34,19,2),(34,20,1),(34,21,1),
         (34,23,3),(34,24,4),(34,27,2),(34,28,4),(34,29,2),(34,30,2),(34,31,3),(34,32,4),(34,33,5)]

detect_comm(vertices,edges)
