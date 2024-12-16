// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IMultiUserWallet {

	struct	Transaction
	{
		address	from;         // Sender
		address	to;          // Recipient
		uint256	value;       // Amount in Wei
		bytes	data;          // Transaction data
		bool	executed;       // Execution status
		uint256	id;         // Transaction ID
		uint256	approvals;   // Number of approvals
		uint256	timestamp;   // When created
	}

	//events:
	event UserAdded(address indexed NewUser);
    event OwnershipTransferred(address indexed PreviousOwner, address indexed NewOwner);
    event TransactionCreated(uint256 indexed TxId, address indexed From, address indexed To, uint256 Value);
    event TransactionApproved(uint256 indexed TxId, address indexed Approver);
    event TransactionExecuted(uint256 indexed TxId);

	//user management :
	function	AddUser(address NewUser) external returns(bool);
	function	IsUser(address User) external view returns(bool);

	//transaction management:
	function	SubmitTransaction(address _to, uint256 _value, bytes memory _data) external;
	function	ApproveTransaction(uint256 TxId) external;
	function	ExecuteTransaction(uint256 TxId) external;

	//getters:
	function GetTransaction(uint256 TxId) external view
	returns (
		address from,
		address to,
		uint256 value,
		bytes memory data,
		bool executed,
		uint256 approvals,
		uint256 timestamp
	);
}