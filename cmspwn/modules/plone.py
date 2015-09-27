# This module detects Plone based cms, https://plone.org/
from cmspwn.module import pwnfunc

@pwnfunc
def is_plone(cmspwn, response):
    identify_strings = ('<meta name="generator" content="Plone"',
                        '<form id="plonesearchform" name="searchform"',
                        "/resourceplone.formwidget",
                       )
    for identify_s in identify_strings:
        if identify_s in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'Plone'
           return
