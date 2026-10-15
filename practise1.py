collection={"hello","apna college","world","coding","python"}
print(collection.pop()) #removes and returns a random element from the set
print(collection.pop()) #removes and returns a random element from the set

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2)) #returns a new set that contains all the elements from both sets

print(set1) #no changes in original set1
print(set2) #no changes in original set2

print(set1.intersection(set2)) #returns a new set that contains only the elements that are present in both sets

print(set1) #no changes in original set1
print(set2) #no changes in original set2

#WAP to store following words in a python dictionary

dict={"table":["a piece of furniture","list of facts & figures"], "cat":"a small domestic animal"} #here, we have multiple values we can add them in a list or a tuple
print(dict)

subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(set(subject))
print(len(subject))