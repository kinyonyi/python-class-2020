#string methods
my_string = "hello david, how are you today"
print(len(my_string))#this returns the length of the string
print(my_string.replace("david","hope"))#replaces part of string
print(my_string.title())
print(my_string.upper())
print(my_string.lower())
print(my_string[0:11])
print(my_string.find("h"))
print(my_string.rfind("h"))
print(my_string[0:my_string.rfind("d")+1])
print(my_string.split())
print("emma" in my_string)
print(my_string.count("david"))
string_two = " hei {age} {county}".format(age = 20, county = "kampala")
print(string_two)
print(my_string + string_two)
print(my_string.endswith("today"))
print(my_string.startswith("today"))

