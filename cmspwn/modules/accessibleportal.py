# Detection function for Accessible Portal, http://www.accessibleportal.com
from cmspwn.module import pwnfunc

@pwnfunc
def is_accessibleportal(cmspwn, response):
    identify_string = '<meta name="generator" content="Accessible Portal'
    if identify_string in response.content:
       cmspwn.found  = True; cmspwn.Framework = 'Accessible Portal'; cmspwn.site = 'http://www.accessibleportal.com'
       return
