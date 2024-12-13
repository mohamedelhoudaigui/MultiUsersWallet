require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  paths: {
    sources: "./contracts",    // Solidity contract files inside "solidity/contracts"
    tests: "./test",           // Test files inside "solidity/test"
    artifacts: "./artifacts",           // Where compiled contracts will be stored
    cache: "./cache",                   // Where Hardhat will store the cache
    scripts: "./scripts",
  },
  networks: {
    localnet: {
      url: "localnet:8545"
    }
  }
};