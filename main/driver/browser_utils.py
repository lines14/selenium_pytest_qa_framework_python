from main.utils.log.logger import Logger
from main.utils.wait.wait_utils import WaitUtils
from main.driver.browser_factory import BrowserFactory

class BrowserUtils:
    @staticmethod
    def init_the_driver():
        Logger.log('[info] ▶ init driver')
        BrowserFactory.init_instance()

    @staticmethod
    def get_url(_):
        Logger.log(f'[info] ▶ open base URL: {_}')
        BrowserFactory.instance.get(_)

    @staticmethod
    def scroll_to_the_bottom():
        BrowserFactory.instance.execute_script('window.scrollBy(0, document.body.scrollHeight);')

    @staticmethod
    def handle_original_tab():
        return BrowserFactory.instance.current_window_handle
    
    @staticmethod
    def get_tabs_list():
        return BrowserFactory.instance.window_handles

    @staticmethod
    def switch_driver_to_another_tab(prev_tabs_list, original_window):
        Logger.log(f'[info] ▶ switch driver to another tab')
        WaitUtils.wait_new_window_is_opened(prev_tabs_list)
        for window_handle in BrowserFactory.instance.window_handles:
            if window_handle != original_window:
                BrowserFactory.instance.switch_to.window(window_handle)
                break

    @staticmethod
    def switch_driver_to_original_tab(original_tab):
        Logger.log('[info] ▶ switch driver to previous tab')
        BrowserFactory.instance.switch_to.window(original_tab)

    @staticmethod
    def get_alert():
        return WaitUtils.wait_alert_is_present()

    @classmethod
    def get_alert_text(cls):
        Logger.log('[info] ▶ alert with text is open')
        text = (cls.get_alert()).text
        Logger.log(f'[info]   text contains: "{text}"')
        return text

    @classmethod
    def enter_text_to_alert(cls, text):
        Logger.log('[info] ▶ input text to alert form')
        (cls.get_alert()).send_keys(text)

    @classmethod
    def accept_alert(cls):
        Logger.log('[info] ▶ accept alert')
        (cls.get_alert()).accept()

    @classmethod
    def alert_is_displayed(cls):
        try:
            cls.get_alert()
            return True
        except:
            return False

    @staticmethod
    def go_into_frame(id_or_index):
        Logger.log('[info] ▶ go into frame')
        BrowserFactory.instance.switch_to.frame(id_or_index)

    @staticmethod
    def go_out_Of_frame():
        Logger.log('[info] ▶ go out of frame')
        BrowserFactory.instance.switch_to.default_content()

    @staticmethod
    def close_tab():
        Logger.log('[info] ▶ close tab')
        BrowserFactory.instance.close()
    
    @staticmethod
    def quit_driver():
        Logger.log('[info] ▶ quit driver')
        BrowserFactory.instance.quit()
        BrowserFactory.instance = None