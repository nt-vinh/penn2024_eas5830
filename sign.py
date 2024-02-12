import eth_account
from web3 import Web3
from eth_account.messages import encode_defunct


def sign(m):
    w3 = Web3()
    # create an eth account and recover the address (derived from the public key) and private key
    # your code here

    acc = w3.eth.account.create()

    eth_address = acc.address  # Eth account
    private_key = acc.key

    # generate signature
    # your code here

    message = encode_defunct(text = m)
    signed_message = w3.eth.account.signed_message(message, private_key=private_key)

    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

    return eth_address, signed_message
