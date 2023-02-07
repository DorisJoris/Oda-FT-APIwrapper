import unittest 

from odaftapiwrapper.filters import Filter


# unittest test class for the Filter class 
class TestFilter(unittest.TestCase):
    # Test that the static _get_date_filter method returns the correct string
    def test_get_date_filter(self):
        date_column = "date_column"
        equality_denoter = "eq"
        year = 2023
        month = 1
        day = 12
        
        # get the date filter string
        date_filter = Filter._get_date_filter(date_column, equality_denoter, year, month, day)
        
        # check that the string is correct
        expected_string = "year(date_column)%20eq%202023%20and%20month(date_column)%20eq%201%20and%20day(date_column)%20eq%2012"
        self.assertEqual(date_filter, expected_string)

    # Test that the static _get_search_filter method returns the correct string
    def test_get_search_filter(self):
        column = "column"
        search_term = "search term"
        
        # get the search filter string
        search_filter = Filter._get_search_filter(column, search_term)
        
        # check that the string is correct
        expected_string = "substringof(%27search%20term%27,column)%20eq%20true"
        self.assertEqual(search_filter, expected_string)

    # Test that the init method results in a Filter object with the correct string attribute
    # Using a date filter type
    def test_init_date(self):
        filter_type = "date"
        filter_values = ("date_column", "eq", 2023, 1, 12)
        
        # create a Filter object with a date filter
        filter = Filter(filter_type, filter_values)
        
        # check that the string attribute is correct
        expected_string = "year(date_column)%20eq%202023%20and%20month(date_column)%20eq%201%20and%20day(date_column)%20eq%2012"
        self.assertEqual(filter.string, expected_string)

    # Test that the init method results in a Filter object with the correct string attribute
    # Using a search filter type with the exact_match parameter set to True
    def test_init_search(self):
        filter_type = "search"
        filter_values = ("navn", "Mette Møller", True)
        
        # create a Filter object with a search filter
        filter = Filter(filter_type, filter_values)
        
        # check that the string attribute is correct
        expected_string = "navn%20eq%20%27Mette%20Møller%27"
        self.assertEqual(filter.string, expected_string)

    # Test that the add_date_filter method results in the correct string attribute for a Filter object where the string attribute is not empty
    def test_add_date_filter(self):
        filter_type = "date"
        filter_values = ("date_column", "gt", 2023, None, None)
        
        # create a Filter object with a date filter
        filter = Filter(filter_type, filter_values)
        
        # add another date filter to the Filter object
        filter._add_date_filter("date_column", "lt", 2024, None, 13)
        
        # check that the string attribute is correct
        expected_string = "year(date_column)%20gt%202023%20and%20year(date_column)%20lt%202024%20and%20day(date_column)%20lt%2013"
        self.assertEqual(filter.string, expected_string)

    # Test that the add_search_filter method results in the correct string attribute for a Filter object where the string attribute is not empty
    def test_add_search_filter(self):
        filter_type = "search"
        filter_values = ("column", "search term", True)
        
        # create a Filter object with a search filter
        filter = Filter(filter_type, filter_values)
        
        # add another search filter to the Filter object
        filter._add_search_filter("anothercolumn", "another search term", False)
        
        # check that the string attribute is correct
        expected_string = "column%20eq%20%27search%20term%27%20and%20substringof(%27another%20search%20term%27,anothercolumn)%20eq%20true"
        self.assertEqual(filter.string, expected_string)

    # Test that the add_filter method results in the correct string attribute for a Filter object where the string attribute is not empty
    # Using a date filter type
    def test_add_filter_date(self):
        filter_type = "date"
        filter_values = ("date_column", "gt", 2023, None, None)
        
        # create a Filter object with a date filter
        filter = Filter(filter_type, filter_values)
        
        # add another date filter to the Filter object
        filter.add_filter("date", ("date_column", "lt", 2024, None, 13))
        
        # check that the string attribute is correct
        expected_string = "year(date_column)%20gt%202023%20and%20year(date_column)%20lt%202024%20and%20day(date_column)%20lt%2013"
        self.assertEqual(filter.string, expected_string)

if __name__ == "__main__":
    unittest.main()