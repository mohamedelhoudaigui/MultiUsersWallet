from web3 import Web3
from solcx import install_solc

from scripts.interact import ContractInteractor
from scripts.compile import compile_solidity, get_contract_data
from scripts.deploy import deploy_contract


RPC_URL = 'http://localnet:8545'
CONTRACT_NAME = 'MultiUserWallet'
INTERFACE_NAME = 'IMultiUserWallet'
WALLET_SOL_PATH = './contracts/MultiUserWallet.sol'
IWALLET_SOL_PATH = './contracts/IMultiUserWallet.sol'
WALLET_JSON_PATH = './compiled_sol/MultiUserWallet.json'
IWALLET_JSON_PATH = './compiled_sol/IMultiUserWallet.json'
MAX_APPROVALS = 3


def compile_and_deploy(provider):
    install_solc('0.8.20')
    w = compile_solidity(WALLET_SOL_PATH, INTERFACE_NAME)
    Iw = compile_solidity(IWALLET_SOL_PATH, CONTRACT_NAME)
    abi_byte_code = get_contract_data(w, CONTRACT_NAME, WALLET_SOL_PATH)
    address = deploy_contract(abi_byte_code, provider, MAX_APPROVALS)
    return address



def init():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    print(f"Connected: {w3.is_connected()}")
    address = compile_and_deploy(w3)
    print(address)
    