from odaftapiwrapper import filters, connection



# run the script
if __name__ == "__main__":
    # ODA FT API ressource
    ressource = "Periode"
    filter = filters.get_date_filter(date_column = 'startdato', equality_denoter = 'ge',year = 2003)
    # ODA FT API URL
    url = connection.get_url(ressource, filter)

    # ODA FT API data
    data = connection.get_data(url)

    # print the data
    len(data)