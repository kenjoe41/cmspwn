# Identifies MoinMoin cms based websites, http://moinmo.in/
from cmspwn.module import pwnfunc

@pwnfunc
def is_moinmoin(cmspwn,response):
    identify_strings = ('title="This site uses the MoinMoin Wiki software.">',
                        'title="MoinMoin is written in Python.">')
    for id_string in identify_strings:
        if id_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'MoinMoin'; cmspwn.site = 'http://moinmo.in'
           return
