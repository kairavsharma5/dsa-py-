matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=5
n=len(matrix)
m=len(matrix[0])
"""for i in range(0,n):
    if ((matrix[i][0]==target)):
        print(matrix[i][0])
        break
    elif((matrix[i][0]<=target<=matrix[i][m-1])):
        low=0
        high=m-1
        while(low<=high):
            mid=(low+high)//2
            if(matrix[i][mid]==target):
                print(True)
                break
            elif(matrix[i][mid]>target):
                high=mid-1
            else:
                low=mid+1
        """


#Optimal
low=0
high=(m*n-1)
while(low<=high):
    mid=(low+high)//2
    row=mid//m
    col=mid%m
    if(matrix[row][col]==target):
        print(True)
        break
    elif(matrix[row][col]<target):
        low=mid+1
    else:
        high=mid-1
