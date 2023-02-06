# 
class Filter:
    def __init__(self):
        self.string = ""

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
        
        date_filter = "year(" + date_column + ")%20" + equality_denoter + "%20" + str(year) 
        if month:
            date_filter = date_filter + "%20and%20month(" + date_column + ")%20" + equality_denoter + "%20" + str(month) 
        if day:
            date_filter = date_filter + "%20and%20day(" + date_column + ")%20" + equality_denoter + "%20" + str(day) 

        
        return date_filter

    