# 
class Filter:
    def __init__(self):
        self.string = ""

    # method that adds a filter to the string by using the _get_date_filter method
    def add_date_filter(self, date_column, equality_denoter, year, month = None, day = None):
        """Add ODA FT API date filter
        
        Args:
            date_column (str): Date column name
            equality_denoter (str): Equality denoter
                Should be one of: ["eq", "ne", "gt", "ge", "lt", "le"]
            year (int): Year
            month (int, optional): Month. Defaults to None.
            day (int, optional): Day. Defaults to None.

        Returns:
            str: ODA FT API date filter
        """   
        date_filter = self._get_date_filter(date_column, equality_denoter, year, month, day)
        if self.string == "":
            self.string = date_filter
        else:
            self.string = self.string + "%20and%20" + date_filter

    # method that adds a filter to the string by using the _get_search_filter method
    def add_search_filter(self, column, search_term, exact_match = False):
        """Add ODA FT API search filter

        Args:
            column (str): Column name
            search_term (str): Search term
            exact_match (bool, optional): Exact match. Defaults to False.

        Returns:
            str: ODA FT API search filter
        """
        search_filter = self._get_search_filter(column, search_term, exact_match)
        if self.string == "":
            self.string = search_filter
        else:
            self.string = self.string + "%20and%20" + search_filter
    
    @staticmethod
    def _get_date_filter(date_column, equality_denoter, year, month = None, day = None):
        """Get ODA FT API date filter

        Args:
            date_column (str): Date column name

            equality_denoter (str): Equality denoter
                Should be one of: ["eq", "ne", "gt", "ge", "lt", "le"]
            
            year (int): Year
            
            month (int, optional): Month. Defaults to None.
            day (int, optional): Day. Defaults to None.    

        Returns:
            str: ODA FT API date filter

        Raises:
            ValueError: If equality_denoter is not one of: ["eq", "ne", "gt", "ge", "lt", "le"]
        """
        equality_denoter_options = ["eq", "ne", "gt", "ge", "lt", "le"]
        if equality_denoter not in equality_denoter_options:
            raise ValueError("equality_denoter must be one of: %r." % equality_denoter_options)
        
        date_filter = ""

        if year:
            date_filter = date_filter + "year(" + date_column + ")%20" + equality_denoter + "%20" + str(year)

        if month:
            if len(date_filter) > 0:
                date_filter = date_filter + "%20and%20"
            date_filter = date_filter + "month(" + date_column + ")%20" + equality_denoter + "%20" + str(month)

        if day:
            if len(date_filter) > 0:
                date_filter = date_filter + "%20and%20"
            date_filter = date_filter + "day(" + date_column + ")%20" + equality_denoter + "%20" + str(day) 

        return date_filter

    # static method that returns a filter string for a given column and a search term that is either an exact match or a partial match
    @staticmethod
    def _get_search_filter(column, search_term, exact_match = False):
        """Get ODA FT API search filter

        Args:
            column (str): Column name

            search_term (str): Search term

            exact_match (bool, optional): Exact match. Defaults to False.

        Returns:
            str: ODA FT API search filter
        """
        if exact_match:
            return column + "%20eq%20%27" + search_term + "%27"
        else:
            return "substringof(%27" + search_term + "%27," + column + ")%20eq%20true"