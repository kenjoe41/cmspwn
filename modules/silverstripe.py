# detects silverstripe cms based websites, http://www.silverstripe.org/
def is_silverstripe(response):
    identify_strings = ('name="generator" content="SilverStripe', )
    for id_string in identify_strings:
        if id_string in response.content:
            return True
    return False
