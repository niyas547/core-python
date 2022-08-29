import json
with open("users.json") as f:
    data=json.load(f)
print(data)
names=[user.get("name") for user in data]
print(names)
salary=[user.get("name") for user in data if user.get("salary")>40000]
print(salary)
hr_users=[user.get("name") for user in data if user.get("department")=="hr"]
print(hr_users)
high_salary=max(data,key=lambda user:user.get("salary"))
print(high_salary)
low_salary=min(data,key=lambda user:user.get("salary"))
print(low_salary)
data.sort(key=lambda user:user.get("salary"),reverse=True)
print(data)
