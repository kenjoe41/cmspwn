# Identifies BrowserCMS based websites, http://www.browsercms.org/
from cmspwn.module import pwnfunc, FOUND

@pwnfunc
def is_browsercms(cmspwn,response):
    identify_strings = ("""<meta name="generator" content="BrowserCMS""", )
    for id_string in identify_strings:
        if id_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'BrowserCMS'
           return

