merge = lambda l1, l2 : (len(l1) == 0 and l2) or (len(l2) == 0 and l1) or (l1[0] <= l2[0] and l1[:1] + merge(l1[1:], l2)) or (l2[:1] + merge(l1, l2[1:]))
mergesort = lambda l : (len(l) == 1 and l) or merge(mergesort(l[:len(l)/2]), mergesort(l[len(l)/2:]))
print(mergesort(map(int, raw_input().split())))