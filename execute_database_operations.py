# execute_database_operations.py

from database_utils import DatabaseConnector
from data_extraction import DataExtractor



if __name__ == "__main__":

    db_connector = DatabaseConnector('db_creds.yaml')  

    # Create engine
    engine = db_connector.init_db_engine()

    if engine:
        print("Engine created successfully:", engine)
    else:
        print("Failed to create engine")  
        exit()

    # List tables
    tables = db_connector.list_db_tables()
    print("Tables in the database:", tables)



# End of file