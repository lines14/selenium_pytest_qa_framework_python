from assertions import assert_, assert_truth
from assertions.operators import Operators
from main.base_test import BaseTest
from main.utils.random.randomizer import Randomizer
from main.utils.data.config_manager import ConfigManager

class TestDB(BaseTest):
    @classmethod
    def test_DB(cls):
        response = cls.project_DB.get_first_project()
        assert_(response, ConfigManager.get_test_data().projectName, 'response equals expected', Operators.EQUAL)
        prev_response = cls.project_DB.get_all_projects()
        cls.project_DB.add_project(Randomizer.get_random_string(False, False, False, False, 5))
        response = cls.project_DB.get_all_projects()
        assert_truth(len(response) > len(prev_response), 'added new project')