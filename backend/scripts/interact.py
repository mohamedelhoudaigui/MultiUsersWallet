# scripts/interact.py
from web3 import Web3
import json

class ContractInteractor:
    def __init__(self, contract_address):
        self.w3 = Web3(Web3.HTTPProvider('YOUR_RPC_URL'))
        
        # Load ABI
        with open('contracts/build/YourContract.json', 'r') as f:
            contract_json = json.load(f)
        contract_abi = contract_json['abi']
        
        # Create contract instance
        self.contract = self.w3.eth.contract(
            address=contract_address,
            abi=contract_abi
        )
    
    def is_user(self, address):
        return self.contract.functions.IsUser(address).call()
    
    def add_user(self, user_address):
        account = self.w3.eth.accounts[0]
        tx_hash = self.contract.functions.addUser(user_address).transact({
            'from': account
        })
        return self.w3.eth.wait_for_transaction_receipt(tx_hash)