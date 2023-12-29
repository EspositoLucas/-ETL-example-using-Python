from decouple import RepositoryIni, Config

config = Config(RepositoryIni(".env"))

CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
REDIRECT_URI = config("REDIRECT_URI")
DB_CONNSTR = config("DB_CONNSTR")
