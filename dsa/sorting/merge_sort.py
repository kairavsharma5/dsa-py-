#merging two sorted arrays
left=[1,2,3,4]
right=[1,4,6,8,9,21]
def merge_arr(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if(left[i]<right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if (i<n):
        while i<n:
            result.append(left[i])
            i+=1
    if (j<m):
            while j<m:
                result.append(right[j])
                j+=1
    return result

# now how will merge sort work
nums=[1,3,2,4,2,323,91,34,4]
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left =merge_sort(left_arr)
    right =merge_sort(right_arr)
    return merge_arr(left,right) 
