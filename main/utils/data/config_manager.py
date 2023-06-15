import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class ConfigManager:
    @staticmethod
    def get_config_data():
        with open('../../../resources/config_data.json', 'r', encoding='utf-8') as data:
            return type("ConfigData", (object, ), json.loads(data.read()))

    @staticmethod
    def get_test_data():
        with open('../../../resources/test_data.json', 'r', encoding='utf-8') as data:
            return type("TestData", (object, ), json.loads(data.read()))

    @staticmethod
    def get_status_code():
        with open('../API/API_codes.json', 'r', encoding='utf-8') as data:
            return type("StatusCode", (object, ), json.loads(data.read()))

    @staticmethod
    def get_API_endpoint():
        with open('../../../resources/API_endpoints.json', 'r', encoding='utf-8') as data:
            return type("APIEndpoint", (object, ), json.loads(data.read()))

    @staticmethod
    def get_API_config_data():
        with open('../../../resources/API_config_data.json', 'r', encoding='utf-8') as data:
            return type("APIConfigData", (object, ), json.loads(data.read()))

    @staticmethod
    def get_DB_config_data():
        with open('../../../resources/DB_config_data.json', 'r', encoding='utf-8') as data:
            return type("DBConfigData", (object, ), json.loads(data.read()))
        
    @staticmethod
    def get_API_client_secret():
        try:
            for file in os.listdir('../../../resources'):
                if file.startswith('client_secret'):
                    with open(f'../../../resources/{file}', 'r', encoding='utf-8') as data:
                        return type("ClientSecret", (object, ), json.loads(data.read())['installed'])
        except:
            return None
                
    @staticmethod
    def get_API_access_token():
        try:
            with open('../../../resources/API_token.json', 'r', encoding='utf-8') as data:
                return type("AccessToken", (object, ), json.loads(data.read())).access_token
        except:
            return None