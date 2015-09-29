# Detection function for AnchorCMS, www.1c-bitrix.ru
from cmspwn.module import pwnfunc
import re

@pwnfunc
def is_1C_Bitrix(cmspwn, response):
    pat = "(?:<link[^>]+components/bitrix|(?:src|href)=\"/bitrix/(?:js|templates))"
    match = re.search(pat, response.content)
    if match:
       cmspwn.found  = True; cmspwn.Framework = '1C-Bitrix'; cmspwn.site = 'http://www.1c-bitrix.ru'
       return

    #ok, maybe they removed the links, how about the headers
    if 'bitrix' in str(response.headers).lower():
       cmspwn.found  = True; cmspwn.Framework = '1C-Bitrix'; cmspwn.site = 'http://www.1c-bitrix.ru'
       return
