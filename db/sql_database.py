from langchain_community.utilities import SQLDatabase
from config.settings import settings

def get_database():
    db = SQLDatabase.from_uri(settings.DATABASE_URI, max_string_length=1000000)
    return db
