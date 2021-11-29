from starter_code import generate_tsp_test_case, traveling_salesman_brute_force
from user_code import tsp_solver
import time

WEIGHT_LIMIT = 1000 #Default according to GSP
NUM_NODES = [3,4,5,6,7,10,12] # list used to generate test cases with specified number of nodes. Feel free to modify.


def runTest():
    num_correct = 0
    for i in NUM_NODES: 
        test_g = generate_tsp_test_case(i,WEIGHT_LIMIT)
        print(f"Testing randomly generated graph with {i} nodes")
        #Brute force to get solutions to compare against. Also measure time
        b_start = time.time()
        b_tour, b_weight = traveling_salesman_brute_force(test_g)
        b_end = time.time()
        b_time = b_end - b_start
        print(f"Brute Force solution weight: {b_weight}, Time: {b_time}")

        #Test implementation
        dp_start = time.time()
        dp_weight = tsp_solver(test_g,0) #Default start at 0 for this test to follow bruteforce soln
        dp_end = time.time()
        dp_time = dp_end - dp_start
        print(f"DP solution: {dp_weight}, Time: {dp_time}")

        if b_weight is dp_weight:
            print("Correct soln!\n\n")
            num_correct+=1
        else:
            print("NOT correct :(\n\n")
    print(f"Total correct solns: {num_correct} out of {len(NUM_NODES)}")





if __name__ == '__main__':
    runTest()