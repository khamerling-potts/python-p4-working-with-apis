import requests
import json


# # HAD TO USE DIFFERENT API - NYC ONE WAS NOT PUBLIC
# class GetBreweries:
#     def get_breweries(self):
#         URL = "https://api.openbrewerydb.org/v1/breweries?by_city=bethesda"

#         response = requests.get(URL)
#         return response.content

#     def brewery_names(self):
#         # we use the JSON library to parse the API response into nicely formatted JSON
#         breweries_list = []
#         breweries = json.loads(self.get_breweries())
#         for brewery in breweries:
#             breweries_list.append(brewery["name"])

#         return breweries_list


# breweries = GetBreweries()
# names = breweries.brewery_names()

# for name in set(names):
#     print(name)

# # breweries = GetBreweries().get_breweries()
# # print(breweries)


class GetPrograms:
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)
        return response.content

    def program_agencies(self):
        # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list


# programs = GetPrograms().get_programs()
# print(programs)

programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
    print(agency)
