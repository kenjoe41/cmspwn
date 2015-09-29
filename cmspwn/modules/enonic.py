# Detection function for Enonic, https://enonic.com/
from cmspwn.module import pwnfunc

@pwnfunc
def is_enonic(cmspwn, response):
    identify_string = '<meta name="generator" content="Enonic CMS"'
    if identify_string in response.content:
       cmspwn.found  = True; cmspwn.Framework = 'Enonic';cmspwn.site = 'https://enonic.com/'
       return
