matrix=[[1,2,3],[4,5,6],[7,8,9]]
r=len(matrix)   # its also the len of matriz
c=len(matrix[0])
# brute
'''for i in range(0,r):
    for j in range(0,c):
        print(matrix[i][j],end="")
    print("")
result=[[0 for _ in range(r)] for _ in range(r)]
for i in range(0,r):
    for j in range(0,c):
        result[j][(r-1)-i] = matrix[i][j]
'''


