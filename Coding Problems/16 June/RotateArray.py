#Rotate Array-Leetcode

arr=[int(i) for i in input().split()]
k=int(input())
n=len(arr)
a=[0]*n
for i in range(n):
    a[(i+k)%n]=arr[i]
print(a)