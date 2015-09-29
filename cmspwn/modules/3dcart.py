# Detection function for 3dCart, www.3dcart.com
from cmspwn.module import pwnfunc
import re

@pwnfunc
def is_3dcart(cmspwn, response):
    pat = "(?:twlh(?:track)?\\.asp|3d_upsell\\.js)"
    match = re.search(pat, response.content)
    if match:
       cmspwn.found  = True; cmspwn.Framework = '3dCart'; cmspwn.site = 'http://www.3dcart.com'
       return

    if '3dvisit' in response.headers.get('set-cookie'):
       cmspwn.found  = True; cmspwn.Framework = '3dCart'; cmspwn.site = 'http://www.3dcart.com'
       return
