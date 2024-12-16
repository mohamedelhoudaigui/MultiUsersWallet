from web3 import Web3

class ContractInteractor:
    def __init__(self, contract_address, contract_abi , provider):
        self.w3 = provider
        
        # Create contract instance
        self.contract = self.w3.eth.contract(
            address=contract_address,
            abi=contract_abi
        )
        print('interactor is ready...')
    # implement the contract interface:
    
    def is_user(self, address):
        try:
            res = self.contract.functions.IsUser(address).call()
            return res
        except Exception as e:
            raise

    def add_user(self, address):
        try:
            res = self.contract.functions.AddUser(address).call()
            return res
        except Exception as e:
            raise
    
    
    def get_transaction(self, id):
        try:
            res = self.contract.functions.GetTransaction(id).call()
            return res
        except Exception as e:
            raise

    