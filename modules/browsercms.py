# Identifies BrowserCMS based websites, http://www.browsercms.org/

def is_browsercms(response):
    identify_strings = ("""<meta name="generator" content="BrowserCMS""", )
    for id_string in identify_strings:
        if id_string in response.content:
            return True
    return False
