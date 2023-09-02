# import os
# from time import sleep
# from main.utils.log.logger import Logger
# from main.utils.API.base_API import BaseAPI
# from main.utils.data.data_utils import DataUtils
# from main.utils.data.config_manager import ConfigManager

# class GmailAPI(BaseAPI):
#     def __init__(self, base_URL=None, log_string=None):
#         # self.model_fields = list(filter(lambda attr: not attr.startswith("__"), dir(ModelTokenGetter)))
#         self.model_fields.reverse()
#         access_token = self.model_fields.pop().upper()
#         super().__init__(
#             base_URL or ConfigManager.get_API_config_data().API_base_URL, 
#             log_string or '[info] ▶ set base api url', 
#             ConfigManager.get_config_data().wait_time, 
#             {"Authorization": f"Bearer {'' or ConfigManager.get_API_access_token() or os.environ.get(access_token)}"}
#         )

#     def get_messages(self, id=None):
#         if id:
#             return super().get(f'{ConfigManager.get_API_endpoint().API_messages}/{id}')
#         else:
#             sleep(ConfigManager.get_API_config_data().API_timeout)
#             response = super().get(ConfigManager.get_API_endpoint().API_messages)
#             return DataUtils.JSON_to_models([response]).pop().messages

#     def get_messages_count(self):
#         Logger.log('[info] ▶ get messages count:')
#         self.messages_precount = len(self.get_messages())
#         return self.messages_precount

#     def wait_messages_count_increment(self):
#         counter = 0
#         messages_count = self.messages_precount
#         Logger.log('[info] ▶ wait incoming message:')

#         while counter < ConfigManager.get_API_config_data().API_requests_limit:
#             messages_count = len(self.get_messages())
#             if messages_count > self.messages_precount:
#                 break
#             counter+=1

#         if messages_count > self.messages_precount:
#             Logger.log('[info] ▶ successfully receive message')
#         else:
#             Logger.log('[info] ▶ message is not received')
#         return messages_count

#     def refresh_token(self):
#         model_dict = dict.fromkeys(self.model_fields)
#         for key in model_dict:
#             if ConfigManager.get_API_client_secret():
#                 model_dict[key] = vars(ConfigManager.get_API_client_secret())[key]
#             else:
#                 model_dict[key] = os.environ.get(key.upper())
#         return super().post(ConfigManager.get_API_endpoint().API_token, model_dict)