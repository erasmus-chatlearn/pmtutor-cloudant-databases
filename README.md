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
IBM Cloudant was chosen for the database implementation. It is a fully managed and distributed document database service designed 
for heavy workloads and fast-growing web and mobile applications. It offers elastic scalability for both throughput and 
storage, ensuring high availability. Cloudant is API-compatible with Apache CouchDB, facilitating hybrid and multicloud
architectures. Key features include data encryption, global data distribution for disaster recovery, and support for 
various programming languages, including Java, Node.js, Python, and Swift. Ideal for serverless and mobile applications, 
Cloudant ensures seamless data synchronization and high performance.

Cloudant's indexing feature supports advanced query capabilities, allowing efficient searches across large datasets. 
It enables developers to create indexes for faster retrieval of documents based on specified criteria. This feature is 
crucial for optimizing performance in applications that require complex querying and real-time data access.

Databases can be managed by authorized users through a web browser in addition to programming scripts. Below shows an example of querying 
all exercises by a learning topic, Earned Valued Management, through a browser.
![Cloudant web UI](./images/cloudant-1.png)

During the project, databases were managed through both programming scripts and web browser.

Below are useful links for working with the database service:
- [General information](https://www.ibm.com/products/cloudant)
- [Service documentation](https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-getting-started-with-cloudant)
- [API documentation](https://cloud.ibm.com/apidocs/cloudant)

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
