# Dectection function for Joomla, https://www.joomla.org/
from cmspwn.module import pwnfunc

@pwnfunc
def is_joomla(cmspwn,response):
	if 'joomla.css' in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'Joomla'; cmspwn.site = 'https://www.joomla.org/'
           return
