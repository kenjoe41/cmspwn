# Identifies Actionhero based websites, 'http://www.actionherojs.com'
from cmspwn.module import pwnfunc
import re

@pwnfunc
def is_actionhero(cmspwn,response):
    match = re.search("actionheroClient\\.js", response.content)
    if match:
        cmspwn.found = True; cmspwn.Framework = 'Actionhero';cmspwn.site = 'http://www.actionherojs.com'
        return

    if "actionhero API" in str(response.headers):
        cmspwn.found = True; cmspwn.Framework = 'Actionhero';cmspwn.site = 'http://www.actionherojs.com'
        return

