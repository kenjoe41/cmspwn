# Detection function for IPB, http://invisionpower.com/
from cmspwn.module import pwnfunc

@pwnfunc
def is_ipb(cmspwn, response):
    identify_strings = ("ipb.vars['base_url']", "ipb.vars['board_url']",
                        "ipb.vars['img_url']", "ipb.vars['loading_img']",
                        "ipb.vars['active_app']", "ipb.vars['upload_url']",
                        "title='Community Forum Software by Invision Power Services'>",
                        "class='ipbfs_login_col'>")
    for id_string in identify_strings:
        if id_string in response.content:
           cmspwn.found  = True; cmspwn.Framework = 'IPB';cmspwn.site = 'http://invisionpower.com/'
           return
