# data_extraction.py

from database_utils import DatabaseConnector

class DataExtractor:
    '''Extract data from different sources (.csv, API and S3)'''

    def __init__(self, database_connector):
        self.db_connector = database_connector

    def extract_data_from_table(self, Multinational_Retail_Data_Centralisation):
        '''Extract data from the RDS database'''

        if self.db_connector.engine is None:
            print("Engine not initialized")
            return None
        
        try:
            # Use engine to execute queries
            with self.db_connector.engine.connect() as conn:
                result = conn.execute(f"SELECT * FROM {Multinational_Retail_Data_Centralisation}")
                return result.fetchall()
        except Exception as e:
            print(f"Error exctracting data from table {Multinational_Retail_Data_Centralisation}:", e)
            return None



# End of file