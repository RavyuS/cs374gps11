from itertools import combinations

#From https://docs.python.org/3/library/itertools.html#itertools-recipes
def subsets_of_size_k(element_set, k):
    return map(set, combinations(element_set, k))

def tsp_solver(G, start_vertex):
    return 42