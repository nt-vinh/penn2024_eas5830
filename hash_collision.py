import hashlib
import os
import random
import string

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    collision_not_found = True
    while collision_not_found:
        x_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))
        y_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))
        #
        if not(x_str == y_str):
            x = x_str.encode('utf-8')
            y = y_str.encode('utf-8')
            #
            x_hash = hashlib.sha256(x).hexdigest()
            y_hash = hashlib.sha256(y).hexdigest()
            #
            x_bits = "{0:256b}".format(int(x_hash, 16)) 
            y_bits = "{0:256b}".format(int(y_hash, 16)) 
            #
            if x_bits[-k:] == y_bits[-k:]:
                collision_not_found = False
    return( x, y )