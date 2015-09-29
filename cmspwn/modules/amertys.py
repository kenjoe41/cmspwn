# Detection function for Ametys, http://ametys.org
from cmspwn.module import pwnfunc

@pwnfunc
def is_ametys(cmspwn, response):
    identify_string = '<meta content="Ametys v3 '\
               '(http://www.ametys.org) - The Smart Web CMS" name="generator" />'
    if identify_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'Ametys';cmspwn.site = 'http://www.ametys.org'
           return
