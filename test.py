from BalancedBST import BalancedBST
from StandardBST import StandardBST
import time
import random


import sys
sys.setrecursionlimit(1000000)  # Set a high limit to handle large datasets

def main():
    sizes1 = [10**3, 10**4, 10**5, 10**6]
    sizes2 = [10**3, 10**4, 10**5]
    random.seed(1)
    c = 0.75
    
    for size in sizes1:
        # Generate a random array of the given size
        
        #inputData = generateData(size)
        inputData = generateRandom(size)
        start_time = time.time()
        tree = BalancedBST(inputData.pop(0),c)

        for i in inputData:
            tree.insert(i)

        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Print the results
        print(f"BalancedBST")
        print(f"Insert size: {size}")
        print(f"Execution time: {execution_time:.4f} seconds")
        print(f"Constant c: {c :0.3f}\n")


    for size in sizes1:
        # Generate a random array of the given size
        
        #inputData = generateData(size)
        inputData = generateRandom(size)
        start_time = time.time()
        tree = StandardBST(inputData.pop(0))

        for i in inputData:
            tree.insert(i)

        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Print the results
        print(f"StandardBST")
        print(f"Insert size: {size}")
        print(f"Execution time: {execution_time:.4f} seconds\n")


def generateData(n):
    return list(range(n, 0, -1))
def generateRandom(n):
    return [random.randint(0, n // 2) for _ in range(n)]

if __name__ == "__main__":
    main()

