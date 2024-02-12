import hashlib
import os

def myhash(m):
    #Generate random nonce
    nonce = 'my_random_nonce'
    #Generate hex digest
    h_hex = hashlib.sha256((nonce + m).encode('utf-16')).hexdigest()
    return nonce, h_hex



