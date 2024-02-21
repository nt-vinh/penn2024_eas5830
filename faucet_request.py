#!/usr/bin/env python3
"""
Please complete the following fields and run the student tests to verify
that you are ready to make a faucet request and the faucet is online

Once you have successfully completed the "run tests" you can submit this
assignment to have funds transferred to your account. This assignment
does not count towards your grade, and you only have to complete it if
you want an AVAX or BNB funds "drip" from the course account.

***NOTE***
Please keep the account and private key somewhere safe so that you can
reuse this account for future assignments that require you to use a
"funded" account.

***Please do not use an account that you use for real funds.***
"""

# Do you need an account? (True or False)
create_account = False

# If you have an account you want to use make sure 'create_account' is False,
# complete the following fields and 'run tests' again to verify the information
name = 'Thanh Vinh Nguyen'  # Your name
e_mail = 'nvinh@seas.upenn.edu'  # this should be your e-mail in ed-stem
account = '0x628b4AbA6aCD618FD15f832f8825D1BFa4b0B42e'  # The account you want the funds in
secret_key = '5c629f325a45701aa221bdd491d9ff48c0cb84c8a01a534090b0cf7af9fd0a62'  # The secret key for your account

# Networks you want funding from (True or False)
AVAX = True
BNB = True

'''
# For your personal use, the entirety of the account creation code is included here

import eth_account
import secrets
 
def create_account():
    private_key = "0x" + secrets.token_hex(32)
    acct = eth_account.Account.from_key(private_key)

    print(f"Below is your new account information!\n\nAddress:     {acct.address}"
          f"\nPrivate key: {private_key}\n\nSave this keypair so that you can "
          f"complete the faucet request,\nand use this account in upcoming "
          f"assignments.\n\nAlso, you can view your new account on the AVAX "
          f"block explorer at:\nhttps://testnet.snowtrace.io/address/{acct.address}\n")
    
'''