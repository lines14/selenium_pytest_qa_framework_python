from main.utils.log.logger import Logger
from tests.API.gmail_API import GmailAPI
from main.utils.data.config_manager import ConfigManager

def token_refresher():
    gmail_API = GmailAPI(ConfigManager.get_API_config_data().API_auth_URL)
    response = gmail_API.refresh_token().text
    try:
        with open('../../../resources/API_token.json', 'w') as file:
            file.write(response)
        Logger.log('[info] ▶ successfully rewrite API_token.json')
    except:
        Logger.log('[error] ▶ error while rewrite API_token.json!')
        
token_refresher()