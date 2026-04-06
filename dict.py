info={
    "key":"value",
    "name":"shivam",
    "age":20,
    "contact":9123473084,
    "is_adult":True,
    12.99 :94.9
}
print(info)
print(info["name"]) #access value 
info["city"]="Bhopal" #add new key
print(info)
info["age"]=25 #update values 
print(info)
del info["contact"] # deleted keys 
print(info)
print(type(info))
null_dict={}
print(null_dict)
null_dict["name"]={"aapna college"}
print(null_dict)
# nested dictionary
student ={
    "name": "Shivam kumar",
    "subject":{
        "physics":97,
        "chemistry":98,
        "math":95
    }
}
print(student)

print(len(student)) # find length
print(len(list(student))) # find length through list
print(list(student.keys())) # prints keys 
print(list(student.values())) # prints values 
print(student.items())
pairs=list(student.items())
print(pairs[0])
print(student.get("name"))
print(student.get("name1"))
student.update({"city":"indore"})
print(student)
student.update({"subject":"english"})
print(student)