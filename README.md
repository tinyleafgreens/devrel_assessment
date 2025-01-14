# DevRel Assessment Project

The purpose of this project is to create a smart contact and modify the "hello_world" method to save a string to box storage. The project was created using Algokit and the only files modified are highlighted below. The [deploy_config.py](/smart_contracts/hello_world/deploy_config.py) file operates on the following steps:

1. Deploy the smart contract defined in [contract.py](/smart_contracts/hello_world/contract.py)
2. Send a transaction to fund the contract account (a minimum balance is required to utilize box storage)
3. Call the hello method of the smart contract with a user's name as a variable. The method concatenates the user's name to say "Hello, {name}" and creates an app call transaction to save the string to the contract's box storage.

This project was completed on Localnet and Testnet. Below are screenshots to the Localnet transactions, and immediately following are links to the Testnet transactions.

# Localnet Results
Note: To simply show that only three transactions were conducted (the first is the funding of the deployer wallet), the localnet sandbox was reset to show as rounds 2, 3 and 4.

### Transaction round 2 (Deploy contract)

![Deploy contract screenshot](/images/localnet_app_init.png)

### Transaction round 3 (Fund contract account)

![Fund contact account screenshot](/images/localnet_app_funding.png)

### Transaction round 4 (Application Call to Update Box Storage)

![Application call screenshot](/images/localnet_app_call.png)

### Application Final Status

![Application final status screenshot](/images/localnet_app_status.png)

![Application final box storage](/images/localnet_app_box_storage.png)

# Testnet Results