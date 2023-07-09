from main.base_form import BaseForm
from main.elements.base_element_children.label import Label

class FootballPage(BaseForm):
    def __init__(self):
        super().__init__('//div[@class="tab--4RNtVz"]', 'game page')
        self.rows = Label('//div[@class="row-common--33mLED"]', 'table rows')

    def get_table_rows(self):
        return self.rows.get_elements()