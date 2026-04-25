import numpy as np

def manhattan_distance(x, y):
    ans = 0
    for i in range(len(x)):
        ans += abs(x[i] - y[i])
    return ans