# PostgreSQL Database configuration

def get_db_config():
    return {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'newstore',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
