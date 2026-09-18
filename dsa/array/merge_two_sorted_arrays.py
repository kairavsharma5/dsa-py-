nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]
nums=[]
i,j=0,0
n,m=len(nums1),len(nums2)
while (i<n and j<m):
    if nums1[i]<nums2[j]:
        if (len(nums)==0 or nums[-1]!=nums1[i]):
            nums.append(nums1[i])
        i+=1
        
    else :
        if (len(nums)==0 or nums[-1]!=nums2[j]):
            nums.append(nums2[j])
        j+=1
while (i<n):
    if (len(nums)==0 or nums[-1]!=nums1[i]):
                nums.append(nums1[i])
    i+=1
while(j<m):
    if (len(nums)==0 or nums[-1]!=nums2[j]):
                nums.append(nums2[j])
    j+=1
print(nums)

