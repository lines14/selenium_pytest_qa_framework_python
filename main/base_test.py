from main.driver.browser_utils import BrowserUtils
from main.utils.log.logger import Logger

class BaseTest:
    @classmethod
    def setup_class(cls):
        BrowserUtils.init_the_driver()

    def teardown_class(cls):
        BrowserUtils.quit_driver()
        Logger.log_to_file()