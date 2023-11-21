# API is application programming interface
# it means an eternal resourcce we can access
# use usually use the 'requests' library to acccess an API
# we used to use urllib (or urllib3)
# we must make sure the requests library is available to python
# pip install requests

import requests

def makeRequest():
    '''call an API'''
    url = 'https://jsonplaceholder.typicode.com/users/1'
    response = requests.get(url)
    return response.json() # convert the JSON data into a Python structure

if __name__ == '__main__':
    data = makeRequest()
    print(data)


