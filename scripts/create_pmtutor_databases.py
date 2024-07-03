import argparse
from services.pmtutor_db_service import (check_if_a_pmtutor_db_exists, create_pmtutor_database_and_indexes,
                                         show_pmtutor_database_info, show_pmtutor_database_design_documents)


def main():
    args = parse_args()
    print("Let's check first if the names are available...")
    existing_db_count = check_if_pmtutor_db_names_exist(
        args.learning_content, args.user_profile, args.user_session_events, args.feedback)
    # Only create databases if all the names are available
    if existing_db_count == 0:
        print('\nStart creating databases...')
        created_db_names = create_databases(args)
        print('Databases are created.')
        print("\nGet information about created databases...")
        print_db_info_and_design_documents(created_db_names)
    else:
        print('\nScript aborted.')
        print('One or more names have been used by other databases.')
        print('Please try again with unique names.')


def check_if_pmtutor_db_names_exist(learning_content, user_profile, user_session_events, feedback):
    db_exists = False
    existing_db_count = 0

    print(f'Check if a database exist with the name {learning_content}...', end=' ')
    db_exists = check_if_a_pmtutor_db_exists(learning_content)
    print(db_exists)
    if db_exists:
        existing_db_count += 1

    print(f'Check if a database exist with the name {user_profile}...', end=' ')
    db_exists = check_if_a_pmtutor_db_exists(user_profile)
    print(db_exists)
    if db_exists:
        existing_db_count += 1

    print(f'Check if a database exist with the name {user_session_events}...', end=' ')
    db_exists = check_if_a_pmtutor_db_exists(user_session_events)
    print(db_exists)
    if db_exists:
        existing_db_count += 1

    print(f'Check if a database exist with the name {feedback}...', end=' ')
    db_exists = check_if_a_pmtutor_db_exists(feedback)
    print(db_exists)
    if db_exists:
        existing_db_count += 1
    return existing_db_count


def create_databases(args):
    db_names = []
    create_pmtutor_database_and_indexes('learning_content', args.learning_content)
    db_names.append(args.learning_content)

    create_pmtutor_database_and_indexes('user_profile', args.user_profile)
    db_names.append(args.user_profile)

    create_pmtutor_database_and_indexes('user_session_events', args.user_session_events)
    db_names.append(args.user_session_events)

    create_pmtutor_database_and_indexes('feedback', args.feedback)
    db_names.append(args.feedback)
    return db_names


def print_db_info_and_design_documents(db_names):
    for name in db_names:
        show_pmtutor_database_info(name)
        show_pmtutor_database_design_documents(name)


def parse_args():
    parser = argparse.ArgumentParser(description='This script creates required databases for PMTutor system.')
    parser.add_argument('--learning_content', default='topics-sandbox', help='Database name for learning content')
    parser.add_argument('--user_profile', default='user-profile-sandbox', help='Database name for user profile')
    parser.add_argument('--user_session_events', default='user-session-events-sandbox', help='Database name for user session events')
    parser.add_argument('--feedback', default='feedback-sandbox', help='Database name for feedback')
    return parser.parse_args()


if __name__ == '__main__':
    main()



