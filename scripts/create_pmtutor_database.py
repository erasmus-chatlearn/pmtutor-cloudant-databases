import argparse
from services.pmtutor_db_service import (check_if_a_pmtutor_db_exists, create_pmtutor_database_and_indexes,
                                         show_pmtutor_database_info, show_pmtutor_database_design_documents)


def main():
    args = parse_args()
    is_purpose_valid = check_is_purpose_valid(args.purpose)
    if is_purpose_valid is False:
        print('Script aborted!')
        return print('Please try again with a valid purpose from learning_content, user_profile, user_session_events, or feedback.')
    db_name_exists = check_if_a_pmtutor_db_exists(args.database_name)
    if db_name_exists:
        print('Script aborted!')
        return print(f'{args.database_name} exists already. Please try again with a new name.')
    print(f'For {args.purpose}, start creating a database with the name: {args.database_name}...')
    create_pmtutor_database_and_indexes(args.purpose, args.database_name)
    print(f'Database {args.database_name} is created!')
    show_pmtutor_database_info(args.database_name)
    show_pmtutor_database_design_documents(args.database_name)
    print('\nDone!')


def parse_args():
    parser = argparse.ArgumentParser(description='This script creates a database for PMTutor system.')
    parser.add_argument('purpose', help='It should be "learning_content", "user_profile", "user_session_events", or "feedback"')
    parser.add_argument('database_name', help='An unique database name')
    return parser.parse_args()


def check_is_purpose_valid(purpose):
    is_valid = False
    if purpose == 'learning_content' or purpose == 'user_profile' or purpose == 'user_session_events' or purpose == 'feedback':
        is_valid = True
    return is_valid


if __name__ == "__main__":
    main()
