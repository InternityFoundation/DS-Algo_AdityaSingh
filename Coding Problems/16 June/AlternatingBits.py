#Binary Number with Alternating Bits-Leetcode

n=int(input())
n=n^(n>>1)#By shifting number by 1 all bits will get flipped and by xoring number with number with flipped bits we will get all 1
n=n+1#If there is a number with all set bits then its next number will be a power of 2
if(n&n-1==0):#checking power of 2
    print('True')
else:
    print('False')

