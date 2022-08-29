# get=retrieve/read
# post=create
# put/patch=update
# delete=delete


from mobiles.models import mobiles
class Mobiles:
    def get(self):
        return mobiles
    def post(self,*args,**kwargs):
        mobile=kwargs.get("data")
        mobiles.append(mobile)
        return mobile

all_mobile=Mobiles()
print(all_mobile.get())
data=  {"id": 1010, "name": "samsungA56", "band": "5g", "display": "LED", "price": 29000, "brand": "samsung"}
print(all_mobile.post(data=data))