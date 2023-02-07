import re 

class Filter:
    def __init__(self, filter_type, filter_values):
        """ODA FT API filter class
        
        Args:
            filter_type (str): Filter type
                Should be one of: ["date", "search"]
            filter_values (tuple): Filter values
                Should be one of:
                    [("date_column", "equality_denoter", "year", "month", "day"),

                     ("column", "search_term", "exact_match")]

                Where:
                    date_column (str): Date column name
                    equality_denoter (str): Equality denoter
                        Should be one of: ["eq", "ne", "gt", "ge", "lt", "le"]
                    year (int): Year
                    month (int, optional): Month. Defaults to None.
                    day (int, optional): Day. Defaults to None.
                      
                    column (str): Column name
                    search_term (str): Search term
                    exact_match (bool, optional): Exact match. Defaults to False.

        """
        self.string = ""
        self.add_filter(filter_type, filter_values)

    # method that takes a filter type and a tuple of filter values and calls the appropriate method depending on the filter type
    def add_filter(self, filter_type, filter_values):
        """Add ODA FT API filter

        filter_type (str): Filter type
            Should be one of: ["date", "search"]
        filter_values (tuple): Filter values
            Should be one of:
                [("date_column", "equality_denoter", "year", "month", "day"),

                    ("column", "search_term", "exact_match")]

            Where:
                date_column (str): Date column name
                equality_denoter (str): Equality denoter
                    Should be one of: ["eq", "ne", "gt", "ge", "lt", "le"]
                year (int): Year
                month (int, optional): Month. Defaults to None.
                day (int, optional): Day. Defaults to None.
                    
                column (str): Column name
                search_term (str): Search term
                exact_match (bool, optional): Exact match. Defaults to False.

        Raises:
            ValueError: If filter_type is not one of: ["date", "search"]
        """
        filter_type_options = ["date", "search"]
        if filter_type not in filter_type_options:
            raise ValueError("filter_type must be one of: %r." % filter_type_options)

        if filter_type == "date":
            self._add_date_filter(*filter_values)
        elif filter_type == "search":
            self._add_search_filter(*filter_values)

    # method that adds a filter to the string by using the _get_date_filter method
    def _add_date_filter(self, date_column, equality_denoter, year, month = None, day = None):
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
    def _add_search_filter(self, column, search_term, exact_match = False):
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
        search_term = re.sub('[^A-Za-z0-9 ]+', '', search_term)
        search_term = search_term.replace(" ", "%20")

        if exact_match:
            return column + "%20eq%20%27" + search_term + "%27"
        else:
            return "substringof(%27" + search_term + "%27," + column + ")%20eq%20true"