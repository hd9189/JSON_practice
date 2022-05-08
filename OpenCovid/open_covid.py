from matplotlib.legend import Legend
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
    ax = df.plot.bar(
        x='Province',
        y='Population',
        rot=45,
        legend=False
    )
    ax.set_title()
    plt.show()

def millions(x, pos):
    return f'{x/1000000:,.0f}' #display by million

def help():
    df = pd.read_csv('Population.csv')
    print(df)
    ax = df.plot.bar(
        x='Province',
        y='Population',
        rot=45,
        legend=False
    ) #plots df csv
    ax.set_title('Population by Province (in millions)', fontsize=16)
    ax.set_xlabel('Province', fontsize=14)
    ax.set_ylabel('Population', fontsize=14)
    ax.yaxis.set_major_formatter(millions) #millions is self made function, formats the y axis
    plt.show()

# population()
# help()

def thousands(x, pos):
    return f'{x:,.0f}'

def province(prov):
    url = 'https://api.opencovid.ca/timeseries'
    response = requests.get(url)
    json_data = json.loads(response.text)
    df = pd.read_json(json.dumps(json_data['data']['cases'])) #dumps converts json into string
    ax = df.query(f'region == "{prov}"').plot( #creates a line graph
        x = 'date',
        y = 'value_daily',
        rot = 45,
        legend = False
    )
    ax.set_title(f'Daily Cases in {prov}')
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Number of People', fontsize=14)
    ax.yaxis.set_major_formatter(thousands)
    plt.show()

provinces = ["AB", "BC", "ON", "MB","NB", "NL", "NS", "NT", "NU", "PE", "QC", "SK", "YT"]
prov = input(f"Choose a province {provinces}: ")
while prov not in provinces:
    prov = input(f"Choose a province {provinces}: ")
province(prov)