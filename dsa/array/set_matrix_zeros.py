#brute
matrix=[[0,2,3],[4,0,6],[7,8,9]]
'''def setZeroes(self, matrix):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0, r):
        for j in range(0, c):
            if matrix[i][j] == 0:
                self.markInfinity(matrix, i, j)

    for i in range(0, r):
        for j in range(0, c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0

def markInfinity(self, matrix, row, col):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0, r):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")
    for j in range(0, c):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")'''

#optimal
r=len(matrix)
c=len(matrix[0])
rowtrack=[0 for _ in range(r)]
coltrack=[0 for _ in range(c)]
for i in range(0,r):
    for j in range(0,c):
        if (matrix [i][j]==0):
            rowtrack[i]=-1
            coltrack[j]=-1
for i in range(0,r):
    for j in range(0,c):
        if (rowtrack[i]==-1  or coltrack[j]==-1):
            matrix[i][j]=0
print(matrix)