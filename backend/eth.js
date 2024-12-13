const   { Web3 } = require('web3')
const   { deploy_contract } = require('./scripts/deploy.js')
const   fs = require('fs');

const   contract_name = "MultiUserWallet"
const   MaxApprovals = 3
const   web3 = new Web3("http://localnet:8545/") 


function extract_abi()
{
    const contractJSON = './artifacts/contracts/' + contract_name + '.sol/' + contract_name + '.json';
    const data = JSON.parse(fs.readFileSync(contractJSON, 'utf8'));
    const abi = data.abi;
    return abi
}

async function init()
{
    web3.eth.getBlockNumber()
    .then((blockNumber) => console.log('Connected! Block number:', blockNumber))
    .catch((error) => console.error('Error connecting to node:', error))

    const addr = await deploy_contract(contract_name, MaxApprovals)
    const abi = extract_abi()
    const contract = new web3.eth.Contract(abi, addr);
    if (!web3.utils.isAddress(addr)) {
        console.error("Invalid contract address!");
    } else {
        console.log("Contract address is valid.");
    }
    if (contract.methods && typeof contract.methods.GetTransaction === 'function') {
        console.log("Contract instance is valid and has the expected methods.");
    } else {
        console.error("Contract instance does not have the expected methods.");
    }
    
}



module.exports =  { init }

