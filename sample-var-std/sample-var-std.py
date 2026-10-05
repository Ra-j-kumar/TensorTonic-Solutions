import numpy as np
import math
def sample_var_std(x: list) -> dict:
    x = np.array(x)
    center = x - np.mean(x)
    a = np.sum(center**2)/(len(x)-1)
    return  {"variance": float(a), "standard_deviation": math.sqrt(a)}