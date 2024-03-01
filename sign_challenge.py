import eth_account

def sign_challenge(challenge):
    """
        Takes a challenge (string)
        Returns addr, sig
        where addr is an ethereum address (in hex)
        and sig is a signature (in hex)
    """

    ####
    #YOUR CODE HERE
    ####

    # w3 = Web3()

    #This is the only line you need to modify
    sk = "5c629f325a45701aa221bdd491d9ff48c0cb84c8a01a534090b0cf7af9fd0a62"

    acct = eth_account.Account.from_key(sk)
    challenge = eth_account.messages.encode_defunct(text = challenge)

    signed_message = eth_account.Account.sign_message( challenge, private_key = acct._private_key )
    
    return acct.address, signed_message.signature.hex()

    # return addr, sig


if __name__ == "__main__":
    """
        This may help you test the signing functionality of your code
    """
    import random 
    import string

    letters = string.ascii_letters
    challenge = ''.join(random.choice(string.ascii_letters) for i in range(32)) 

    addr, sig = sign_challenge(challenge)

    eth_encoded_msg = eth_account.messages.encode_defunct(text=challenge)

    if eth_account.Account.recover_message(eth_encoded_msg,signature=sig) == addr:
        print( f"Success: signed the challenge {challenge} using address {addr}!")
    else:
        print( f"Failure: The signature does not verify!" )
        print( f"signature = {sig}" )
        print( f"address = {addr}" )
        print( f"challenge = {challenge}" )

