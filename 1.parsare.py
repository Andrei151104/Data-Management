import json

#Versiunea 2 - citire din fisier + parsare 
with open("euro_2024.json") as file_handler:
    #citesc continutul
    continut = file_handler.read()
    print(type(continut),continut)
    #parsez continutul
    continut_parsat = json.loads(continut)
    print(type(continut_parsat),continut_parsat)

#Vesiunea 2 -parsare la citire(direct)
with open("euro_2024.json") as file_handler:
    continut_parsat = json.load(file_handler)
    print(type(continut_parsat),continut_parsat)