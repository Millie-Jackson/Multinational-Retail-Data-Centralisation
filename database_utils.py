# database_utils.py

import psycopg2
import sqlalchemy
import yaml
from sqlalchemy import engine, create_engine

class DatabaseConnector:
    '''Upload and connect to the database'''

    def read_db_creds(self, file_path):
        '''Reads and returns dictionary of credentials'''
        
        try:
            with open(file_path, 'r') as file:
                creds = yaml.safe_load(file)
            return creds
        except FileNotFoundError:
            print("Error: File (db_creds) not found")
            return {}
        except yaml.YAMLError as e:
            print("Error parsing YAML:", e)
            return {}
        
    def init_db_engine(self, file_path):
        '''Reads credentials and returns SQLAlchemy database engine'''

        # Read credentials
        creds = self.read_db_creds(file_path)

        # Construct database URL
        db_url = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"

        try:
            # Create engine
            engine = create_engine(db_url)

            # Test connection
            with engine.connect():
                pass
        except Exception as e:
            print("Error creating engin:", e)
            return None

        return engine



if __name__ == "__main__":

    db_connector = DatabaseConnector()        
    engine = db_connector.init_db_engine('db_creds.yaml')
    print(engine)

    if engine:
        print("Engine created successfully:", engine)
    else:
        print("Failed to create engine") 