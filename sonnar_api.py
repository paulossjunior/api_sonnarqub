import requests
import json

class Sonnar_API(object):
    url = 'https://sonarcloud.io/api'
    
    def __init__(self, token):
        self.token = token
    
    
    def retrieve_information (self,url):
        uri = self.url+url;
        print self.token
        response = requests.get(uri,
                            headers={'Authorization': self.token})
        return response.json()
    
    def get_projects(self):
        url = '/projects/search'
        return self.retrieve_information(url)
    
    '''
    class User(object):
    def __init__(self, name, username, *args, **kwargs):
        self.name = name
        self.username = username

import json
j = json.loads(your_json)
u = User(**j)
'''        
