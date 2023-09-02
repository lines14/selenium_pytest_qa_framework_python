from main.driver.browser_utils import BrowserUtils
from main.utils.log.logger import Logger

class BaseTest:
    @staticmethod
    def setup_class():
        BrowserUtils.init_the_driver()

    @staticmethod
    def teardown_class():
        BrowserUtils.quit_driver()
        Logger.log_to_file()