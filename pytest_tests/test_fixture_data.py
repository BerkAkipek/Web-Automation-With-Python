import pytest
from BaseClass import BaseClass

@pytest.mark.usefixtures("data_load")
class TestExample01(BaseClass):

    def test_edit_profile(self, data_load):
        logger = self.test_logging_demo()
        logger.info(data_load)

