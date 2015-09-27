# Identifies Wolf CMS based websites, http://www.wolfcms.org/

from cmspwn.module import pwnfunc

@pwnfunc
def is_wolfcms(cmspwn, response):
    if '<a href="http://www.wolfcms.org/" title="Wolf CMS">' in response.content:
        cmspwn.found  = True; cmspwn.Framework = 'Wolf CMS'
        return
