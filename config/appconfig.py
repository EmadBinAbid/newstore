# Application configuration

def get_data_expiry_timedelta():
    return {
        'HOURS': 0,
        'MINUTES': 15,
        'SECONDS': 0,
    }

def get_log_filename():
    return 'logs/app.log'

def is_news_history_table_active():
    return True