def image_histogram(image):
    x = [0] * 256
    for i in image:
        for j in i:
            x[j] += 1
    return x
    