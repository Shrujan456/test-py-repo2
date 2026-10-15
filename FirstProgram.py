## print("My name is Shrujan.", "My age is 31")
## print(23)
##print(25+33)

#name="Shrujan"
#age=31
#price=25.99
#print(name)
#print(age)
#print(price)

#age2=age

#print("my name is : ", name)
#print("my age is : ", age)
#print("the price is : ", price)

#print(age2)

#print(type(name))
#print(type(age))
#print(type(price))

#name1='sk'
#name2="sk"
#name3='''sk'''

#print(name1)
#print(name2)
#print(name3)

old=False
c=None
print(type(old))
print(type(c))

#a=2
#b=3
#sum=a+b
#diff=a-b
#print(sum)
#print(diff)

a,b=2,3
txt="str"
print(a*txt*b)
print(a/b) #float division, quotient in float=0.6666
print(a%b) #modulus, reminder=2
print(a//b) #floor division, quotient in integer=0.6666
print(a**b) #exponentiation

A,B=5,-2
txt="str"
print(A*txt*B)
print(A/B) #float division, quotient in float=0.6666
print(A%B) #modulus, reminder=2
print(A//B) #floor division, quotient in integer=0.6666

#Taking input from user and printing it

#name=input("name : ")
#age=input("age : ")
#price=input("price : ")

#print("My name is", name, "and I am", age, "years old")

#Conditional statements

age=int(input("age : "))

if (age>=18):
    print("can vote")
else:
    print("cannot vote")

light=input("color : ")
if (light=="red"):
    print("stop")
elif (light=="yellow"):
        print("look")
elif (light=="green"):
        print("go")
else:
        print("broken")

marks=int(input("marks : "))

if (marks>=90):
    print("A")
elif (marks>=80 and marks<90):
    print("B")
elif (marks>=70 and marks<80):
    print("C")
else:
    print("D")


#Single line if/Ternary operator

food=input("food : ")
eat="Yes" if (food=="Cake") else "No"
print(eat)

food=input("food : ")
print("sweet") if food=="Cake" or food=="jalebi" else print("not sweet")

#Clever if/Ternary operator

age=int(input("age : "))
vote=("yes","no") [age>=18]
print(vote)

sal=float(input("salary : "))
tax=sal*(0.1,0.2) [sal<=50000]
print(tax)

#Best practises

p=float(input("p : "))
r=float(input("r : "))
t=float(input("t : "))
si=(p*r*r*t/100)
print(si)

#multi line comments

#Hi, I'm a comment
""" 
multi-line
comment
"""

# print("this is a comment") # selected all three lines and pressed ctrl+/
# print("this is a comment")
# print("this is a comment")

#arithmetic operators
a=2
b=3
print(a+b) 
print(a-b)
print(a*b)
print(a/b) #floating value
print(a%b) #remainder
print(a**b) #a^b

#relational operators
a=50
b=20
print(a==b) #False
print(a!=b) #True
print(a>b) #True
print(a>=b) #True
print(a<b) #False
print(a<=b) #False

#assignment operators
num=10
num=num+10 #10+10
print("num :",num) #20

num=10
num=num*10 #10*10
print("num :",num) #100

num=10
num=num/10 #10/10
print("num :",num) #1.0

num=10
num=num%10 #10%10
print("num :",num) #0

num=10
num=num**10 #10**10
print("num :",num) #100000

#logical operators
a=50
b=30
print(not False)
print(not (a>b)) #False

val1=True
val2=False
print("AND operator:", val1 and val2) #False
print("OR operator:", val1 or val2) #True
print("OR operator:", a==b or a>b) #True

#Type conversion
a=2
b=4.5
sum=a+b
print(sum) #a is an integer and b is a float, so the result is a float which is implicit type conversion, example of type conversion

a,b=1,"2"
c=int(b) 
sum=a+c #explicit type conversion which is exmample of type casting

#type casting examples

a=int("2")
b=4.25
print(type(a))
print(a+b)

a=float("2")
b=4.25
print(type(a))
print(a+b)

a=3.14
a=str(a)
print(type(a))

name=input("enter your name: ")
print("Welcome", name)

val=int(input("enter a number: ")) # type casting the input which is string into integer
print(type(val), val)

name=input("enter your name: ")
age=int(input("enter your age: "))
marks=float(input("enter your marks: "))

print("Welcome:", name)
print("Age:", age)
print("Marks:", marks)

#Practise1:- take two inputs from user and print their sum
a=int(input("enter a number: "))
b=int(input("enter another number: "))
c=a+b
print("sum :", c)

#Practise2:- take input from user and print area of square

a=float(input("enter the value of a side of a square: "))
area=a*a
print("area of square is:", area)

#Practise3:- take float inputs from user and take the average of two numbers

a=float(input("enter a number: "))
b=float(input("enter another number: "))
c=(a+b)/2
print("average is:", c)

#Pracise4:- take int inputs from user and print True if a>b else print False

a=int(input("enter a number: "))
b=int(input("enter another number: "))
print(True) if a>=b else print(False)