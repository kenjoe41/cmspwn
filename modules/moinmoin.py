# Identifies MoinMoin cms based websites, http://moinmo.in/

def is_moinmoin(response):
    identify_strings = ('title="This site uses the MoinMoin Wiki software.">',
                        'title="MoinMoin is written in Python.">')
    for id_string in identify_strings:
        if id_string in response.content:
            return True
    return False
