import requests
import json

class Sonnar_API(object):
    
    def __init__(self, token ):
        self.url = 'https://sonarcloud.io/api'
        self.token = token
    
    def retrieve_information_none (self,url):
        response = requests.get('https://sonarcloud.io/api/'+url,
                            headers={'Authorization': self.token)
        return response.json()
        
    def retrieve_information (self,url, parameters):
        response = requests.get('https://sonarcloud.io/api/'+url,
                            params=parameters,    
                            headers={'Authorization': self.token})
        return response.json()    
    
    @classmethod
    def get_projects(self):
        url = '/projects/search'
        return retrieve_information_none(url)
    
        
        
