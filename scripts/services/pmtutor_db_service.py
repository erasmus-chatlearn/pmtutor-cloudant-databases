from cloudant.database_operations import (create_search_index, create_cloudant_database, get_database_info,
                                            get_all_design_docs, db_exists)

import json
import time


def create_indexes_for_learning_content_database(db_name):
    try:
        design_doc_name = 'globalIndexes'
        index_name = 'byDocType'
        fields = ['docType']
        is_partitioned_index = False
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        # Avoid too many request error
        time.sleep(1)

        design_doc_name = 'partitionedIndexes'
        index_name = 'partitionedIndexByDocType'
        is_partitioned_index = True
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

        design_doc_name = 'partitionedIndexes'
        index_name = 'partitionedIndexByIsActive'
        fields = ['isActive']
        is_partitioned_index = True
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

    except Exception as err:
        print('\nGot an error, please see the details below.')
        print(err)


def create_indexes_for_user_profile_database(db_name):
    try:
        design_doc_name = 'globalIndexes'
        index_name = 'byDocType'
        fields = ['docType']
        is_partitioned_index = False
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

        design_doc_name = 'partitionedIndexes'
        index_name = 'partitionedIndexByDocType'
        is_partitioned_index = True
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

        design_doc_name = 'globalIndexes'
        index_name = 'byCreatedAt'
        fields = ['createdAt']
        is_partitioned_index = False
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

        design_doc_name = 'partitionedIndexes'
        index_name = 'partitionedIndexByCreatedAt'
        is_partitioned_index = True
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

        design_doc_name = 'partitionedIndexes'
        index_name = 'partitionedIndexBySessionId'
        fields = ['sessionId']
        is_partitioned_index = True
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

        design_doc_name = 'partitionedIndexes'
        index_name = 'partitionedIndexByUserSessionInfoId'
        fields = ['userSessionInfoId']
        is_partitioned_index = True
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

        design_doc_name = 'partitionedIndexes'
        index_name = 'partitionedIndexByUserSurveyId'
        fields = ['userSurveyId']
        is_partitioned_index = True
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

    except Exception as err:
        print('\nGot an error, please see the details below.')
        print(err)


def create_indexes_for_user_session_events_database(db_name):
    try:
        design_doc_name = 'partitionedIndexes'
        index_name = 'partitionedIndexBySessionEventTypeIdAndCreatedAt'
        fields = ['sessionEventTypeId', 'createdAt']
        is_partitioned_index = True
        create_search_index(db_name, design_doc_name, index_name, fields, is_partitioned_index)
        time.sleep(1)

    except Exception as err:
        print('\nGot an error, please see the details below.')
        print(err)


def create_pmtutor_database_and_indexes(db_purpose, db_name):
    try:
        create_cloudant_database(db_name, True)
        if db_purpose == 'learning_content':
            create_indexes_for_learning_content_database(db_name)
        elif db_purpose == 'user_profile':
            create_indexes_for_user_profile_database(db_name)
        elif db_purpose == 'user_session_events':
            create_indexes_for_user_session_events_database(db_name)
        else:
            print(f'No indexes are created for {db_name}')
    except Exception as err:
        print('\nGot an error, please see the details below.')
        print(err)


def show_pmtutor_database_info(db_name):
    print(f'\nGet database information for {db_name}...')
    db_info = get_database_info(db_name)
    print(f'{db_name}:')
    print(json.dumps(db_info, indent=2))


def show_pmtutor_database_design_documents(db_name):
    print(f'\nGet all design documents in database {db_name}...')
    db_info = get_all_design_docs(db_name)
    print(f'All design documents in database {db_name}:')
    print(json.dumps(db_info, indent=2))


def check_if_a_pmtutor_db_exists(db_name):
    return db_exists(db_name)







