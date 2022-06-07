import psycopg2
import psycopg2.extras
from decouple import config


class DatabaseConnection(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseConnection, cls).__new__(cls)
        return cls.instance
    

    def __init__(self):
        self.DATABASE_URL = config("DATABASE_URL")
        self.USER = config("PGUSER")
        self.PASSWORD = config("PGPASSWORD")
        self.PORT = config("PGPORT")
        self.DATABASE = config("PGDATABASE")
        self.HOST = config("PGHOST")
        self.db_cursor = None


    def get_db_cursor(self):
        """
        Connect to the database.

        Returns:

        """
        # print("connect to db")
        # try:
        #     print("successfully connect to the database")
        return psycopg2.connect(
            dbname=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT
        )
        # except Exception as e:
        #     SystemError("A problem happens during the db connection", e)
        #     exit(1)
    
    
