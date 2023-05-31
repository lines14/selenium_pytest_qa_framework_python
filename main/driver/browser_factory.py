from selenium import webdriver
from main.utils.data.config_manager import ConfigManager

class BrowserFactory:
    def __init__(self):
        self.__instance = None

    def create_instance(self):
        if (not self.__instance):
            if (ConfigManager.get_config_data().browser == 'chrome'):
                options = webdriver.ChromeOptions()
                options.add_argument('--incognito')
                self.__instance = webdriver.Chrome(options=options)

                if (ConfigManager.get_config_data().is_maximize):
                    self.__instance.maximize_window()

            elif (ConfigManager.get_config_data().browser == 'firefox'):
                options = webdriver.FirefoxOptions()
                options.add_argument('-private')
                self.__instance = webdriver.Firefox(options=options)

                if (ConfigManager.get_config_data().is_maximize):
                    self.__instance.maximize_window()

    @property
    def instance(self):
        if (self.__instance):
            return self.__instance
        
    @instance.setter
    def instance(self, value):
        self.__instance = value