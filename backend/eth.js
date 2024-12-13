const { Web3 } = require('web3')
const { deploy_wallet } = require('./scripts/deploy.js')
const   MaxApprovals = 3;

let web3

async function init(url)
{
    web3 = new Web3(url);
    
    web3.eth.getBlockNumber()
    .then((blockNumber) => console.log('Connected! Block number:', blockNumber))
    .catch((error) => console.error('Error connecting to node:', error))

    const addr = await deploy_wallet(MaxApprovals);
    console.log(addr)
}



module.exports =  { init }

