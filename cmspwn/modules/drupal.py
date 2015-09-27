# Detection function for Drupal.
from cmspwn.module import pwnfunc, FOUND

@pwnfunc
def is_drupal(cmspwn,response):
        identify_string = 'Drupal.settings'
        if identify_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'Drupal'
           return
