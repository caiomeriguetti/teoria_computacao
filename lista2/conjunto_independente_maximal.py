graph = [
    [0, 1, 0, 1, 1, 0, 0], # 0
    [1, 0, 1, 0, 0, 1, 1], # 1
    [0, 1, 0, 1, 0, 1, 0], # 2
    [1, 0, 1, 0, 1, 0, 0], # 3
    [1, 0, 0, 1, 0, 1, 0], # 4
    [0, 1, 1, 0, 1, 0, 0], # 5
    [0, 1, 0, 0, 0, 0, 0], # 6
]

def check_independente(g, vertices):
    k = 0
    lenv = len(vertices)

    visited_map = {}

    while k < lenv:
        v = vertices[k]
        visited_map[v] = True

        t = k + 1

        while t < lenv:
            next_v = vertices[t]

            if graph[v][next_v] == 1:
                return False

            t += 1

        k += 1

    return True

def check_independente_maximal(g, vertices):

    if not check_independente(g, vertices):
        return False

    vertices_set = set(vertices)
    n_vertices = len(g)

    for graph_v in range(0, n_vertices):
        if graph_v in vertices_set:
            continue

        # check if the node graph_v has an edge to any of
        # the elements in vertices_set
        no_edge = True
        for v in vertices_set:
            if g[v][graph_v] == 1:
                no_edge = False


        # if no edges found, then the set is not maximal
        # because there is an independent set S that
        # contains the set vertices_set
        if no_edge == True:
            return False

    return True

def get_independente_maximal(g, v):
    current_set = set([v])
    n_vertices = len(g)

    all_vertices = range(0, n_vertices)

    for v in all_vertices:
        if v in current_set:
            continue

        no_edge = True
        for set_v   in current_set:
            if g[set_v][v] == 1:
                no_edge = False
                break

        if no_edge:
            current_set.add(v)

    return current_set


def calculate_degrees(g, removeds={}):
    len_g = len(g)
    degrees = {}
    for i in range(0, len_g):

        try:
            removeds[i]
            continue
        except:
            pass

        for j in range(0, len_g):

            try:
                removeds[j]
                continue
            except:
                pass

            if g[i][j] == 1:

                try:
                    degrees[i]
                except:
                    degrees[i] = float(0)

                try:
                    degrees[j]
                except:
                    degrees[j] = float(0)

                degrees[i] += 1.0/2.0
                degrees[i] += 1.0/2.0

    return degrees


def get_childs(g, v):

    l = g[v]

    childs = set()
    for i, el in enumerate(l):
        if el == 1:
            childs.add(i)

    return childs


def cind_max_2(g):

    def sort_function(a, b):
        if degrees[a] > degrees[b]:
            return 1
        elif degrees[b] > degrees[a]:
            return -1

        return 0

    degrees = calculate_degrees(g, {})
    vertices = degrees.keys()
    vertices.sort(sort_function)

    c_ind = []
    removeds = {}

    while 1:

        if len(vertices) == 0:
            return c_ind

        v = vertices.pop(0)

        try:
            removeds[v]
            continue
        except:
            pass

        c_ind.append(v)

        childs = get_childs(g, v)
        for child in childs:
            removeds[child] = True

        degrees = calculate_degrees(g, removeds)
        vertices = degrees.keys()
        vertices.sort(sort_function)

from common import print_time

print_time(check_independente, (graph, [1, 3]))
print_time(check_independente_maximal, (graph, [3, 5, 6]))
print_time(get_independente_maximal, (graph, 2))
print_time(cind_max_2, (graph,))
