import numpy as np

def euclidean_distance(x, y):
    x , y = np.array(x) , np.array(y)
    return np.linalg.norm(x-y)