# DevRel Assessment Project

The purpose of this project is to create a smart contact and modify the AlgoKit default "hello_world" project to save data to the contract's box storage. The project was created using AlgoKit and the only files modified are linked below. The [deploy_config.py](/smart_contracts/hello_world/deploy_config.py) file operates on the following steps:

1. Deploy the smart contract defined in [contract.py](/smart_contracts/hello_world/contract.py).
2. Send a transaction to fund the contract account (a minimum balance is required to utilize box storage).
3. Call the **hello** method of the smart contract with a user's name as a variable. The method concatenates the user's name to *Hello, {name}* then creates an app call transaction to save the data to the contract's box storage.

This project was completed on LocalNet and TestNet. Below are screenshots of the LocalNet transactions, and immediately following are links to the TestNet transactions.

# LocalNet Results
*Note: To simply show that only four transactions were conducted (the first being the funding of the deployer wallet), the LocalNet sandbox was reset to show the results as blocks 2, 3 and 4.*

### Transaction block 2 (Deploy contract)

![Deploy contract screenshot](/images/localnet_app_init.png)

### Transaction block 3 (Fund contract account)

![Fund contact account screenshot](/images/localnet_app_funding.png)

### Transaction block 4 (Application Call to Update Box Storage)

![Application call screenshot](/images/localnet_app_call.png)

### Application Final Status

![Application final status screenshot](/images/localnet_app_status.png)

![Application final box storage](/images/localnet_app_box_storage.png)

# TestNet Results

After acquiring TestNet funds and deploying to TestNet, the results can be seen as successful. Below are the Lora links to transactions.

1. [Link to contract deployment transaction](https://lora.algokit.io/testnet/transaction/A7EQB3LFECUJ446QK3XWN4WHJF6RV6M3JAVG75JGQKFKKV3JHNBA)
2. [Link to contract funding transaction](https://lora.algokit.io/testnet/transaction/26OWK4JJBS3ZRBA3KPZ4ENJYCDULMYG3VN6LCRKKDRWEDCXW7ZTQ)
3. [Link to application call transaction](https://lora.algokit.io/testnet/transaction/USEZAZSPFSTTDSSTFD3YO7LXBLM7SGGTZPNN56OUZTPFJGBVF5LA)
4. [Link to application (for viewing box storage)](https://lora.algokit.io/testnet/application/732459352)


![TestNet final box storage](/images/testnet_app_box_storage.png)

# Conclusion
This results of the project were a success on both LocalNet and TestNet. This was a fun project and I really enjoyed diving into it.