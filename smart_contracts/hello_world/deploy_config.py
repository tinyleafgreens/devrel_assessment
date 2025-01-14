import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
from algosdk.transaction import PaymentTxn, wait_for_confirmation

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.hello_world.hello_world_client import (
        HelloWorldClient,
    )

    # Initialize Variables (My name, the box key and account fund amount)
    name = "Austin"  # My name
    box_key = b"FutureHireGreeting"  # Box key saved as bytes (with an optimistic key name)
    fund_amount = 150_000  # We will fund the account just above the minimum required to create the box

    # Initialize the app client
    app_client = HelloWorldClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client
    )

    # Deploy the contract
    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )

    # Here we will create the transation to fund the contract account with the minimum Algo needed
    funding_tx = PaymentTxn(
        sender=deployer.address,
        receiver=app_client.app_address,
        amt=fund_amount,
        sp=algod_client.suggested_params(),
    )

    # Here we will sign the transaction using deployer private key, submit the transaction, and wait for confirmation
    signed_tx = funding_tx.sign(deployer.private_key)
    txid = algod_client.send_transaction(signed_tx) 
    txn_result = wait_for_confirmation(algod_client, txid, 4) 
    
    # Confirm that the funding transaction went through. If not, log an error and do not proceed
    if not txn_result.get('confirmed-round'):
        logger.error('Error, the funding transaction did not go through successfully.')
        return

    # Here we specify the transaction parameters and box we'll be accessing in the hello function
    hello_tx_params = algokit_utils.TransactionParameters(boxes=[(app_client.app_id, box_key)])

    # Here we will call the hello function to create a greeting and save to the contract's box storage
    response = app_client.hello(name=name, transaction_parameters=hello_tx_params)

    # Log the results 
    logger.info(
        f"Called hello on {app_spec.contract.name} ({app_client.app_id}) "
        f"with name={name}, received: {response.return_value}"
    )