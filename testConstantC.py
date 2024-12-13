from BalancedBST import BalancedBST
from StandardBST import StandardBST
import time
import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    inputSize = 10**5
    c_values = np.arange(0.51, 0.99, 0.01)
    results = []


    for c in c_values:
        input = generateData(inputSize)
        tree = BalancedBST(input.pop(0), c)
        start_time = time.time()
        for j in input:
            tree.insert(j)
        end_time = time.time()
        results.append(end_time-start_time)

    # Plotting results
    plt.figure(figsize=(10, 6))
    plt.plot(c_values, results, marker='o')
    plt.title("Running Time of BalancedBST with Different c Values")
    plt.xlabel("c Value")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.show()




def generateData(n):
    return list(range(n, 0, -1))


if __name__ == "__main__":
    main()
