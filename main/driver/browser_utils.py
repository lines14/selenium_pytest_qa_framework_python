from main.driver.browser_factory import BrowserFactory
from main.utils.log.logger import Logger
from main.utils.wait.wait_utils import WaitUtils

class BrowserUtils:
    @staticmethod
    def init_the_driver():
        Logger.log('    ▶ init driver')
        BrowserFactory.create_instance()

    @staticmethod
    def getUrl(_):
        BrowserFactory.instance.get(_)

    @staticmethod
    def scrollToTheBottom():
        BrowserFactory.instance.execute_script('window.scrollBy(0, document.body.scrollHeight);')

    @staticmethod
    def handleOriginalTab():
        return BrowserFactory.instance.current_window_handle

    @staticmethod
    def getTabsCount():
        return len(BrowserFactory.instance.window_handles)

    @staticmethod
    def switchDriverToAnotherTab(prevTabsCount, original_window):
        Logger.log(f'    ▶ switch driver to another tab')
        WaitUtils.wait_new_window_is_opened(prevTabsCount)
        for window_handle in BrowserFactory.instance.window_handles:
            if window_handle != original_window:
                BrowserFactory.instance.switch_to.window(window_handle)
                break

    @staticmethod
    def switchDriverToOriginalTab(originalTab):
        Logger.log('    ▶ switch driver to previous tab')
        BrowserFactory.instance.switch_to.window(originalTab)

    @staticmethod
    def getAlert():
        return WaitUtils.wait_alert_is_present()

    @classmethod
    def getAlertText(cls):
        Logger.log('    ▶ alert with text is open')
        text = (cls.getAlert()).text
        Logger.log(f'    ▶ text contains: "{text}"')
        return text

    @classmethod
    def enterTextToAlert(cls, text):
        Logger.log('    ▶ input text to alert form')
        (cls.getAlert()).send_keys(text)

    @classmethod
    def acceptAlert(cls):
        Logger.log('    ▶ accept alert')
        (cls.getAlert()).accept()

    @classmethod
    def alertIsDisplayed(cls):
        try:
            cls.getAlert()
            return True
        except:
            return False

    @staticmethod
    def goIntoFrame(id_or_index):
        Logger.log('    ▶ go into frame')
        BrowserFactory.instance.switch_to.frame(id_or_index)

    @staticmethod
    def goOutOfFrame():
        Logger.log('    ▶ go out of frame')
        BrowserFactory.instance.switch_to.default_content()

    @staticmethod
    def closeTab():
        Logger.log('    ▶ close tab')
        BrowserFactory.instance.close()
    
    @staticmethod
    def quitDriver():
        Logger.log('    ▶ quit driver')
        BrowserFactory.instance.quit()
        BrowserFactory.instance = None