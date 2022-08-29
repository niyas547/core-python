frameworks=[
    {"fwname":"django","language":"python","rating":5},#fw
    {"fwname": "flask", "language": "python", "rating": 3},
    {"fwname": "angular", "language": "typescript", "rating": 5},
    {"fwname": "react", "language": "javascript", "rating": 4},
    {"fwname": "spring", "language": "java", "rating": 4},
    {"fwname": "ASP", "language": "c#", "rating": 5},

]


fw_name=[fw.get("fwname") for fw in frameworks]
print(fw_name)

language=[fw.get("language") for fw in frameworks]
print(language)

most_rated=[fw.get("fwname") for fw in frameworks if fw.get("rating")>4 ]        #if "fw" print all >4
print(most_rated)

py_name=[fw.get("fwname") for fw in frameworks if fw.get("language")=="python"]
print(py_name)

high_rated=max(frameworks,key=lambda fw:fw.get("rating"))
print(high_rated)

low_rated=min(frameworks,key=lambda fw:fw.get("rating"))
print(low_rated)
