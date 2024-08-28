person = { 
            "name" : "Joseph", 
            "occupation": "software developer",
            "address" : {
                "streetname" : "ABC street",
                "coordinates" : (0,10)
            },
            "tuple" : (0,10),
            "list" : [1,2,3,4,5]
          }

# # access 
# locations = person["address"]
# print(locations)

# street = person["address"]["streetname"]
# name = person["name"]
# print(name)
# print(f"{name} stays at the following coordinates {locations} at the street : {street}")
# # modify values 
# person["name"] = "Alice"
# name = person["name"]
# print(f"{name} stays at the following coordinates {locations}")

# # adding new key and value pairs 
# person["apartment"] = "Building 5A"
# print(person)

### in built operations 
## LOOPING 

for x in person:
    print(f"Key : {x} Value: {person[x]}")
    
for x in person.values():
    print(x)
    
for key,value in person.items():
    print(f'{key}: {value}')