const { expect } = require("chai");
const { ethers } = require("hardhat");


//cheetsheet:

// // Equality
// expect(value).to.equal(expectedValue);
// expect(value).to.be.true;
// expect(value).to.be.false;

// // Numbers
// expect(number).to.be.gt(5);  // greater than
// expect(number).to.be.gte(5); // greater than or equal
// expect(number).to.be.lt(10); // less than
// expect(number).to.be.lte(10);// less than or equal

// // Big Numbers (for ethers.js)
// expect(bigNum).to.equal(ethers.utils.parseEther("1.0"));

// // Arrays
// expect(array).to.have.lengthOf(3);
// expect(array).to.include(item);

// // Objects
// expect(object).to.have.property("key");

// // get signer balance:
// const balance1 = await ethers.provider.getBalance(owner.address);
// // Format it to ETH for readability
// console.log("Balance in ETH:", ethers.formatEther(balance1));

describe("Multi User Wallet Test", function ()
{
    let wallet_factory;
    let wallet_user;
    let approving_req = 2;

    beforeEach(async function ()
    {
        // Get the ContractFactory and Signers

        [owner , adr1, adr2] = await ethers.getSigners(); 
        wallet_factory = await ethers.getContractFactory("MultiUserWallet");
        wallet_user = await wallet_factory.deploy(approving_req);
        await wallet_user.waitForDeployment();
    
    });


    it("Should assign a user", async function () {
        await wallet_user.AddUser(adr1)
        const res = await wallet_user.IsUser(owner)
        expect(res).to.be.true
        const res1 = await wallet_user.IsUser(adr1)
        expect(res1).to.be.true
        const res2 = await wallet_user.IsUser(adr2)
        expect(res2).to.be.false
    });

    it("Should submit transaction", async function()
    {
        const T = {
            to: adr1.address,
            value: ethers.parseEther("1.0"),
            data: "0x",
        }

        await expect(wallet_user.SubmitTransaction(T.to, T.value, T.data))
        .to.emit(wallet_user, "TransactionCreated")
        .withArgs(1, owner.address, T.to, T.value)
        .and.to.emit(wallet_user, "TransactionApproved")
        .withArgs(1, owner.address)
    });

    it("Should get transaction", async function()
    {
        const T = {
            to: adr1.address,
            value: ethers.parseEther("1.0"),
            data: "0x",
        }

        await wallet_user.SubmitTransaction(T.to, T.value, T.data)
        const R = await wallet_user.GetTransaction(1)

        expect(R.to).to.equal(T.to)
        expect(R.from).to.equal(owner.address)
        expect(R.value).to.equal(T.value)
        expect(R.data).to.equal(T.data)
        expect(R.executed).to.equal(false)
        expect(R.approvals).to.equal(0)
    });

    it("Should approve transaction", async function ()
    {
        const T = {
            to: adr1.address,
            value: ethers.parseEther("1.0"),
            data: "0x",
        }
        await wallet_user.AddUser(adr1)
        await wallet_user.AddUser(adr2)

        await wallet_user.SubmitTransaction(T.to, T.value, T.data)
        await expect(wallet_user.connect(adr1).ApproveTransaction(1))
        .to.emit(wallet_user, "TransactionApproved")
        .withArgs(1, adr1.address)

        await expect(wallet_user.connect(adr2).ApproveTransaction(1))
        .to.emit(wallet_user, "TransactionApproved")
        .withArgs(1, adr2.address)
    });

    it("Should execute transaction", async function()
    {
        const T = {
            to: adr1.address,
            value: ethers.parseEther("1.0"),
            data: "0x",
        }
        
        // Fund the wallet contract first
        await owner.sendTransaction({
            to: wallet_user.getAddress(), // or wallet_user.address in some versions
            value: ethers.parseEther("1.1")  // Send more than needed to cover the transaction
        });
        
        await wallet_user.AddUser(adr1)
        await wallet_user.AddUser(adr2)
        await wallet_user.SubmitTransaction(T.to, T.value, T.data)
        await wallet_user.connect(adr1).ApproveTransaction(1)
        await wallet_user.connect(adr2).ApproveTransaction(1)
        
        await expect(wallet_user.ExecuteTransaction(1))
        .to.emit(wallet_user, "TransactionExecuted")
        .withArgs(1)
    });
    
});
