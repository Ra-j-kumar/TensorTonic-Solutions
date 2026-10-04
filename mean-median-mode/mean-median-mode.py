from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    c = Counter(x)
    x = np.array(x)
    ans = {"mean":float(np.mean(x)),"median":float(np.median(x))}
    q = max(list(c.values()))    
    a = float('inf')
    for i in c:
        if c[i] == q:  a = min(a,i)
    ans["mode"] = float(a)
    return ans