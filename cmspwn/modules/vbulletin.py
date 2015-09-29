#Detection function for vBulletin, http://www.vbulletin.org/
from cmspwn.module import pwnfunc

@pwnfunc
def is_vbulletin(cmspwn,response):
    identify_strings = ('id="vbulletin_html"', 'content="Vbulletin"',
                        '<meta name="generator" content="vBulletin', )
    for id_string in identify_strings:
        if id_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'vBulletin'; cmspwn.site = 'http://www.vbulletin.org/'
           return
