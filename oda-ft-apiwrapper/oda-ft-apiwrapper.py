import requests

# 
def get_date_filter(date_column, equality_denoter, year, month = None, day = None):
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
        start_filter = start_filter + "%20and%20month(" + date_column + ")%20" + equality_denoter + "%20" + str(month)
    if day:
        start_filter = start_filter + "%20and%20day(" + date_column + ")%20" + equality_denoter + "%20" + str(day)

    
    return date_filter

# ODA FT API URL - build the URL based on the supplied ressource and filter
def get_oda_ft_api_url(ressource, filter = None):
    """Get ODA FT API URL

    Args:
        ressource (str): ODA FT ressource/table name
        filter (str): ODA FT API filter
        

    Returns:
        str: ODA FT API URL
    """
    
    api_url = "https://oda.ft.dk/api/" + ressource + "?$inlinecount=allpages"
    if filter:
        api_url = api_url + "&$filter=" + filter
    return api_url


# ODA FT API DATA - get the data from the ODA FT API based on the supplied url
def get_oda_ft_api_data(url):
    """Get ODA FT API data

    Args:
        url (str): ODA FT API URL

    Returns:
        dict: ODA FT API data
    """
    
    response = requests.get(url)
    response = response.json()
    return response["value"]


# run the script
if __name__ == "__main__":
    # ODA FT API ressource
    ressource = "Periode"
    filter = 'year(startdato)%20gt%202003%20'
    # ODA FT API URL
    url = get_oda_ft_api_url(ressource, filter)

    # ODA FT API data
    data = get_oda_ft_api_data(url)

    # print the data
    len(data)