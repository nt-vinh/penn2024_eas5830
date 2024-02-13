from web3 import Web3
from web3.contract import Contract
from web3.providers.rpc import HTTPProvider
import requests
import json
import time

bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
contract_address = Web3.toChecksumAddress(bayc_address)

#You will need the ABI to connect to the contract
#The file 'abi.json' has the ABI for the bored ape contract
#In general, you can get contract ABIs from etherscan
#https://api.etherscan.io/api?module=contract&action=getabi&address=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D
with open('/home/codio/workspace/abi.json', 'r') as f:
	abi = json.load(f) 

############################
#Connect to an Ethereum node
api_url = 'https://mainnet.infura.io/v3/97d5ebed0b714ef7b442181913944a21' #YOU WILL NEED TO TO PROVIDE THE URL OF AN ETHEREUM NODE
provider = HTTPProvider(api_url)
web3 = Web3(provider)

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	data = requests.get('https://gateway.pinata.cloud/ipfs/'+cid)
	data = json.loads(data.text)
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data

def get_ape_info(apeID):
	assert isinstance(apeID,int), f"{apeID} is not an int"
	assert 1 <= apeID, f"{apeID} must be at least 1"

	contract = web3.eth.contract(address='0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D',abi=abi)
	owner    = contract.functions.ownerOf(apeID).call()
	image    = contract.functions.tokenURI(apeID).call()
	#
	ipfs     = get_from_ipfs(image[7:]) # 7 because this removes 'ipfs://'
	for temp in ipfs['attributes']:
		if temp['trait_type'] == 'Eyes':
			eyes = temp['value']
	#YOUR CODE HERE	
	data = {'owner': owner, 'image': image, 'eyes': eyes}	

	assert isinstance(data,dict), f'get_ape_info{apeID} should return a dict' 
	assert all( [a in data.keys() for a in ['owner','image','eyes']] ), f"return value should include the keys 'owner','image' and 'eyes'"
	return data

