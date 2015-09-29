# Detection function for Amiro, http://amirocms.com
from cmspwn.module import pwnfunc

@pwnfunc
def is_amirocms(cmspwn, response):
    identify_string = '<meta name="GENERATOR" content="\n -= Amiro.CMS (c) =- \n www.amiro.ru \n">'
    if identify_string in response.content:
       cmspwn.found  = True; cmspwn.Framework = 'AmiroCMS'; cmspwn.site = 'http://amirocms.com'
       return
