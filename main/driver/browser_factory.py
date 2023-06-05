from selenium import webdriver
from main.utils.data.config_manager import ConfigManager

class BrowserFactory:
    __instance = None

    @classmethod
    def create_instance(cls):
        if (cls.__instance is None):
            if (ConfigManager.get_config_data().browser == 'chrome'):
                options = webdriver.ChromeOptions()
                options.add_argument('--incognito')
                cls.__instance = webdriver.Chrome(options=options)

                if (ConfigManager.get_config_data().is_maximize):
                    cls.__instance.maximize_window()

            elif (ConfigManager.get_config_data().browser == 'firefox'):
                options = webdriver.FirefoxOptions()
                options.add_argument('-private')
                cls.__instance = webdriver.Firefox(options=options)

                if (ConfigManager.get_config_data().is_maximize):
                    cls.__instance.maximize_window()

    @property
    def instance(cls):
        if (cls.__instance):
            return cls.__instance
        
    @instance.setter
    def instance(cls, value):
        cls.__instance = value