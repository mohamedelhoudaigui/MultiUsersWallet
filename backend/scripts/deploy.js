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


async function deploy_wallet(MaxApprovals)
{
	return await deploy("MultiUserWallet", MaxApprovals)
}


module.exports = { deploy_wallet }