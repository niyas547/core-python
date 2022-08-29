mobiles = [
    {"id": 1000, "name": "samsungA52", "band": "4g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1001, "name": "samsungA52s", "band": "5g", "display": "AMoLED", "price": 32000, "brand": "samsung"},
    {"id": 1002, "name": "redminote10", "band": "4g", "display": "led", "price": 17000, "brand": "redmi"},
    {"id": 1003, "name": "redminote11pro", "band": "5g", "display": "superAMOLED", "price": 20000, "brand": "redmi"},
    {"id": 1004, "name": "samsungA72", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1005, "name": "samsungA53", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1006, "name": "samsungm52", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1007, "name": "samsungm53", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1008, "name": "samsungA22", "band": "5g", "display": "AMOLED", "price": 27000, "brand": "samsung"},
    {"id": 1009, "name": "iphone13", "band": "5g", "display": "AMOLED", "price": 97000, "brand": "apple"},
    {"id": 1010, "name": "oneplusnordce2", "band": "5g", "display": "AMOLED", "price": 23000, "brand": "oneplus"}

]
# 1
mob_name=[mob.get("name") for mob in mobiles]
print(mob_name)
# 2
mob_brand=[mob.get("brand") for mob in mobiles]
print(mob_brand)
# 3
mob_sam=[mob for mob in mobiles if mob.get("brand")=="samsung"]
print(mob_sam)
# 4
mob_cash=[mob.get("name") for mob in mobiles if mob.get("price")>28000]
print(mob_cash)
# 5
mob_cash_sam=[mob.get("name") for mob in mobiles if mob.get("price")>25000 and mob.get("brand")=="samsung" and mob.get("band")=="4g"]
print(mob_cash_sam)
# 6
mob_cash_dis=[mob.get("name") for mob in mobiles if mob.get("price")>15000 and mob.get("display")=="led"]
print(mob_cash_dis)
# 7
mob_price_max=max(mobiles,key=lambda mob:mob.get("price"))
print(mob_price_max)
# 8
mob_price_min=min(mobiles,key=lambda mob:mob.get("price"))
print(mob_price_min)
# 9
mobiles.sort(key=lambda mob:mob.get("price"))
print(mobiles)
# 10
mobiles.sort(key=lambda mob:mob.get("price"),reverse=True)
print(mobiles)
#11 cheapest in samsung
mob_sam=[mob for mob in mobiles if mob.get("brand")=="samsung"]
a=min(mob_sam,key=lambda mob:mob.get("price"))
print(a)
# 12
two_details=[[mob.get("name"),mob.get("price")] for mob in mobiles if mob.get("band")=="5g"]
print(two_details)
