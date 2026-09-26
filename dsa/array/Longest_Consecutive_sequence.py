#brute gave tle thats why its not here
nums=[1,99,101,98,2,5,3,90,100]
'''nums.sort()
count=0
last_small=float("-inf")
longest=0
for i in range(0,len(nums)):
    num=nums[i]
    if(num-1==last_small):
        count+=1
        last_small=num
    elif(num!=last_small):
        count=1
        last_small=num
    longest=max(longest,count)
print(longest)

'''

my_set=set()
for i in range(0,len(nums)):
    my_set.add(nums[i])
longest=0
for num in my_set:
    if num-1 not in my_set:
        count=1
        x=num
        while(x+1 in my_set):
            count+=1
            x+=1
        longest=max(longest,count)
print(longest)