from web3 import Web3
import random
import json


rpc_url = "https://mainnet.infura.io/v3/97d5ebed0b714ef7b442181913944a21" #Set this to a node that you can connect to (e.g. an Alchemy node)
w3 = Web3(Web3.HTTPProvider(rpc_url))

if w3.is_connected():
	pass
else:
	print( "Failed to connect to Ethereum node!" )


"""
	Takes a block number
	Returns a boolean that tells whether all the transactions in the block are ordered by priority fee

	Before EIP-1559, a block is ordered if and only if all transactions are sorted in decreasing order of the gasPrice field

	After EIP-1559, there are two types of transactions
		*Type 0* The priority fee is tx.gasPrice - block.baseFeePerGas
		*Type 2* The priority fee is min( tx.maxPriorityFeePerGas, tx.maxFeePerGas - block.baseFeePerGas )

	Conveniently, most type 2 transactions set the gasPrice field to be min( tx.maxPriorityFeePerGas + block.baseFeePerGas, tx.maxFeePerGas )
"""
def is_ordered_block(block_num):
    block = w3.eth.get_block(block_num)
    ordered = True
       
    #YOUR CODE HERE
    num_transactions = len(block.transactions)
    if num_transactions > 1:
        for i in range(num_transactions-1):
            current_tx    = w3.eth.get_transaction(block.transactions[i])
            current_priority = current_tx.gasPrice
	    
            next_tx       = w3.eth.get_transaction(block.transactions[i+1])
            next_priority = next_tx.gasPrice
            if next_priority > current_priority:
                ordered = False
                break
            #
    return ordered

"""
	This might be useful for testing
"""
if __name__ == "__main__":
	latest_block = w3.eth.get_block_number()

	london_hard_fork_block_num = 12965000
	assert latest_block > london_hard_fork_block_num, f"Error: the chain never got past the London Hard Fork"

	n = 5

	for _ in range(n):
        #Pre-London
		block_num = random.randint(1,london_hard_fork_block_num-1)
		ordered = is_ordered_block(block_num)
		if ordered:
			print( f"Block {block_num} is ordered" )
		else:
			print( f"Block {block_num} is ordered" )

        #Post-London
		block_num = random.randint(london_hard_fork_block_num,latest_block)
		ordered = is_ordered_block(block_num)
		if ordered:
			print( f"Block {block_num} is ordered" )
		else:
			print( f"Block {block_num} is ordered" )

