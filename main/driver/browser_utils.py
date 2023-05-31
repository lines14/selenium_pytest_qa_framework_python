from main.driver.browser_factory import BrowserFactory
from main.utils.log.logger import Logger
from main.utils.wait.wait_utils import WaitUtils

class BrowserUtils:
    def init_the_driver(self):
        Logger.log('    ▶ init driver')
        BrowserFactory.create_instance()

    def getUrl(self, _):
        BrowserFactory.instance.get(_)

    def scrollToTheBottom(self):
        BrowserFactory.instance.execute_script('window.scrollBy(0, document.body.scrollHeight);')

    def handleOriginalTab(self):
        return BrowserFactory.instance.current_window_handle

    def getTabsCount(self):
        return len(BrowserFactory.instance.window_handles)

    def switchDriverToAnotherTab(self, prevTabsCount, original_window):
        Logger.log(f'    ▶ switch driver to another tab')
        WaitUtils.wait_new_window_is_opened(prevTabsCount)
        for window_handle in BrowserFactory.instance.window_handles:
            if window_handle != original_window:
                BrowserFactory.instance.switch_to.window(window_handle)
                break

    def switchDriverToOriginalTab(self, originalTab):
        Logger.log('    ▶ switch driver to previous tab')
        BrowserFactory.instance.switch_to.window(originalTab)

    def getAlert(self):
        return WaitUtils.wait_alert_is_present()

    def getAlertText(self):
        Logger.log('    ▶ alert with text is open')
        text = (self.getAlert()).text
        Logger.log(f'    ▶ text contains: "{text}"')
        return text

    def enterTextToAlert(self, text):
        Logger.log('    ▶ input text to alert form')
        (self.getAlert()).send_keys(text)

    def acceptAlert(self):
        Logger.log('    ▶ accept alert')
        (self.getAlert()).accept()

    def alertIsDisplayed(self):
        try:
            self.getAlert()
            return True
        except:
            return False

    def goIntoFrame(self, id_or_index):
        Logger.log('    ▶ go into frame')
        BrowserFactory.instance.switch_to.frame(id_or_index)

    def goOutOfFrame(self):
        Logger.log('    ▶ go out of frame')
        BrowserFactory.instance.switch_to.default_content()

    def closeTab(self):
        Logger.log('    ▶ close tab')
        BrowserFactory.instance.close()
    
    def quitDriver(self):
        Logger.log('    ▶ quit driver')
        BrowserFactory.instance.quit()
        BrowserFactory.instance = None