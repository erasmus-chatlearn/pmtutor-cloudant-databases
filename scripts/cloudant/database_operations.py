import json
import os
from ibmcloudant.cloudant_v1 import CloudantV1, Document, BulkDocs
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_cloud_sdk_core.api_exception import ApiException

load_dotenv()
authenticator = IAMAuthenticator(os.getenv('CLOUDANT_APIKEY'))
cloudant_client = CloudantV1(authenticator=authenticator)
cloudant_client.set_service_url(os.getenv('CLOUDANT_URL'))


# Functions related to creating a database
def create_cloudant_database(new_db_name, is_partitioned):
    return cloudant_client.put_database(db=new_db_name, partitioned=is_partitioned).get_result()


def create_search_index(db_name, design_doc_name, index_name, index_fields, is_partitioned_index):
    index = {'fields': index_fields}
    return cloudant_client.post_index(
        db=db_name, ddoc=design_doc_name, name=index_name, index=index, type='json', partitioned=is_partitioned_index)


# Functions related to reading database information
def print_capacity_throughput_information():
    response = cloudant_client.get_capacity_throughput_information().get_result()
    print(json.dumps(response, indent=2))


def print_all_dbs_info():
    db_list = cloudant_client.get_all_dbs().get_result()
    response = cloudant_client.post_dbs_info(keys=db_list).get_result()
    print(json.dumps(response, indent=2))


def get_database_info(db_name):
    return cloudant_client.get_database_information(db=db_name).get_result()


def get_all_design_docs(db_name):
    return cloudant_client.post_design_docs(include_docs=True, db=db_name).get_result()


def db_exists(db_name):
    db_exists = False
    try:
        cloudant_client.get_database_information(db=db_name).get_result()
        db_exists = True
        return db_exists
    except ApiException as apiErr:
        if apiErr.code != 404:
            print(f'Encounter error: {apiErr.message}, status code: {apiErr.code}')
        return db_exists

