# Identifies Wolf CMS based websites, http://www.wolfcms.org/

def is_wolfcms(response):
    return '<a href="http://www.wolfcms.org/" title="Wolf CMS">' in response.content
