# make public key
import random
import fractions

def mod_exp(a,d,n):
    if d == 1:
        return a
    res = (a*a)%n
    if d%2 == 1:
        return (mod_exp(res,d/2,n)*a)%n
    else:
        return (mod_exp(res,d/2,n))%n
        
def d_make(n):
    while(1):
        d = random.randint(2,n)
        if(fractions.gcd(d,n) == 1):
            return d
            
def expand_gcd(d,n):
    # supposed d<n
    if d == 1:
        return (1,0)
    r = n/d
    s = n%d
    (a,b) = expand_gcd(s,d)
    # 1 = as + bd = a(n-rd) + bd = an + (b-ar)d
    return (b-a*r,a)
        
def key_make(p,q):
    n = p*q
    print "n="
    print n
    fi_n = (p-1)*(q-1)
    
    d = d_make(fi_n)
    print "d="
    print d
    
    (e,ed_rest) = expand_gcd(d,fi_n)
    e = e%fi_n
    print "e="
    print e
    
    print "e*d mod fi_n = "
    print (e*d)%fi_n
        
        
        
        
p = 11260863207212702103460474093002595541449751697925862895654841505993756717287186060653826108669131114554096873072576118014083178999905221008214722001943339
q = 10057860828989564052637278955977000644334785958542967421198451589491463097151456183670351992389841894659540570390117889232610166686311055148114238796103417

key_make(p,q)
