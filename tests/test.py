from main.driver.browser_utils import BrowserUtils
from main.utils.data.config_manager import ConfigManager
from tests.page_objects.football_page import FootballPage

BrowserUtils.init_the_driver()
BrowserUtils.get_url(ConfigManager.get_config_data().base_URL)

football_page = FootballPage()
football_page.wait_page_is_visible()
print(football_page.get_table_rows())