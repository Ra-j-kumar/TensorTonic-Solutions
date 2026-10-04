import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    a, b = np.array(a) , np.array(b)
    c , d = np.linalg.norm(a) ,np.linalg.norm(b)
    if c == 0 or d == 0:
        return float(0)
    return float(np.dot(a,b)/(c*d))