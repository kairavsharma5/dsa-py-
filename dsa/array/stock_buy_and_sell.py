prices=[7,2,1,5,6,4,8]
maxi=0
mini=float("inf")
n=len(prices)
'''
for i in range(0,n-1):
    for j in range(i+1,n):
        if prices[j]>prices[i]:
            profit=prices[j]-prices[i]
            maxi=max(maxi,profit)
print(maxi)'''

for i in range(0,n):
    if mini>prices[i]:
        mini=prices[i]
    maxi=max(maxi,prices[i]-mini)
print(maxi)