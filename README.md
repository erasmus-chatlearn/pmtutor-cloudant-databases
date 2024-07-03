# Erasmus+ ChatLearn PMTutor cloudant databases
This repository provides information on the design of PMTutor databases and python scripts for creating required databases.

## Table of Contents
- [Conceptual data model](#conceptual-data-model)
- [IBM Cloudant](#ibm-cloudant)
- [Pysical data model](#physical-data-model)
- [Prerequisites for creating databases](#prerequisites-for-creating-databases)
- [Python scripts (Windows)](#python-scripts-windows)
- [Python scripts (Ubuntu)](#python-scripts-ubuntu)
- [License](#license)

## Conceptual data model
Introduce high-level data model
## IBM Cloudant
Introduce cloudant and share links to cloudant documentations
## Physical data model
Introduce the physical data model implemented
## Prerequisites for creating databases
- IBM Cloudant service
- Python 3.10
- Python virtualenv package
- Create a Python virtual environment&mdash;use the virtual environment for running scripts
- Install requirements.txt in the virtual environment 
- Create a .env file using .env.example as template at the root level of this repository
- Provide required environment variables in the .env

## Python scripts (Windows)
### Create all required databases with default names
The command below will create 4 databases: topics-sandbox, user-profile-sandbox, user-session-events-sandbox, and
feedback-sandbox, if the names have not been taken by other existing databases in your cloudant service. You will see
the information of created databases and their indexes displayed in the terminal.

It will abort if any of the names are used by existing databases.
```bash
python scripts\create_pmtutor_databases.py
```

### Create all required databases with specific names
For example, create required databases for production:
```bash
python scripts\create_pmtutor_databases.py --learning_content topics-prod --user_profile user-profile-prod --user_session_events user-session-events-prod --feedback feedback-prod
```

### Create a new database for a specific purpose
For example, you could create a learning content database for development or testing purpose with the following command.
```bash
# The 1st argument should be 'learning_content', 'user_profile', 'user_session_events', or 'feedback'
# The 2nd argument is the name of database
# It will abort if the arguments are not valid
python scripts\create_pmtutor_database.py 'learning_content' 'topics-dev'
```

## Python scripts (Ubuntu)
### Create all required databases with default names
The command below will create 4 databases: topics-sandbox, user-profile-sandbox, user-session-events-sandbox, and 
feedback-sandbox, if the names have not been taken by other existing databases in your cloudant service. You will see
the information of created databases and their indexes displayed in the terminal.

It will abort if any of the names are used by existing databases.
```bash
python scripts/create_pmtutor_databases.py
```

### Create all required databases with specific names
For example, create required databases for production:
```bash
python scripts/create_pmtutor_databases.py --learning_content topics-prod --user_profile user-profile-prod --user_session_events user-session-events-prod --feedback feedback-prod
```

### Create a new database for a specific purpose
For example, you could create a learning content database for development or testing purpose with the following command.
```bash
# The 1st argument should be 'learning_content', 'user_profile', 'user_session_events', or 'feedback'
# The 2nd argument is the name of database
# It will abort if the arguments are not valid
python scripts/create_pmtutor_database.py 'learning_content' 'topics-dev'
```

## License
MIT
