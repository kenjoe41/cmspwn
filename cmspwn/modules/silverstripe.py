# detects silverstripe cms based websites, http://www.silverstripe.org/
from cmspwn.module import pwnfunc

@pwnfunc
def is_silverstripe(cmspwn,response):
    identify_strings = ('name="generator" content="SilverStripe', )
    for id_string in identify_strings:
        if id_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'Silverstripe'
           return
