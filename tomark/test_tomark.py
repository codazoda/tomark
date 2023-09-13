
from tomark import Tomark


class TestTomark:

    def test_empty_list(self):
        # Test an empty list
        input_list = []
        expected_output = ""
        assert Tomark.table(input_list) == expected_output

    def test_single_dict(self):
        # Test a list with one dictionary
        input_list = [{"Name": "Alice", "Age": 30}]
        expected_output = "| Name | Age |\n| --- | --- |\n| Alice | 30 |\n"
        assert Tomark.table(input_list) == expected_output

    def test_multiple_dicts(self):
        # Test a list with multiple dictionaries
        input_list = [
            {"Name": "Alice", "Age": 30},
            {"Name": "Bob", "Age": 25},
            {"Name": "Charlie", "Age": 35},
        ]
        expected_output = "| Name | Age |\n| --- | --- |\n| Alice | 30 |\n| Bob | 25 |\n| Charlie | 35 |\n"
        assert Tomark.table(input_list) == expected_output
