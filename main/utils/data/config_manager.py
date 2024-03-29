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