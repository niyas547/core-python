import json
with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)
print(len(data))
india=[country for country in data if country.get("name")=="India"]
print(india)
india_borders=[nation.get("borders") for nation in data if nation.get("name")=="India"]
print("indian borders=",india_borders)
china_capital=[china.get("capital") for china in data if china.get("name")=="China"]
print("capital of china=",china_capital)
australia_population=[aus.get("population") for aus in data if aus.get("name")=="Australia"]
print("population of australia=",australia_population)
nepal_currency=[nepal.get("currencies") for nepal in data if nepal.get("name")=="Nepal"].pop()
currncy_name=[name.get("name")for name in nepal_currency ]
print("nepalese currency=",currncy_name)

bhutan_languages=[bhutan.get("languages") for bhutan in data if bhutan.get("name")=="Bhutan"].pop()
lan_name=[lan.get("name") for lan in bhutan_languages]
print("bhutan languages =",lan_name)

most_populated=max(data,key=lambda pop:pop.get("population"))
print("most populated country=",most_populated)
low_populated=min(data,key=lambda pop:pop.get("population"))
print("low populated country=",low_populated)
india_borders_names=[country.get("borders") for country in data if country.get("name")=="India"].pop()
print(india_borders_names)
border_names=[name.get("name") for name in data if name.get("alpha3Code") in india_borders_names]
print(border_names)