from sonnar_api import Sonnar_API
'''
#verificando o historico de violacao do projeto
parameters = {"component": "libebox_123","metrics":"ncloc,complexity,coverage,new_violations"}
response = requests.get('https://sonarcloud.io/api/measures/search_history',
                            params=parameters,    
                            headers={'Authorization': '6d6c5a6cdc8d04f976ba42671e18859683df840c'})


#print json.dumps(response_data, indent=4, sort_keys=True)

#Verificando a violacao dos componentes (arquivos) do projeto
parameters = {"component": "libebox_123","metricKeys":"ncloc,complexity,coverage,new_violations"}
response = requests.get('https://sonarcloud.io/api/measures/component_tree',
                            params=parameters,    
                            headers={'Authorization': '6d6c5a6cdc8d04f976ba42671e18859683df840c'})

#Verificando a violacao do componente (arquivo) do projeto
parameters = {"component": "libebox_123","metricKeys":"ncloc,complexity,coverage,new_violations"}
response = requests.get('https://sonarcloud.io/api/measures/component',
                            params=parameters,    
                            headers={'Authorization': '6d6c5a6cdc8d04f976ba42671e18859683df840c'})

#Verificando os componentes do projeto
parameters = {"qualifiers":"TRK"}
response = requests.get('https://sonarcloud.io/api/components/search',
                            params=parameters,    
                            headers={'Authorization': '6d6c5a6cdc8d04f976ba42671e18859683df840c'})

response_data = response.json()
print json.dumps(response_data, indent=4, sort_keys=True)
'''

USER_TOKEN = '6d6c5a6cdc8d04f976ba42671e18859683df840c'
sonnar_api = Sonnar_API(USER_TOKEN)
response_data = sonnar_api.get_projects()
print json.dumps(response_data, indent=4, sort_keys=True)