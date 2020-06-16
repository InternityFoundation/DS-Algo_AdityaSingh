#Hamming Distance- Leetcode
# We need to find corrresponding set bits in two numbers which are different

a,b=[int(i) for i in input().split()]
c=a^b #By doing xor of the two numbers we will get 1 corresponding to those bits which are different
def countsetbits(n):
    count=0
    while(n):
        count+=n&1 # Check last bit
        n>>=1 #Right shift number by 1 
    return count
print(countsetbits(c))
