# This module detects Plone based cms, https://plone.org/
def is_plone(response):
    identify_strings = ('<meta name="generator" content="Plone"',
                        '<form id="plonesearchform" name="searchform"',
                        "/resourceplone.formwidget",
                       )
    for identify_s in identify_strings:
        if identify_s in response.content:
            return True
    return False

