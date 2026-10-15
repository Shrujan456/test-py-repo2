#Dictionary

info={
    "name": "John",
    "subjects":["Maths","Science","English"], #list inside a dictionary
    "topics":("dict","set"), #tuple inside a dictionary
    "learning": "Python",
    "age": 25,
    "is_adult": True,
    "marks":94.4
}

print(info)
print(type(info))
print(info["name"])
print(info["subjects"])
print(info["topics"])
print(info["age"])
#print(info["surname"])#this will give us an error because there is no key called "surname" in the dictionary

info["name"]="sharadha" #we can change the value of a key in a dictionary
info["surname"]="kumari"#we can add a new key-value pair to the dictionary
print(info)

null_dict={} #empty dictionary
print(null_dict)

#Nested dictionary

student={
    "name": "John",
    "subjects": {
        "Maths": 90,
        "Science": 85,
        "English": 95
    }
}
print(student["subjects"])
print(student["subjects"]["Maths"])

print(student.keys())#this will give us all the keys in the dictionary
#We can't call nested values directly using keys() method, we need to access the nested dictionary first and then call the keys() method on it

print(student.keys())
print(student.values())

#We can do type casting in dictionary

#float(9)
#print(list(student.keys()))
print(len(student))
print(len(student.keys())) #this will give us the number of keys in the dictionary

#print(list(student.keys())) #this will give us a list of all the keys in the dictionary
#print(list(student.values())) #this will give us a list of all the values in the dictionary
print(student.items())

# pairs=list(student.items())
# print(pairs[0])
# print(pairs[1])

print(student["name"]) #this will give us the value of the key "name" in the dictionary, if the key is not present in the dictionary, it will give us an error
print(student.get("name")) #this will give us the value of the key "name" in the dictionary, if the key is not present in the dictionary

#print(student["name2"]) #this will give us an error because there is no key called "name2" in the dictionary
#print(student.get("name2")) #this will give us None instead of an error because there is no key called "name2" in the dictionary

#We are using get() method to avoid getting an error.

new_dict={"city" : "Delhi"}
student.update(new_dict) #this will add the key-value pair from new_dict to student dictionary, if the key is already present in the student dictionary, 
print(student)

#Sets in python

collection={1,2,3,4}
print(collection) 
print(type(collection))

collection={1,2,3,4,4,3,2,1,"hello","world","world",7,8,7} #sets do not allow duplicate values, so it will only store unique values. And the elements are stored in an unordered way.
print(collection)
print(type(collection))
print(len(collection)) #this will give us the number of unique elements in the set

collection={}
print(type(collection)) #this is not a set, this is a dictionary because we have used curly braces to create

collection=set() #this is how we can create an empty set
print(type(collection))

collection=set()
collection.add(1)
print(collection)
collection.add(2)
print(collection)
collection.add(2)
print(collection) #this will not add 2 again because sets do not allow duplicate values
collection.remove(1) #this will remove the value 1 from the set
print(collection)
#collection.remove(3) #this will give us an error because there is no value 3 in the set, #key error since the element here is key as well as value
collection.add("apna college") #adding a string to the set
collection.add((1,2,3)) #tuples can be added to sets because they are immutable #here, elements are stored in any order.
#collection.add([1,2,3]) #this will give us an error because lists are mutable and cannot be added to sets

print(collection)
collection.clear() #this will remove all the elements from the set
print(collection)
