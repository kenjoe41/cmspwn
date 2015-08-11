# Dectection function for Joomla.
def is_joomla(response):
	if 'joomla.css' in response.content:
		return True
