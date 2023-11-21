# API is application programming interface
# it means an eternal resource we can access
# use usually use the 'requests' library to acccess an API
# we used to use urllib (or urllib3)
# we must make sure the requests library is available to python
# pip install requests

import requests

def makeRequest(whichUser):
    '''call an API'''
    # wevcan use any available end-point
    url = f'https://jsonplaceholder.typicode.com/users/{whichUser}'
    # it is a really good idea to surround requests with try block
    try:
        response = requests.get(url) # or post, update, put ...
        # we might retrieve text, xml, html json ...
        # NB this URL will only return JSON
        return response.json() # convert the JSON data into a Python structure
    except Exception as e:
        return f'Something went wrong {e}'

if __name__ == '__main__':
    id = input('Which user ID? ') # id can be 1-9
    data = makeRequest(id)
    print(data)



