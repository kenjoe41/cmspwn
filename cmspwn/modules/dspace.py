# Detection function for DSpace, http://www.dspace.org
from cmspwn.module import pwnfunc

@pwnfunc
def is_dspace(cmspwn, response):
    identify_string = '<meta name="Generator" content="DSpace'
    if identify_string in response.content:
       cmspwn.found  = True; cmspwn.Framework = 'DSpace';cmspwn.site = 'http://www.dspace.org'
       return
