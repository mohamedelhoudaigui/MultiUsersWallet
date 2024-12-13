const { ethers } = require('hardhat');

async function deploy(cName, P1)
{
	const C = await ethers.getContractFactory(cName);
	console.log("Deploying ", cName, "...");
	const c = await C.deploy(P1);
	await c.waitForDeployment();
	console.log(cName + " deployed to: ", await c.getAddress());
	return await c.getAddress()
}


async function deploy_contract(name, params)
{
	return await deploy("MultiUserWallet", params)
}


module.exports = { deploy_contract }