from main.utils.log.logger import Logger
from main.utils.wait.wait_utils import WaitUtils
from main.driver.browser_factory import BrowserFactory
from main.utils.data.config_manager import ConfigManager

class BaseForm:
    def __init__(self, page_locator, page_name):
        self.page_locator = page_locator
        self.page_name = page_name

    def get_unique_element(self):
        WaitUtils.wait_element_located(self.page_locator)
        return BrowserFactory.instance.find_element(self.page_locator)

    def page_is_displayed(self):
        Logger.log(f'    ▶ {self.page_name} is open')
        return (self.get_unique_element()).is_displayed()

    def page_is_enabled(self):
        Logger.log(f'    ▶ {self.page_name} is enabled')
        return (self.get_unique_element()).is_enabled()
    
    def wait_page_is_enabled(self):
        WaitUtils.wait_element_clickable(self.page_locator)