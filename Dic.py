import json

print("what would you like it to be called?")
name = input()
list1 = []
age = 18
num = 14
dictionary = {"number": num, "age": age}
x = dictionary.get("number")
print(x)
list1.append(str(age))
list1.append(str(num))
# adding it to the JSON file
jsonString = json.dumps(dictionary)
jsonFile = open(f"{name}.JSON", "w")
jsonFile.write(jsonString)
jsonFile.close()

# opening the file and bringing it into the file
with open(f"{name}.json", 'r') as f:
    data = json.load(f)
    print(data)
f.close()

'''
hello = 19
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": hello,
}
print(thisdict)
temp = data.pop(0)
# printing returned value from the JSON file
print(temp)
# adding it to a perminet variable then converting to a int
age_save = int(temp)
age_save += 1
# printing the new save
print(age_save)

temp = data.pop(0)
print(temp)
'''