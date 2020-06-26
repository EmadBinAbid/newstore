# Newstore
Newstore is a JSON API that aggregates news and blog articles from various popular third party APIs built with Django, DRF, and PostgreSQL.

Newstore uses a relatively older version of Django i.e. v2.2.13. If you already have this version of Django installed then well and good. Else it is recommeded to create a Python virtual environment to contribute to this task. You can create your own virtual environment as follows:
`python -m venv [path at which you want to create the virtual environment]`

For instance the command `python -m venv env` will create a virtual environment in `./env`.

Once the environment is set up, you just need to navigate to `./Scripts` and run `activate.bat` in command line to activate the virtual environment.

## Dependencies

- django v2.2.13
- djangorestframework
- psycopg2
- praw
- newsapi-python

To install these dependencies, run the `envsetup.bat` file located in the root folder of this repository.

## Setting up Database
Newstore uses PostgreSQL database. To install PostgreSQL, please visit: https://www.postgresql.org/download/.

To create Newstore database locally, run the `dbsetup.bat` file located in the root folder of this repository.

# Endpoints
- GET /news