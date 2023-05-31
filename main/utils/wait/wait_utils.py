from main.driver.browser_factory import BrowserFactory
from main.utils.data.config_manager import ConfigManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class WaitUtils:
    def wait_new_window_is_opened(self, prevTabsCount):
        WebDriverWait(BrowserFactory.instance, ConfigManager.get_config_data().wait_time).until(expected_conditions.new_window_is_opened(prevTabsCount))

    def wait_alert_is_present(self):
        return WebDriverWait(BrowserFactory.instance, ConfigManager.get_config_data().wait_time).until(expected_conditions.alert_is_present())