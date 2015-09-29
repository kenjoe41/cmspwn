# Detection function for AnchorCMS, http://anchorcms.com
from cmspwn.module import pwnfunc

@pwnfunc
def is_anchorcms(cmspwn, response):
    identify_string = '<meta name="generator" content="Anchor CMS">'
    if identify_string in response.content:
       cmspwn.found  = True; cmspwn.Framework = 'AnchorCMS'; cmspwn.site = 'http://anchorcms.com'
       return
