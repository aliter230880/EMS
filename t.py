import requests 
import json 
url='https://www.foreo.com/api/v3.8/users/send_activation_code' 
payload={'data':{'type':'mail','attributes':{'id':'fancy@mail.ru','code':'Konfeta83!'}}} 
keys=['ZGV2OlAwd2Ehbw==','ffy','foreo',''] 
for key in keys: 
print(key) 
