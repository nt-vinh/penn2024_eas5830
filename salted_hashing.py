import hashlib
import os
import string
import random

def myhash(m):
    #Generate random nonce
    # nonce = 'my_random_nonce'
    nonce = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=len(m)))
    #Generate hex digest
    h_hex = hashlib.sha256((nonce + m).encode('utf-16')).hexdigest()
    return nonce, h_hex



