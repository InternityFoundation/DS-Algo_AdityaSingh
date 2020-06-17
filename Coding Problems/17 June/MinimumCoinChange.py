#Longest Plindromic Substring-Leetcode
def LPS(a):
    return lcs(a,a[::-1])
def lcs(a,b):
    K=[[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if(i==0 or j==0):
                K[i][j]=0
            elif(a[i-1]==b[j-1]):
                K[i][j]=1+K[i-1][j-1]
            else:
                K[i][j]=max(K[i-1][j],K[i][j-1])
    return K[n][n]

a=input()
n=len(a) 
print(LPS(a))