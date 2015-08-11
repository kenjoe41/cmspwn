#Detection function for vBulletin, http://www.vbulletin.org/
def is_vbulletin(response):
    identify_strings = ('id="vbulletin_html"', 'content="Vbulletin"',
                        '<meta name="generator" content="vBulletin', )
    for id_string in identify_strings:
        if id_string in response.content:
            return True
    return False
