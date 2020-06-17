#Partition Equal Subset Sum-Leetcode
def equal_partition(S,arr,n):
    if(S%2!=0):
        return False
    else:
        return subsetSum(S//2,arr,n)
def subsetSum(S, arr, n): 
    K = [[0 for x in range(S+ 1)] for x in range(n + 1)] 
    
    for i in range(n + 1): 
        for j in range(S + 1): 
            if j == 0:
                K[i][j] = True
            elif i==0:
                K[i][j]=False

            elif arr[i-1] <= j: 
                K[i][j] =K[i-1][j-arr[i-1]] or  K[i-1][j]
            else: 
                K[i][j] = K[i-1][j] 
  
    return K[n][S]
  
arr=[1,2,3,5]
n=len(arr)
S=sum(arr)
print(equal_partition(S,arr,n)) 