# Detection function for Drupal.
def is_drupal(response):
	return 'Drupal.settings' in response.content
