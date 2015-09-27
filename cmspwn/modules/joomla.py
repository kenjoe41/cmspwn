# Dectection function for Joomla.
from cmspwn.module import pwnfunc

@pwnfunc
def is_joomla(cmspwn,response):
	if 'joomla.css' in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'Joomla'
           return
