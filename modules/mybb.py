# Detection function for MyBB
def is_mybb(response):
    answer = False
    if 'jscripts/prototype.js' in response.content:
        answer = True
    elif 'mybb[lastactive]' in response.cookies:
        answer = True
    elif "mybb[lastactive]" in response.cookies:
        answer = True
    return answer

