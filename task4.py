from numbers import Integral


def sum_square(n):
    c=0
    for i in range (0,n+1):
        c=c+i**2
        i+=1
    return c 

x=int(input("the input number: \n"))
print("the sum sequence of x =",sum_square(x))
    
        
