# Detection function for 2z Project, http://2zproject-cms.ru/
from cmspwn.module import pwnfunc

@pwnfunc
def is_2z_project(cmspwn, response):
    identify_string = '<meta name="Generator" content="2z project'
    if identify_string in response.content:
       cmspwn.found  = True; cmspwn.Framework = '2z Project'; cmspwn.site = 'http://2zproject-cms.ru/'
       return
