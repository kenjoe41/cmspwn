#!/usr/bin/python
#
# CMSpwn v0.1
#
# Project   : CMSpwn
# Module    : Main
# Author    : Phage
# Rewritten : Kenjoe41


# Import the needed libraries.
import re, os, sys
import argparse
import requests
import imp
import cfscrape
from urlparse import urlparse

# Import the local modules
from cmspwn import report, error, module
requests.packages.urllib3.disable_warnings()

report = report.Report()
modules = module.Modules()

class engine():
    def __init__(self):
        self.callables = set()
        self.found = False
        self.Framework = ''
        self.site = ''

        #functions to scan the html
        self.functions = []
        self.filenames = {}

    @staticmethod
    def is_callable(obj):
        if not callable(obj):
            return False
        if (hasattr(obj, 'cms')):
            return True
        return False
            

    def setup(self):
        msg = "Welcome to CMSPwn. Loading modules...";report.info(msg)
        self.filenames = modules.get_modules()
        modulez = []
        error_count = 0
        for name, filename in module.iteritems(self.filenames):
            try:
                modul = imp.load_source(name, filename)
            except Exception as e:
                error_count = error_count + 1
                filename, lineno = error.get_err_file_and_line()
                rel_path = os.path.relpath(filename, os.path.dirname(__file__))
                raising_stmt = "%s:%d" % (rel_path, lineno)
                msg="Error in {} setup procedure:{} ({})".format(name, e, raising_stmt);report.error(msg)
            else:
                for value in module.itervalues(vars(modul)):
                    if self.is_callable(value):
                        self.callables.add(value)

                modulez.append(name)

        if modulez:
            msg = "\nRegistered %d modules"%len(modulez); report.info(msg)
            msg = "\n%d failed to load."%error_count; report.medium(msg)
        else:
            msg = '\nWarning: Couldn\'t find any modules'; report.high(msg)
        self.collect_commands()

    def collect_commands(self):
        for func in self.callables:
            if hasattr(func, 'cms'):#func.cms:, prefered to use hasattr()
                self.functions.append(func)
        msg = 'Found %d functions'%len(self.functions); report.info(msg)

    
    def call(self, func,cmspwn, html):
        try:
                exit_code = func(cmspwn, html)
        except:
            pass

    def pwn(self, html):
        num_funcs = len(self.functions)
        while self.found == False and num_funcs > 0:
            for func in self.functions:
                self.call(func,self, html)
                num_funcs -= 1
        return self.Framework, self.site

class CMSpwn(engine, object):
    def __init__(self, args):
        engine.__init__(self)
        self.args = args

    def cms_identifier(self):
        """ Identifies the target's content management system. """
        engine.setup(self)
        
        targets = [target for target in self.args.target if target.strip()]
        error_count = 0
        for url in targets:
            self.sanitize_url(url)
            msg = "Getting source for {}".format(self.url); report.low(msg)
            headers = {'User-Agent': "Mozilla/5.0 (X11; Fedora; Linux i686;" +\
			"rv:40.0) Gecko/20100101 Firefox/40.1"}
            response = None
            try:
                response = requests.get(self.url, headers=headers, verify=False)
                if "Checking your browser before accessing" in response.content:
                    msg ="Site: {} is using cloudflare. "\
                         "Trying to bypass cloudflare protection.".format(self.url);report.medium(msg)
                    #damn cloudflare, lets see if how to circumvert it. 
                    #TODO: Ask for permision since executing JS might be a security issue.
                    # https://github.com/Anorov/cloudflare-scrape
                    cfscraper = cfscrape.create_scraper()
                    response = cfscraper.get(self.url)
            except Exception as e:
                #print e
                error_count += 1
                msg="Something went wrong while getting ({}), moving on...".format(self.url);report.error(msg)
                if error_count > 3:
                    msg = "Too many error. Exiting..."; report.error(msg)
                    sys.exit()
            
            framework, site = engine.pwn(self,response)
            if framework:
                report.info("This is a website based on: {0} from {1}".format(framework, site))
            else:
                report.high("Failed to determine CMS of site.")
    def sanitize_url(self,url):
        self.url = url
        up = urlparse(self.url)
        if not up.scheme:
            self.url = "http://{0}".format(up.geturl())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="CMSpwn")
    parser.add_argument('-t', '--target', help="specifies the target website",
                        nargs="*", required=True)

    args = parser.parse_args()
    cmspwn = CMSpwn(args)
    cmspwn.cms_identifier()
