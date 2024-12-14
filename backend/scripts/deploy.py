from web3 import Web3

def deploy_contract(abi_byte_code, provider, arg):
    
    contract_bytecode = abi_byte_code[0]
    contract_abi = abi_byte_code[1]
    
    # Create contract instance using w3
    Contract = provider.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    
    # Get account
    account = provider.eth.accounts[0]
    
    # Deploy
    tx_hash = Contract.constructor(arg).transact({'from': account})
    tx_receipt = provider.eth.wait_for_transaction_receipt(tx_hash)
    
    return tx_receipt.contractAddress