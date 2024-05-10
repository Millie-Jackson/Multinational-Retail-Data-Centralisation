# database_utils.py

import psycopg2
import sqlalchemy
import yaml
from sqlalchemy import engine, create_engine, MetaData

class DatabaseConnector:
    '''Upload and connect to the database'''

    def __init__(self, file_path) -> None:
        '''Initialise with credentials file path'''

        self.file_path = file_path
        self.engine = self.init_db_engine()

    def read_db_creds(self):
        '''Reads and returns dictionary of credentials'''
        
        try:
            with open(self.file_path, 'r') as file:
                creds = yaml.safe_load(file)
            return creds
        except FileNotFoundError:
            print("Error: File (db_creds) not found")
            return {}
        except yaml.YAMLError as e:
            print("Error parsing YAML:", e)
            return {}
        
    def init_db_engine(self):
        '''Reads credentials and returns SQLAlchemy database engine'''

        # Read credentials
        creds = self.read_db_creds()

        # Construct database URL
        db_url = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"

        try:
            # Create engine
            engine = create_engine(db_url)

            # Test connection
            with engine.connect():
                pass
        except Exception as e:
            print("Error creating engine:", e)
            return None

        return engine
    
    def list_db_tables(self):
        '''List all tables in the database'''

        if self.engine is None:
            print("Engine not initializes")
            return[]
        
        try:
            metadata = MetaData(bind=self.engine)
            metadata.reflect()
            return metadata.tables.keys()
        except Exception as e:
            print("Error listing tables:", e)
            return []



# End of file