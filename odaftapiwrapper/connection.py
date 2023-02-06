import requests

# ODA FT API URL - build the URL based on the supplied ressource and filter
def get_url(ressource, filter = None):
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
def get_data(url):
    """Get ODA FT API data

    Args:
        url (str): ODA FT API URL

    Returns:
        dict: ODA FT API data
    """
    
    response = requests.get(url)
    response = response.json()
    return response["value"]