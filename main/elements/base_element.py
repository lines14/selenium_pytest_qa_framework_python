from main.driver.browser_factory import BrowserFactory
from main.utils.wait.wait_utils import WaitUtils
from selenium.webdriver.common.keys import Keys
from main.utils.log.logger import Logger

class BaseElement:
    def __init__(self, elementLocator, elementName):
        self.elementLocator = elementLocator
        self.elementName = elementName

    def getElement(self):
        WaitUtils.wait_element_located(self.elementLocator)
        return BrowserFactory.instance.find_element(self.elementLocator)

    def getElements(self):
        return BrowserFactory.instance.find_elements(self.elementLocator)

    def getText(self):
        Logger.log(f'    ▶ get displayed {self.elementName}')
        text = (self.getElement()).text
        Logger.log(f'    ▶ text contains: "{text}"')
        return text

    def clickButton(self):
        Logger.log(f'    ▶ click {self.elementName}')
        (self.getElement()).click()

    def inputText(self, text):
        Logger.log(f'    ▶ input {self.elementName}')
        (self.getElement()).send_keys(text)

    def enterText(self, text):
        Logger.log(f'    ▶ input {self.elementName} and submit')
        (self.getElement()).send_keys(text + Keys.ENTER)

    def getAttributeValue(self, attr):
        return (self.getElement()).get_attribute(attr)

    def elementIsDisplayed(self):
        Logger.log(f'    ▶ {self.elementName} is present')
        return (self.getElement()).is_displayed()

    def elementIsEnabled(self):
        return (self.getElement()).is_enabled()

    def parseChildrenForAttr(self, attr):
        return list(map(lambda element: element.get_attribute(attr), self.getElements()))

    def parseChildrenForText(self):
        return list(map(lambda element: element.text, self.getElements()))

    def waitIsVisible(self):
        Logger.log(f'    ▶ wait {self.elementName} is visible')
        WaitUtils.wait_element_visible(self.elementLocator)

    def waitStalenessOf(self):
        WaitUtils.wait_element_staleness_of(self.elementLocator)
    
    def waitIsClickable(self):
        Logger.log(f'    ▶ wait {self.elementName} is clickable')
        WaitUtils.wait_element_clickable(self.elementLocator)
        