#Product of array except number itself - Leetcode

#We find product of elements to left of it and product of elements to right of it to get the product of array except itself
a=[int(i) for i in input().split()]
n=len(a)
left,right=[0]*n,[0]*n
left[0]=1
right[n-1]=1
for i in range(1,n):
    left[i]=left[i-1]*a[i-1]
for i in range(n-2,-1,-1):
    right[i]=right[i+1]*a[i+1]
for i in range(n):
    print(left[i]*right[i],end=' ')