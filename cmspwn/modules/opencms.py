# Identifies OpenCMS based websites, http://www.opencms.org
from cmspwn.module import pwnfunc
import re

@pwnfunc
def is_opencms(cmspwn,response):
    match = re.search(r'href="/opencms/', response.content)
    if match:
        cmspwn.found = True; cmspwn.Framework = 'OpenCMS';cmspwn.site = 'http://opencms.org'
        
