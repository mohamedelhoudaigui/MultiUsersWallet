async function deploy(cName, P1)
{
	const C = await ethers.getContractFactory(cName);
	console.log("Deploying ", cName, "...");
	const c = await C.deploy(P1);
	await c.waitForDeployment();
	console.log(cName + " deployed to: ", await c.getAddress());
}


async function main()
{
	let	MaxApprovals = 2;
	await deploy("MultiUserWallet", MaxApprovals)
}
  
main()
.then(() => process.exit(0))
.catch((error) => {
	console.error(error);
	process.exit(1);
});