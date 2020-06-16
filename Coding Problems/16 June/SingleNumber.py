#Single Number-Leetcode

a=[int(i) for i in input().split()]
ans=a[0]
for i in a[1:]:
    ans=ans^i
print(ans)
