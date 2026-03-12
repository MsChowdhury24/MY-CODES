def power(x,n):
    if n==0:
        return 1
    a = pow(x,n//2)
    if n%2==0:
        return a*a
    else :
        return a*a*x        
def my_pow(x,n):    
    if n>=0:
        return power(x,n)
        print(power(2,-10))
    else:
        return 1/power(x,n*(-1))
print(my_pow(2,-10))       


