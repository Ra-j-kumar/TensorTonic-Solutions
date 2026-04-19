import numpy as np

def matrix_inverse(A):
    a = np.array(A)
    if a.shape[0] != a.shape[1]:
        return None        
    try:        
        return np.linalg.inv(a)
    except np.linalg.LinAlgError:
        return None
            
