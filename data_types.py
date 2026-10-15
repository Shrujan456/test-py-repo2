# #String Data type
# #literal assignment #1

import math


first="Dave"
last="Grey"
# print(type(first))
# print(type(first)==str)
# print(isinstance(first,str))

#constructor function #2
# pizza=str("Pepperoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))

#Concatenation #3
full_name=first+" "+last
print(full_name)
full_name +="!"
print(full_name)

#Casting a number to a String #4
decade=str(1980)
print(type(decade))
print(decade)

statement="I like rock music from the " +decade+ "s."
print(statement)

#Multiple lines #5
multiline='''
Hey, how are you?

I was just checking in.
                                                All good? 

'''
print(multiline)

#Escaping special characters #6
sentence='I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#String methods #7
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline+="                                                            "
multiline="                              "+multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

#Build a menu #8
title="menu".upper()
print(title.center(20,"="))

print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheesecake".ljust(16,".") + "$3".rjust(4))

print("")

#string index #9
print(first[1]) #first='Dave
print(first[-1])
print(first[1:-1])
print(first[1:])

#Some methods return boolean data #10
print(first.startswith("D"))
print(first.endswith("y"))

#Boolean data type #11
myvalue=False
x=bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#Numeric data types #12

#integer type
price=100
best_price=int(80)
print(type(price))
print(isinstance(best_price,int))

#float type
gpa=3.28
y=float(1.14)
print(type(gpa))

#complex type
comp_value=5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#Built-in functions for numbers #13

print(abs(gpa))
print(abs(gpa*-1))

print(round(gpa))

print(round(gpa,1))

#import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number
zipcode="10001"
zip_value=int(zipcode)
print(type(zip_value))

#Error if you attempt to case incorrect data

# zip_value=int("New York") throws error like invalid literal for int() with base 10: 'New York'

if 1>2:print("Yes")
