import json

# some JSON:
x =  '{"name":"John", "age":30, "city":"New York"}'
print(x)

# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


x = {
  "name": "John doe",
  "age": 70,
  "nationality":"jenyan",
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)