import random
import networkx as nx
from itertools import permutations

def generate_tsp_test_case(num_nodes, weight_limit):
    "Generate a complete graph with random weights"
    G = nx.complete_graph(num_nodes)

    for u,v in G.edges():
        G[u][v]['weight'] = random.randint(1, weight_limit)

    return G

def traveling_salesman_brute_force(G, start_node = 0):
    "Computes the cheapest TSP tour by brute force"
    nodes = set(G.nodes)
    nodes.remove(start_node)

    cheapest_tour_weight = None
    cheapest_tour = None

    for tour_tuple in permutations(nodes):
        tour_weight = 0
        tour = [start_node] + list(tour_tuple) + [start_node]
        for u,v in zip(tour, tour[1:]):
            tour_weight += G[u][v]['weight']

        if cheapest_tour is None or cheapest_tour_weight > tour_weight:
            cheapest_tour = tour
            cheapest_tour_weight = tour_weight

    if cheapest_tour is None or cheapest_tour_weight is None:
        raise ValueError("Could not find cheapest tour")

    return cheapest_tour, cheapest_tour_weight
