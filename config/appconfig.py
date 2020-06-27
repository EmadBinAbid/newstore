# Application configuration

def get_data_expiry_timedelta() -> dict:
    return {
        'HOURS': 0,
        'MINUTES': 15,
        'SECONDS': 0,
    }

def get_log_filename() -> str:
    return 'logs/app.log'

def is_news_history_table_active() -> bool:
    return True