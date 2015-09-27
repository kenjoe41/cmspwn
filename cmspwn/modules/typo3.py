# Identifies Typo3 based websites, https://typo3.org/
from cmspwn.module import pwnfunc

@pwnfunc
def is_typo3(cmspwn,response):
    if "<meta name=\"generator\" content=\"TYPO3" in response.content:
        cmspwn.found  = True; cmspwn.Framework = 'Typo3'
        return
