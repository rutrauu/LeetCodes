def bucketSort(array):
    
    buckets = [[] for _ in range (10)]

    for item in array:
        buckets[item].append(item)
    out = []

    for bucket in buckets:
        for item in bucket:
            out.append(item)