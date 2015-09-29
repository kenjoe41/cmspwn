# Detection function for Liferay, http://www.liferay.com/
from cmspwn.module import pwnfunc

@pwnfunc
def is_liferay(cmspwn, response):
    identify_strings = ('var Liferay', 'Liferay.AUI', 'Liferay.ThemeDisplay', 'Liferay.Portlet')
    for id_string in identify_strings:
        if id_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'Liferay';cmspwn.site = 'http://www.liferay.com/'
           return
