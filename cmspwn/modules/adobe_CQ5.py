# Identifies adobeCQ5 based websites, http://adobe.com/products/cq.html
from cmspwn.module import pwnfunc
import re

@pwnfunc
def is_adobecq5(cmspwn,response):
    pat = "<div class=\"[^\"]*parbase|<div[^>]+data-component-path=\"[^\"+]jcr:"
    match = re.search(pat, response.content)
    if match:
        cmspwn.found = True; cmspwn.Framework = 'Adobe CQ5';cmspwn.site = 'http://adobe.com/products/cq.html'
        
