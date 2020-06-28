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

To install these dependencies, run the `envsetup.bat` file located inside `./setup`.

## Setting up Database
Newstore uses PostgreSQL database. To install PostgreSQL, please visit: https://www.postgresql.org/download/.

To create Newstore database locally, run the `dbsetup.bat` file located inside `./setup`. Before executing this file, make sure that you have `postgres` as one of the users of your PostgreSQL instance. If not abided, the command might break for now.

Newstore runs on PostgreSQL user `postgres` with password `password` on `localhost:5432` as default. You may change these settings in `./config/dbconfig.py`.

Newstore, by default, stores the history of news that are accumulated over time. You can turn off this functionality by setting `is_news_history_table_active` to `False` in `appconfig.py`.

## General Configurations
Apart from `dbconfig.py`, `./config` contains three other configuration files to manage app, Reddit API, and NewsAPI. 

### redditapiconfig.py
Contains `client_id` and `client_secret` required to connect with Reddit API.

### newsapiconfig.py
Contains API key to connect with NewsAPI.

### appconfig.py
Contains general app configuration and settings. You may change these settings to customise the app behaviour. 

## Logs
All the generated logs of Newstore are stored in `./logs`.

## Endpoints
- `GET /news`, `GET /news?query=somekeyword`
    - Usage: This endpoint works as a standalone endpoint as well as accepts a query parameter `query` to search for news against specific keyword. It fetches and returns news from all the supported sources.

- `GET /sources`
    - Usage: It fetches and returns all the news sources that are supported by Newstore.

Every endpoint requires an API token that must be provided in the request header against the key `Authorization`. In our promotional stages, we have given free API token to our clients as `wErdTg123STELLICgF5GhK`.

## Postman Collection
To save your time creating dummy requests, we have already come to your rescue. You can find a full-fledged ready Postman collection at `./scripts/Newstore.postman_collection.json` containing requests against all the supported endpoints so far. We will keep on updating it as the product grows.

## Running the App
To run this app, navigate to the project's root directory and run `python manage.py runserver` in the terminal. Your application should be up and running at `localhost:8000`.

## Contact
For queries and concerns, feel free to open the issue on this repository or email the author at emad.bin.abid@gmail.com