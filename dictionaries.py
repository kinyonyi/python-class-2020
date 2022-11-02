import json
person = {
    "name":"isaac",
    "age":25,
    "school":"makerere"
}
print(person['school'])
print(person['name'])
#dictionary methods
person.update({"school":"ugandan"})
person["nationality"] = "ugandan"
del person["nationality"]
del person["school"]
print(json.dumps(person, indent=2))
print(person.keys())
print(person.values())
print(person.items())
for x, y in person.items():
    print(x,y)
person.setdefault("village","kampala")
print(person)
person.clear()
print(person)
people = [
    {"name":"isaac","age":28},
    {"name":"jonah","age":25},
    {"name":"emma","age":20},
]
names = []
ages = []
for per in people:
    names.append(per['name'])
    ages.append(per['age'])
print(names)
print(ages)