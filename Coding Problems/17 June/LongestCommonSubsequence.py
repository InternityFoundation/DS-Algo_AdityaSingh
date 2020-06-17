#Longest Common Subsequence-Leetcode
def lcs(a,b):
    K=[[0 for i in range(m+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0):
                K[i][j]=0
            elif(a[i-1]==b[j-1]):
                K[i][j]=1+K[i-1][j-1]
            else:
                K[i][j]=max(K[i-1][j],K[i][j-1])
    return K[n][m]

a=input()
b=input()
n=len(a)
m=len(b)
print(lcs(a,b))   