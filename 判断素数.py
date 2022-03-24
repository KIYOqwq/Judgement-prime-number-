
import math
#输入一个整数n
n =  int(input())

def prime(n):
    if n==1:
        return bool(0)
    else:
        for i in range(2,int(math.sqrt(n))+1): #math.sqrt返回n的平方根
            if n%i==0:
                return bool(0)
                break
            else:
                i=i+1

        return bool(1)

#是素数则返回1 不是则返回0
print(prime(n))
