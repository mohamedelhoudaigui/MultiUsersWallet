# tests/test_contract.py
import pytest
from scripts.interact import ContractInteractor

@pytest.fixture
def contract():
    return ContractInteractor('YOUR_CONTRACT_ADDRESS')

def test_is_user(contract):
    address = '0x...'  # Test address
    result = contract.is_user(address)
    assert isinstance(result, bool)

def test_add_user(contract):
    address = '0x...'  # Test address
    tx_receipt = contract.add_user(address)
    assert tx_receipt['status'] == 1