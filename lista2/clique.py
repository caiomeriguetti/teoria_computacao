import copy
import math
import time

graph = [
    #0, 1, 2, 3, 4, 5, 6
    [0, 1, 0, 1, 1, 0, 0], # 0
    [1, 0, 1, 0, 0, 1, 1], # 1
    [0, 1, 0, 1, 0, 1, 0], # 2
    [1, 0, 1, 0, 1, 0, 0], # 3
    [1, 0, 0, 1, 0, 1, 0], # 4
    [0, 1, 1, 0, 1, 0, 0], # 5
    [0, 1, 0, 0, 0, 0, 0], # 6
]

def get_complement(g):
    len_g = len(g)
    complement = [[None for k in range(len_g)] for t in range(len_g)]

    for i, line in enumerate(g):
        for j, col in enumerate(line):
            val = 0
            if col == 0:
                val = 1

            complement[i][j] = val
    return complement


def get_all_combinations(n):

    subsets = []

    for i in [0, 1]:
        first_subset = []

        if i == 1:
            first_subset.append('0')

        root_element = {'path_size': 0, 'subset': first_subset}

        queue = [root_element]

        while 1:

            if len(queue) == 0:
                break

            element = queue.pop()

            path_size = element['path_size']
            subset = element['subset']

            if path_size == n-1:

                subsets.append(subset)

                continue

            newpathsize = path_size + 1

            left = {'path_size': newpathsize, 'subset': subset[:]}
            right = {'path_size': newpathsize, 'subset': subset + [str(newpathsize)]}

            queue.append(left)
            queue.append(right)

    return subsets


def is_clique(g, vertices):
    len_v = len(vertices)
    for i, v in enumerate(vertices):
        next_nodes = range(i+1, len_v)
        for j in next_nodes:
            if not (g[int(v)][int(vertices[j])] == 1):
                return False

    return True


def brute_force_find_max_clique(g):
    subsets = get_all_combinations(len(g))
    max_clique = None
    for subset in subsets:
        if is_clique(g, subset):
            if max_clique is None:
                max_clique = subset
            elif len(max_clique) < len(subset):
                max_clique = subset

    return max_clique

def get_max_civ(g):
    # aqui a alteracao na entrada
    # mudar o grafo para seu complemento
    # antes de encontrar a clique maxima
    # Encontrar uma clique maxima no complemento
    # e equivalente a encontrar um civ em g
    g_comp = get_complement(g)
    return brute_force_find_max_clique(g_comp)

from common import print_time

print_time(brute_force_find_max_clique, (graph,))
print_time(get_max_civ, (graph,))
