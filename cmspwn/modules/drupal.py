# Detection function for Drupal, https://www.drupal.org/
from cmspwn.module import pwnfunc

@pwnfunc
def is_drupal(cmspwn,response):
        identify_string = 'Drupal.settings'
        if identify_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'Drupal';cmspwn.site = 'https://www.drupal.org/'
           return
