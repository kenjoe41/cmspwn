# Detection function for AMPCMS, http://www.ampcms.org
#TODO: still needs more work
from cmspwn.module import pwnfunc

@pwnfunc
def is_ampcms(cmspwn, response):
    if 'AMP'.lower() in response.headers.get('set-cookie').split('=')[0].lower():
       cmspwn.found  = True; cmspwn.Framework = 'AMPCMS'; cmspwn.site = 'http://www.ampcms.org'
       return
