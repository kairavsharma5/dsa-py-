from bisect import bisect_right

def median(mat, n, m):
    # n = rows, m = columns (n * m is odd)
    low = min(row[0] for row in mat)        # smallest value in the matrix
    high = max(row[-1] for row in mat)      # largest value in the matrix
    req = (n * m) // 2                      # median has more than req elements <= it

    while low <= high:
        mid = (low + high) // 2

        # count how many elements are <= mid
        count = 0
        for row in mat:
            count += bisect_right(row, mid)

        if count <= req:
            low = mid + 1                   # mid is too small
        else:
            high = mid - 1                  # mid might be the answer, try smaller

    return low