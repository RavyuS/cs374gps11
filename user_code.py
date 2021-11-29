from itertools import combinations, chain

from math import inf

#From https://docs.python.org/3/library/itertools.html#itertools-recipes
def subsets_of_size_k(element_set, k):
    return map(frozenset, combinations(element_set, k))


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def tsp_solver(G, start_vertex):
    num_nodes = G.number_of_nodes()
    WT = {k: [inf for i in range(num_nodes)] for k in map(frozenset, powerset(range(num_nodes)))}
    for i in range(1,num_nodes): # base cases
        WT[frozenset()][i] = G[0][i]['weight']
    cur_subset_size = 0

    while cur_subset_size is not num_nodes-1:
        cur_subset_size += 1
        subsets = subsets_of_size_k(range(1,num_nodes),cur_subset_size)
        for subset in subsets:
            for i in range(1, num_nodes):
                if i not in subset:
                    for t in subset:
                       
                        val = WT[subset - frozenset((t,))][t] + G[i][t]['weight']
                        if val < WT[subset][i]:
                            WT[subset][i] = val
    full_set = frozenset(range(1,num_nodes))
    min_weight = inf
    for i in range(1,num_nodes):
        val = WT[full_set - frozenset((i,))][i] + G[0][i]['weight']
        if val < min_weight:
            min_weight = val
    return min_weight


                    