def expected_value_discrete(x: list, p: list) -> float:    
    ans = float(0)
    for i in range(len(x)):
        ans += x[i]*p[i]
    return ans