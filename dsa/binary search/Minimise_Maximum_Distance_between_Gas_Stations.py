#BRUTE

"""def minimiseMaxDistance(arr, k):
    n = len(arr)
    how_many = [0] * (n - 1)      # how_many[i] = new stations placed in gap i

    for _ in range(k):            # place stations one by one
        max_section = -1
        max_ind = -1
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            section_len = diff / (how_many[i] + 1)
            if section_len > max_section:
                max_section = section_len
                max_ind = i
        how_many[max_ind] += 1    # put the new station in the biggest section

    max_ans = -1
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        section_len = diff / (how_many[i] + 1)
        max_ans = max(max_ans, section_len)
    return max_ans"""



#optimal
def minimiseMaxDistance(arr, k):
    n = len(arr)
    lo, hi = 0, max(arr[i + 1] - arr[i] for i in range(n - 1))

    while hi - lo > 1e-6:
        mid = (lo + hi) / 2
        cnt = 0                           # stations needed so every gap <= mid
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            c = int(diff / mid)
            if diff == mid * c:           # exact fit: one fewer station needed
                c -= 1
            cnt += c
        if cnt > k:                       # needs too many stations, so mid is too small
            lo = mid
        else:                             # k stations are enough, try smaller
            hi = mid
    return hi
