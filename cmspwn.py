#!/usr/bin/python
#
# CMSpwn v0.1
#
# Project   : CMSpwn
# Module    : Main
# Author    : Phage
#

# Import the needed libraries.
import re
import argparse
import requests
import urlparse

# Import the local modules
from modules.wordpress import is_wordpress
from modules.joomla import is_joomla
from modules.drupal import is_drupal
from modules.smf import is_smf
from modules.mybb import is_mybb
from modules.vbulletin import is_vbulletin
from modules.ipb import is_ipb
from modules.plone import is_plone
from modules.browsercms import is_browsercms
from modules.typo3 import is_typo3
from modules.wolfcms import is_wolfcms
from modules.moinmoin import is_moinmoin
from modules.silverstripe import is_silverstripe

class CMSpwn(object):
    def __init__(self, args):
        self.args = args

    def cms_identifier(self):
        """ Identifies the target's content management system. """
        targets = [target for target in self.args.target if target.strip()]
        for url in targets:
            up = urlparse.urlparse(url)
            if not up.scheme:
                url = "http://{0}".format(up.geturl())

            headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6;"+\
                                        " rv:25.0) Gecko/20100101 Firefox/28.0"}
            response = requests.get(url, headers=headers, verify=False)

            systems = [
            ('Wordpress', is_wordpress),
            ('Joomla', is_joomla),
            ('Drupal', is_drupal),
            ('SMF', is_smf),
            ('MyBB', is_mybb),
            ('vBulletin', is_vbulletin),
            ('IP.Board', is_ipb),
            ("Plone", is_plone),
            ("BrowserCMS", is_browsercms),
            ("TYPO3", is_typo3),
            ("Wolf CMS", is_wolfcms),
            ("MoinMoin", is_moinmoin),
            ("SilverStripe", is_silverstripe),
            ]

            # Prints the result.
            for name, fn in systems:
                if fn(response):
                    print "This is a website based on: {0}".format(name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="CMSpwn")
    parser.add_argument('-t', '--target', help="specifies the target website",
                        nargs="*", required=True)

    args = parser.parse_args()
    cmspwn = CMSpwn(args)
    cmspwn.cms_identifier()
