import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    ans = a = float(0)
    for i in range(k+1):            
        a = (math.comb(n,i) * (p**i) * ((1-p)**(n-i)))
        ans += a        
    return {"pmf":float(a),"cdf":ans}