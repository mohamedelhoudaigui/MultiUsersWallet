// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./IMultiUserWallet.sol";

contract	MultiUserWallet is IMultiUserWallet
{
	receive() external payable {}

	//state vars:
	uint private immutable							Req_Apprv;
	uint private									NC_Owners;
	uint private									T_Id;

	mapping (address => bool)						IsOwner;
	mapping (uint256 => Transaction)				Transactions;
	mapping (uint256 => mapping(address => bool))	ApprMap;

	// constructor:

	constructor (uint256 _Req_Apprv) IMultiUserWallet()
	{
		NC_Owners = 1;
		Req_Apprv = _Req_Apprv;
		T_Id = 1;
		IsOwner[msg.sender] = true;
	}


	//--------------modifiers:

	modifier	CheckAddress(address adr)
	{
		require(adr != address(0), "Invalid address");
		_;
	}

	modifier	CheckIsOwner()
	{
		require(IsOwner[msg.sender] == true, "Not a wallet owner");
		_;
	}

	modifier	CheckTransactionExist(uint256 Id)
	{
		require((Id < T_Id) && (Id > 0), "Transaction doesnt exist");
		_;
	}

	modifier	CheckApprovedBy(uint256 TxId, address User)
	{
		Transaction memory T = Transactions[TxId];
		require(!ApprMap[T.id][User], "User already approved");
		_;
	}

	modifier	CheckApproved(uint256 TxId)
	{
		Transaction memory T = Transactions[TxId];
		require(T.approvals >= Req_Apprv, "Transaction need more approves");
		_;
	}

	modifier	CheckExecuted(uint256 TxId)
	{
		Transaction memory T = Transactions[TxId];
		require(!T.executed, "Transaction already executed");
		_;
	}

	modifier	CheckExecBalance(uint256 TxId)
	{
		Transaction memory T = Transactions[TxId];
		require(address(this).balance >= T.value, "Insufficient balance");
		_;
	}

	//---------------interface:

	function	AddUser(address NewUser) external
		CheckIsOwner()
		CheckAddress(NewUser)
		override
	returns(bool)
	{
		if (IsOwner[NewUser] == true)
			return false;
		IsOwner[NewUser] = true;
		NC_Owners++;

		emit UserAdded(NewUser);
		return true;
	}

	function	IsUser(address User) external view
		CheckAddress(User)
		override
	returns (bool)
	{
		return (IsOwner[User]);
	}


	function	SubmitTransaction(address _to, uint256 _value, bytes memory _data) external
		CheckIsOwner()
		CheckAddress(_to)
		override
	{
		Transaction memory NewTransaction = Transaction({
			from: msg.sender,
			to: _to,
			value: _value,
			data: _data,
			executed: false,
			id: T_Id,
			approvals: 0,
			timestamp: block.timestamp
		});

		Transactions[T_Id] = NewTransaction;
		T_Id++;
		ApprMap[NewTransaction.id][msg.sender] = true;

		emit TransactionCreated(NewTransaction.id,
								NewTransaction.from,
								NewTransaction.to,
								NewTransaction.value);

		emit TransactionApproved(NewTransaction.id, msg.sender);
	}


	function	ApproveTransaction(uint256 TxId) external
		CheckIsOwner()
		CheckTransactionExist(TxId)
		CheckApprovedBy(TxId, msg.sender)
		CheckExecuted(TxId)
		override
	{
		Transaction storage T =  Transactions[TxId];
		T.approvals++;

		ApprMap[TxId][msg.sender] = true;

		emit TransactionApproved(T.id, msg.sender);
	}


	function	ExecuteTransaction(uint256 TxId) external
		CheckIsOwner()
		CheckTransactionExist(TxId)
		CheckApproved(TxId)
		CheckExecuted(TxId)
		CheckExecBalance(TxId)
		override
	{
		Transaction storage T =  Transactions[TxId];
		T.executed = true;
		(bool success, ) = T.to.call{value: T.value}(T.data);
    	require(success, "Transaction execution failed");

		emit TransactionExecuted(T.id);
	}

	function GetTransaction(uint256 TxId) external view
        CheckTransactionExist(TxId)
		override
	returns (
		address from,
		address to,
		uint256 value,
		bytes memory data,
		bool executed,
		uint256 approvals,
		uint256 timestamp
	)
    {
        Transaction storage T = Transactions[TxId];
        return (
            T.from,
            T.to,
            T.value,
            T.data,
            T.executed,
            T.approvals,
            T.timestamp
        );
	}

}