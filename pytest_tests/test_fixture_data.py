import pytest


@pytest.mark.usefixtures("data_load")
class TestExample01:

    def test_edit_profile(self, data_load):
        print(data_load)

