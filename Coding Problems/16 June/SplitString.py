#Split a String in Balanced Strings-Leetcode

a=input()
c=0
ans=0
for i in a:
    if(i=='R'):
        c+=1
    else:
        c-=1
    if(c==0):
        ans+=1
print(ans)
