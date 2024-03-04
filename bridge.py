from web3 import Web3
from web3.contract import Contract
from web3.providers.rpc import HTTPProvider
from web3.middleware import geth_poa_middleware #Necessary for POA chains
import json
import sys
from pathlib import Path

source_chain = 'avax'
destination_chain = 'bsc'
contract_info = "contract_info.json"

def connectTo(chain):
    if chain == 'avax':
        api_url = f"https://api.avax-test.network/ext/bc/C/rpc" #AVAX C-chain testnet

    if chain == 'bsc':
        api_url = f"https://data-seed-prebsc-1-s1.binance.org:8545/" #BSC testnet

    if chain in ['avax','bsc']:
        w3 = Web3(Web3.HTTPProvider(api_url))
        # inject the poa compatibility middleware to the innermost layer
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return w3

def getContractInfo(chain):
    """
        Load the contract_info file into a dictinary
        This function is used by the autograder and will likely be useful to you
    """
    p = Path(__file__).with_name(contract_info)
    try:
        with p.open('r')  as f:
            contracts = json.load(f)
    except Exception as e:
        print( "Failed to read contract info" )
        print( "Please contact your instructor" )
        print( e )
        sys.exit(1)

    return contracts[chain]

my_address      = '0x628b4AbA6aCD618FD15f832f8825D1BFa4b0B42e'
w3_avax         = connectTo(source_chain)
source_info     = getContractInfo('source')
source_contract = w3_avax.eth.contract(address='0x3d99e142ad1b96Bf84A800077950548908feB570', abi=source_info['abi'])
#
w3_bsc            = connectTo(destination_chain)
destination_info  = getContractInfo('destination')
destination_contract = w3_bsc.eth.contract(address='0x9bd2d4F5B3462cB5b2a354Aa2d92788d718a750d', abi=destination_info['abi'])      
#
source_contract.functions.registerToken('0xc677c31AD31F73A5290f5ef067F8CEF8d301e45c').build_transaction({'from': my_address, 
                                                                                                 'gasPrice': w3_avax.eth.gas_price, 
                                                                                                 'nonce': w3_avax.eth.get_transaction_count(my_address), 
                                                                                                 'gas': 5 * (10 ** 6)})
destination_contract.functions.createToken('0xc677c31AD31F73A5290f5ef067F8CEF8d301e45c','test_token_1','tt1').build_transaction({'from': my_address, 
                                                                                                 'gasPrice': w3_bsc.eth.gas_price, 
                                                                                                 'nonce': w3_bsc.eth.get_transaction_count(my_address), 
                                                                                                 'gas': 5 * (10 ** 6)})
source_contract.functions.registerToken('0x0773b81e0524447784CcE1F3808fed6AaA156eC8').build_transaction({'from': my_address, 
                                                                                                 'gasPrice': w3_avax.eth.gas_price, 
                                                                                                 'nonce': w3_avax.eth.get_transaction_count(my_address), 
                                                                                                 'gas': 5 * (10 ** 6)})
destination_contract.functions.createToken('0x0773b81e0524447784CcE1F3808fed6AaA156eC8','test_token_2','tt2').build_transaction({'from': my_address, 
                                                                                                                           'gasPrice': w3_bsc.eth.gas_price, 
                                                                                                                           'nonce': w3_bsc.eth.get_transaction_count(my_address), 
                                                                                                                           'gas': 5 * (10 ** 6)})

def scanBlocks(chain):
    """
        chain - (string) should be either "source" or "destination"
        Scan the last 5 blocks of the source and destination chains
        Look for 'Deposit' events on the source chain and 'Unwrap' events on the destination chain
        When Deposit events are found on the source chain, call the 'wrap' function the destination chain
        When Unwrap events are found on the destination chain, call the 'withdraw' function on the source chain
    """

    if chain not in ['source','destination']:
        print( f"Invalid chain: {chain}" )
        return None
    else:
        if chain == 'source':
            arg_filter = {}
            end_block = w3_avax.eth.get_block_number()
            event_filter = source_contract.events.Deposit.create_filter(fromBlock=end_block-5,toBlock=end_block,argument_filters=arg_filter)
            events = event_filter.get_all_entries()
            for evt in events:
                destination_contract.functions.wrap(evt.args['token'],evt.args['recipient'],evt.args['amount']).build_transaction({'from': my_address, 
                                                                                                                                   'gasPrice': w3_bsc.eth.gas_price, 
                                                                                                                                   'nonce': w3_bsc.eth.get_transaction_count(my_address), 
                                                                                                                                   'gas': 5 * (10 ** 6)})
        else:
            arg_filter = {}
            end_block = w3_bsc.eth.get_block_number()
            event_filter = destination_contract.events.Unwrap.create_filter(fromBlock=end_block-5,toBlock=end_block,argument_filters=arg_filter)
            events = event_filter.get_all_entries()
            for evt in events:
                source_contract.functions.withdraw(evt.args['underlying_token'],evt.args['to'],evt.args['amount']).build_transaction({'from': my_address, 
                                                                                                                                      'gasPrice': w3_avax.eth.gas_price, 
                                                                                                                                      'nonce': w3_avax.eth.get_transaction_count(my_address), 
                                                                                                                                      'gas': 5 * (10 ** 6)})