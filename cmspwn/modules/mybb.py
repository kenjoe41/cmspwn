# Detection function for MyBB
from cmspwn.module import pwnfunc

@pwnfunc
def is_mybb(cmspwn,response):
    identify_strings = ('jscripts/prototype.js', 'mybb[lastactive]', "mybb[lastactive]")
    if identify_string in response.content:
        cmspwn.found  = True; cmspwn.Framework = 'MyBB';cmspwn.site = 'http://www.mybb.com/'
        return
