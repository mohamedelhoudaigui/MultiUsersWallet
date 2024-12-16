from web3 import Web3
from solcx import install_solc

from scripts.interact import ContractInteractor
from scripts.compile import compile_solidity, get_contract_data
from scripts.deploy import deploy_contract
from scripts.interact import ContractInteractor


RPC_URL = 'http://localnet:8545'
CONTRACT_NAME = 'MultiUserWallet'
SOL_PATH = './contracts/'
SOLIDITY_VERSION = '0.8.20'
MAX_APPROVALS = 3



def compile_and_deploy(provider):
    install_solc(version=SOLIDITY_VERSION)
    compiled = compile_solidity(SOL_PATH, SOLIDITY_VERSION)
    abi, bytecode = get_contract_data(compiled, CONTRACT_NAME)
    address = deploy_contract(abi, bytecode, provider, MAX_APPROVALS)
    interactor = ContractInteractor(address, abi, provider)
    return interactor


def init():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    print(f"Connected: {w3.is_connected()}")
    interactor = compile_and_deploy(w3)
    return interactor