str1="this is a string"
str2='Apna College'
str3="""this is a string"""

"this is apna college's tutorial"

str1="this is a string.\nwe are creating it in python"
str2="this is a string.\twe are creating it in python"
print(str1)
print(str2)

str1="apna"
str2="college"
final_str=str1+str2
print(final_str)

str1="apna"
len1=len(str1)
print(len1)

str2="college"
len2=len(str2)
print(len2)

final_str=str1+" "+str2  #4+1(space)+7=12
print(final_str)
print(len(final_str))

#indexing

str="apna college"
ch=str[0]
print(ch)
print(str[4])

str1="apna college"
#str[3]=3 #strings are immutable, we cannot change the value of a string once it is created, so this will give an error

#slicing


str="apna college"
print(str[1:4]) 
print(str[5:]) #5 to end
print(str[:4]) #0:4

#negative indexing

str="apple"
print(str[-3:-1]) #pl

str="I am learning python"
print(str.endswith("hon")) #True

str="i am learning python"
print(str.capitalize()) #I am learning python #old string is not changed in this case, it will return a new string with the first character capitalized

str="i am learning python"
str=str.capitalize() #str is now updated with the new string
print(str.capitalize())

str="i am studying python from apna college"
print(str.replace("apna college", "apna university")) #i am studying python from apna university
print(str.replace("o", "a")) #i am studying pythan fram apna callege

str="i am studying python from apna college"
print(str.find("o")) # finds the first occurrence of "o" and returns its index, which is 18
print(str.find("z")) # finds the first occurrence of "z" and returns -1 since it is not found in the string
print(str.find("from")) # finds the first occurrence of "from" and returns its index, which is 21

str="i am from studying python from apna college"
print(str.count("from")) # counts the number of occurrences of "from" in the string, which is 2
print(str.count("o"))

#str.

a=input("enter a string: ")
print(len(a)) # Convert the input to a string first, then get its length

Str="Petrol expenseabcd is 70$ and Diesls expense is 50$"
print(Str.count("$")) # counts the number of occurrences of "$" in the string, which is 2

#Conditional statements

age=21
if (age>=18):
    print("can vote")
    print("can drive")

light="green"
if(light=="red"):
    print("stop")
elif(light=="green"): #elif is checked only when first statement is false
    print("go")
elif(light=="yellow"):
    print("look")

num=5
if(num>2):
    print("greater than 2")
if(num>3):
    print("greater than 3") #true statement is checked irrespective of whether first statement is true or false.

light="pink"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("broken")

age=25
if(age>=18):
    print("can vote") #indentation
else:
    print("cannot vote")

marks=int(input("marks of a student: "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")

#nesting

age=95
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

#Practise questions
#WAP to check whether a number entered by user is even or odd

a=int(input("enter a number: "))
if(a%2==0):
    print("even")
else:
    print("odd")

#WAP to check which number is greatest among three numbers entered by user

a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))
if(a>=b and a>=c):
    print("a is greatest")
elif(b>=a and b>=c):
    print("b is greatest")
else:
    print("c is greatest")

#WAP to check whether a number is divisible by 7 or not

a=13
if(a%7==0):
    print("divisible by 7")
else:
    print("not divisible by 7")

#WAP to check which number is greatest among four numbers entered by user

a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))
d=int(input("enter 4th number: "))
if(a>=b and a>=c and a>=d):
    print("a is greatest")
elif(b>=a and b>=c and b>=d):
    print("b is greatest")
elif(c>=a and c>=b and c>=d):
    print("c is greatest")
else:
    print("d is greatest")

marks1=94.9
marks2=78.2
marks3=89.3
marks4=65.9
marks5=45.6

marks=[94.9, 78.2, 89.3, 65.9, 45.6]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])

student=["Karan", 21, 94.9, "Delhi"]
print(student) #valid in python

str="hello"
print(str[0])
#str[0]="y" #strings are immutable, we cannot change the value of a string once it is created, so this will give an error

