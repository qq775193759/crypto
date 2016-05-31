import random

def mod_exp(a,d,n):
    if d == 1:
        return a
    res = (a*a)%n
    if d%2 == 1:
        return (mod_exp(res,d/2,n)*a)%n
    else:
        return (mod_exp(res,d/2,n))%n

def rand_uint(n):
    temp = random.randint(2**(n-1), 2**n)
    if temp%2 == 0:
        temp = temp + 1
    return temp
    
def decompose_n(n):
    d = n - 1
    r = 0
    while(d%2 == 0):
        d = d/2
        r = r + 1
    return d,r
    
def test_once(n,d,r):
    a = random.randint(2, n-2)
    #x = (a**d)%n
    x = mod_exp(a,d,n)
    if (x*x)%n == 1:
        return True
    for i in range(0,r-1):
        x = (x*x)%n
        if x==1:
            return False
        if x==(n-1):
            return True
    return False
    
def test(n):
    (d,r) = decompose_n(n)
    for i in range(0,100):
        if test_once(n,d,r):
            pass
        else:
            return False
    return True
        
    
def prime_make(lenth):
    #n = rand_uint(10)
    bo = False
    while(not bo):
        n = rand_uint(lenth)
        #print("%d"%(n))
        bo = test(n)
        #print bo
    return n
        

def pq_make():
    p = prime_make(512)
    q = prime_make(512)
    print p
    print q

    
pq_make()