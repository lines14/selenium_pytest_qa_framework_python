from main.elements.base_element import BaseElement

class TextBox(BaseElement):
    def __init__(self, locator_type, locator, name):
        super().__init__(locator_type, locator, name)