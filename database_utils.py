# database_utils.py

import yaml

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



if __name__ == "__main__":

    db_connector = DatabaseConnector()        
    creds_dict = db_connector.read_db_creds('db_creds.yaml')
    print(creds_dict)