from web3 import Web3

def deploy_contract(abi, bytecode, provider, arg):
    try:
        provider.eth.default_account = provider.eth.accounts[0]
        # Create contract instance 
        Contract = provider.eth.contract(abi=abi, bytecode=bytecode)
        # Deploy with error handling
        tx_hash = Contract.constructor(arg).transact()
        # Wait for transaction receipt
        tx_receipt = provider.eth.wait_for_transaction_receipt(tx_hash)
        print(f'deployed successfully at : {tx_receipt.contractAddress}')
        return tx_receipt.contractAddress
    
    except Exception as e:
        print(f"Deployment error: {e}")