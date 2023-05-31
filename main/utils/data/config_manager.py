# import configData from '../../../resources/configData.json' assert { type: "json" };
# import testData from '../../../resources/testData.json' assert { type: "json" };
# import APICodes from '../API/APICodes.json' assert { type: "json" };
# import APIEndpoints from '../../../resources/APIEndpoints.json' assert { type: "json" };
# import APIConfigData from '../../../resources/APIConfigData.json' assert { type: "json" };
# import DBConfigData from '../../../resources/DBConfigData.json' assert { type: "json" };

# class Config_manager:
#     def get_config_data():
#         with open(r'/resources/config_data.json', 'r', encoding='utf-8') as x:
#             y = x.read()
#             print(y)
#         return JSON.parse(JSON.stringify(configData))

#     def get_test_data():
#         return JSON.parse(JSON.stringify(testData))

#     def get_test_file():
#         return path.join(path.resolve(), "test", "template.jpg")

#     def get_status_code():
#         return JSON.parse(JSON.stringify(APICodes))

#     def get_api_endpoint():
#         return JSON.parse(JSON.stringify(APIEndpoints))

#     def get_api_config_data():
#         return JSON.parse(JSON.stringify(APIConfigData))

#     def get_database_config_data():
#         return JSON.parse(JSON.stringify(DBConfigData))