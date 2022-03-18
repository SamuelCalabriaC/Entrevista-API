from sys import stderr
import requests


class ApiService:
    endpoint = 'https://jsonplaceholder.typicode.com/todos/'

    def __init__(self):
        pass

    # Calls get method.
    def run(self):
        print('Running ApiService', file=stderr)
        return self.__get()

    # GET request to endpoint
    def __get(self):
        print('- Sending Get Request to the Endpoint')
        r = requests.get(self.endpoint)
        if r.status_code == 200:
            print('- GET Request Status Code: ' + str(r.status_code))
            return r.json()
        else:
            return 'There is something wrong.'
