from main.utils.API.base_API import BaseAPI
from main.utils.data.config_manager import ConfigManager

class API(BaseAPI):
    def __init__(self):
        super().__init__(ConfigManager.get_API_config_data().API_base_URL, ConfigManager.get_API_config_data().API_timeout)

    def getPosts(self, id):
        if id:
            return super().get(f'{ConfigManager.get_API_endpoint().API_posts}/{id}')
        else:
            return super().get(ConfigManager.get_API_endpoint().API_posts)

    def getUsers(self, id):
        if id:
            return super().get(f'{ConfigManager.get_API_endpoint().API_users}/{id}')
        else:
            return super().get(ConfigManager.get_API_endpoint().API_users)

    # def postPosts(self, model):
        # params = { 
        #     id: model.id, 
        #     userId: model.userId, 
        #     title: model.title, 
        #     body: model.body
        # }
        # return super().post(ConfigManager.get_API_endpoint().API_posts, params)