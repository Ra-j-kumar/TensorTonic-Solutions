def detect_drift(reference_counts, production_counts, threshold):
    refernce_sum = sum(reference_counts)
    production_sum = sum(production_counts)

    ans = 0

    for r, p in zip(reference_counts , production_counts):
        ans += abs((r/refernce_sum) - (p/production_sum))

    ans *= 0.5 

    return {
        "score" : ans,
        "drift_detected" : ans > threshold
    }