import random

from params import p
from params import g

def keygen():
    sk = random.randint(1,p)
    pk = pow(g,sk,mod=p)
    return pk,sk

def encrypt(pk,m):
    r  = random.randint(1,p)
    c1 = pow(g,r,mod=p)
    c2 = (pow(pk, r, mod=p)*m)%p
    return [c1,c2]

def decrypt(sk,c):
    temp = pow(pow(c[0],sk,mod=p),-1,mod=p)
    m = (c[1]*temp)%p
    return m

