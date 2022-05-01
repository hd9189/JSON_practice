import requests, json
import pandas as pd
#pylot is a function within matplotlib, so we import that specifically
# import matplotlib.pyplot as plt
# from matplotlib import pyplot

# import matplotlib
# matplotlib.pyplot.show()

# from matplotlib import pyplot
# pyplot.show()

from matplotlib import pyplot as plt
plt.show()

#the same as text file

# url = 'https://api.opencovid.ca/other?stat=prov'
# response = requests.get(url)

# #loads a dictionary, takes the first layer of data structure, creates the json structure from the raw data
# json_data = json.loads(response.text)

# for province in json_data['prov']:
#     if province["pop"] != "NULL":
#         #prints no decimal points, and with thousand seperator
#         print(f'{province["province_full"]}: {province["pop"]:,.0f}\n')

def population():
    url = 'https://api.opencovid.ca/other?stat=prov'
    response = requests.get(url)
    json_data = json.loads(response.text)
    #need to get rid of null because it won't work with nulls
    json_data['prov'].pop() #! data cleaning, deletes the very last province because its null
    #read_json is a function in pandas, and it reads the string from the json.dumps which creates a string of a json file
    #uses each key from dictionary as the column
    df = pd.read_json(json.dumps(json_data['prov'])) #dataset or data frame in pandas
    #prints the data set in a more organized manner
    print(df)
    #creaters a plot and sets the x and y axis
    df.plot.bar(
        x='province',
        y='pop'
    )
    plt.show()

population()