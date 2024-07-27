
def get_config():
    return LocalConfig


class LocalConfig:
    MOCK_API = "http://mock:5002"
    ESTIMATE_ENDPOINT = "/estimate"

    USER = 'root'
    PASSWORD = 'password'
    HOST = 'db'
    PORT = '3306'
    DB_NAME = 'DB'
    CONNECT_STR = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
