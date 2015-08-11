# Detection function for SMF, http://www.simplemachines.org/
def is_smf(response):
    identify_strings = ("var smf_theme_url", "var smf_default_theme_url",
                        "var smf_scripturl", "var smf_images_url",
                        "var smf_charset", 'title="Simple Machines Forum"')
    for id_string in identify_strings:
        if id_string in response.content:
            return True
    return False
