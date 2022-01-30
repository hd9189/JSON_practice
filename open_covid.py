import requests, json
import pandas as pd
import matplotlib as plt

#the same as text file

url = 'https://api.opencovid.ca/other?stat=prov'
response = requests.get(url)

json_data = json.loads(response.text)

for province in json_data['prov']:
    if province["pop"] != "NULL":
        #prints no decimal points, and with thousand seperator
        print(f'{province["province_full"]}: {province["pop"]:,.0f}\n')
