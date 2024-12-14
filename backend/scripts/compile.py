from solcx import compile_standard
import json

def compile_solidity(source_path, name):
    """
    Compile a Solidity source file and return the compilation output
    
    Args:
        source_path (str): Path to the .sol file
    
    Returns:
        dict: Compiled contract data
    """
    # Read the Solidity source code
    with open(source_path, 'r') as file:
        source_code = file.read()
    
    # Compile the contract
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {
                source_path: {
                    "content": source_code
                }
            },
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": [
                            "abi",
                            "metadata",
                            "evm.bytecode",
                            "evm.sourceMap"
                        ]
                    }
                }
            }
        },
        solc_version="0.8.20"
    )
    
    # Save the compilation output
    with open('./compiled_sol/' + name + '.json', 'w') as file:
        json.dump(compiled_sol, file)
    
    return compiled_sol

# Get contract binary and ABI
def get_contract_data(compiled_sol, contract_name, contract_path):
    """
    Extract contract bytecode and ABI from compiled data
    
    Args:
        compiled_sol (dict): Compiled contract data
        contract_name (str): Name of the contract
        source_path (str): Path to the source file
        
    Returns:
        tuple: (bytecode, abi)
    """
    # Get bytecode
    bytecode = compiled_sol['contracts'][contract_path][contract_name]['evm']['bytecode']['object']
    
    # Get ABI
    abi = compiled_sol['contracts'][contract_path][contract_name]['abi']
    
    return bytecode, abi