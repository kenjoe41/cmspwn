# Identifies BrowserCMS based websites, http://www.browsercms.org/
from cmspwn.module import pwnfunc

@pwnfunc
def is_browsercms(cmspwn,response):
    identify_string = '<meta name="generator" content="BrowserCMS'
    if identify_string in response.content:
       cmspwn.found  = True; cmspwn.Framework = 'BrowserCMS';cmspwn.site = 'http://www.browsercms.org/'
       return

