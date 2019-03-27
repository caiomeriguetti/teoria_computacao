import time

graph = {
    "0-1": 6,
    "0-3": 5,
    "0-2": 1,
    "1-2": 2,
    "1-4": 5,
    "3-5": 4,
    "2-3": 2,
    "2-4": 6,
    "2-5": 4,
    "4-5": 3
}

def get_neighbors_datastructure(g):
    n = {}
    for k in g.keys():
        indexes = k.split('-')
        indexes = [int(indexes[0]), int(indexes[1])]

        try:
            n[indexes[0]]
        except KeyError:
            n[indexes[0]] = set()


        try:
            n[indexes[1]]
        except KeyError:
            n[indexes[1]] = set()

        n[indexes[0]].add(indexes[1])
        n[indexes[1]].add(indexes[0])

    return n

def val(v1, v2):
    try:
        return graph[str(v1) + "-" + str(v2)]
    except KeyError:
        return graph[str(v2) + "-" + str(v1)]

check_added = {}

def prim(thegraph, origin):

    n = get_neighbors_datastructure(thegraph)

    n_nodes = len(n.keys())

    tree_nodes = [origin]

    result = []

    while 1:
        current_val = None
        current_edge = None

        for node in tree_nodes:
            #print node
            neightbors = n[node]
            for neigh in neightbors:
                nval = val(neigh, node)
                #print node, neigh, nval

                try:
                    if check_added[(node, neigh)]:
                        continue
                except KeyError:
                    pass

                if current_val is None or current_val > nval:
                    current_val = nval
                    current_edge = (node, neigh)


        result.append(current_edge)

        tree_nodes.append(current_edge[1])

        # salvando flag para determinar se uma
        # aresta ja foi adicionada a arvore
        # geradora minima
        check_added[current_edge] = True
        check_added[(current_edge[1], current_edge[0])] = True

        if len(tree_nodes) == n_nodes:
            return result

from common import print_time

print_time(prim, (graph, 0))
