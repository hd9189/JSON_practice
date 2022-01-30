#JSON(JavaScript Object Notation)
# # JSON is nested lists and dictionaries
# # JSON is a syntax(text) for storing and exchanging data

'''peoples = [
    {
        "name": "John",
        "city": "Ottawa",
        "age": 30
    },
    {
        "name": "Sarah",
        "city": "Toronto",
        "age": 31
    },
    {
        "name": "John",
        "city": "Ottawa",
        "age": 30
    }]
for i in peoples:
    print()
    for x,y in i.items():
        print(x+": "+str(y))'''

'''data = {
    "peoples":
    [
        {
            "name": "John",
            "city": "Ottawa",
            "age": 30
        },
        {
            "name": "Sarah",
            "city": "Toronto",
            "age": 31
        },
        {
            "name": "John",
            "city": "Ottawa",
            "age": 30
        }
    ]
}


for dict in data["peoples"]:
    print()
    for key,term in dict.items():
        print(key+": "+str(term))'''

import json

'''str_json = '[{"name": "John", "city": "Ottawa", "age": 30}, {"name": "Smith", "city": "Toronto", "age": 31}]'
#convert into json objet
data = json.loads(str_json)
print(data[0]["age"])'''

#write JSON to a File

'''data = {
    "peoples":
    [
        {
            "name": "John",
            "city": "Ottawa",
            "age": 30
        },
        {
            "name": "Sarah",
            "city": "Toronto",
            "age": 31
        },
        {
            "name": "John",
            "city": "Ottawa",
            "age": 30
        }
    ]
}'''


'''with open("data.json","w") as w_file:
    json.dump(data, w_file)'''

'''covid_stats = {"summary":[{"active_cases":351850,"active_cases_change":-12100,"avaccine":286834.0,"cases":12531,"cumulative_avaccine":73432663.0,"cumulative_cases":2748537,"cumulative_cvaccine":29656509.0,"cumulative_deaths":31359.0,"cumulative_dvaccine":86732116.0,"cumulative_recovered":2365328.0,"cumulative_testing":44620348.0,"cvaccine":19511.0,"date":"15-01-2022","deaths":109.0,"dvaccine":0.0,"province":"Canada","recovered":24522.0,"testing":63717.0,"testing_info":"NULL"}],"version":"2022-01-15 21:38 EST"}
with open("data.json","w") as w_file:
    json.dump(covid_stats, w_file)'''

#
with open("data.json", "r") as r_file:
    data = json.load(r_file)

for dict in data["summary"]:
    print()
    for key,term in dict.items():
        if isinstance(term, float) or isinstance(term, int): print(key+": "+ f"{term:,}")

        else: print(key+": "+ str(term))