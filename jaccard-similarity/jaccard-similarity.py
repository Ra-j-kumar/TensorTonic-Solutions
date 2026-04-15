def jaccard_similarity(set_a, set_b):
    # jaccard similarity
    a , b = set(set_a) , set(set_b)
    common = a.intersection(b)
    all = a.union(b)
    if len(common) == 0 or len(all) == 0:
        return 0
    return len(common) / len(all)