# Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

print(len(thisdict))
'''
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
'''
y = thisdict.get("brand")
print(y)
x = thisdict.get("name", "nothing")
print(x)

x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)


print("add")
print("*************")
thisdict["size"] = "3m"

print("update")
print("*************")
print(thisdict)
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)

print("remove")
print("*************")
thisdict.pop("model")
print(thisdict)

del thisdict["brand"]
print(thisdict)

thisdict.clear()
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("copy")
print("*************")

mydict = thisdict.copy()
print(mydict)

print("nested")
print("*************")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
print(myfamily["child2"]["name"])
