# Detection function for IPB, http://invisionpower.com/
def is_ipb(response):
    identify_strings = ("ipb.vars['base_url']", "ipb.vars['board_url']",
                        "ipb.vars['img_url']", "ipb.vars['loading_img']",
                        "ipb.vars['active_app']", "ipb.vars['upload_url']",
                        "title='Community Forum Software by Invision Power Services'>")
    for id_string in identify_strings:
        if id_string in response.content:
            return True
    return False
