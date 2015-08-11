# Identifies Typo3 based websites, https://typo3.org/
def is_typo3(response):
    return """<meta name="generator" content="TYPO3""" in response.content

