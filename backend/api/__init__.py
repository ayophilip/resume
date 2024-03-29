import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="CosmosDBTrigger")
@app.cosmos_db_trigger(arg_name="documents", 
                       database_name="AzureResume", 
                       collection_name="COLLECTION_NAME", 
                       connection_string_setting="CONNECTION_SETTING",
 lease_collection_name="leases", create_lease_collection_if_not_exists="true")
def test_function(documents: func.DocumentList) -> str:
    if documents:
        logging.info('Document id: %s', documents[0]['id'])