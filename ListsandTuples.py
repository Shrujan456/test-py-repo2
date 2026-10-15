#Lists

student=["Karan", 21, 94.9, "Delhi"]
print(student[0])
student[0]="Rahul" #lists are mutable, we can change the value of a list once it is created

student=["Karan", 21, 94.9, "Delhi"]
#print(student[5]) #this will give an error because index 5 is out of range, we have only 4 elements in the list

marks=[94, 78, 89, 65, 45]
print(marks[1:4])
print(marks[-3:-1])

list=[2,1,3]
list.append(4) #adds an element to the end of the list
print(list.append(4)) #this will give None because append() method does not return anything, it modifies the list in place
print(list)

list=[2,3,1]
print(list.sort()) #sorts the list in ascending order
print(list)

list=[2,1,3]
print(list.append(4))
print(list.sort(reverse=True))
print(list)

list=['banana', 'apple', 'cherry']
print(list.sort()) #sorts the list in alphabetical order
print(list)


list=['c','a','b']
list.reverse() #reverses the list
print(list)

list=[2,1,3]
list.insert(1,5) #inserts 5 at index 1
print(list)

list=[2,1,3,1]
list.remove(1) #removes the first occurrence of 1 #[2,3,1]
print(list)

list=[2,1,3,1]
list.pop(2) #removes the element at index 2 #[2,1,1]
print(list)

#Tuple

tup=(1,2,3)
print(tup)
print(type(tup))
print(tup[0])
#tup[0]=3 #tuples are immutable, so we cannot change the value of a tuple

tup=() #we can have empty tuple
print(tup)
print(type(tup))

tup=(1,) #single value tuple, we need to add a comma after the value to make it a tuple
print(tup)
print(type(tup))

tup=(1)
print(tup)
print(type(tup)) #this is not a tuple, this is an integer

tup=("hello",) #single value tuple, we need to add a comma after the value to make it a tuple
print(tup)
print(type(tup))

tup=(1,2,3,4,5)
print(tup[1:3]) #slicing of tuple, it will give us a new tuple with the values from index 1 to index 2, index 3 is not included
print(tup.index(2)) #gives the index of the value 2 in the tuple

tup=(2,1,2,3,4,5)
print(tup.count(2)) #gives the count of the value 2 in the tuple

#WAP to ask the user to enter names of their favourite movies and store them in a list. 

movies=[]
movie1=input("enter your favourite movie: ")
movie2=input("enter your second favourite movie: ")
movie3=input("enter your third favourite movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)

#WAP to check if a list contains a palindrome of elements or not.

list1=[1,2,3,2,1]

copy_list1=list1.copy()
copy_list1.reverse()

if list1==copy_list1:
    print("palindrome.")
else:
    print("Not palindrome.")

list2=[1,2,3]

copy_list2=list2.copy()
copy_list2.reverse()

if list2==copy_list2:
    print("palindrome.")
else:
    print("Not palindrome.")

list3=["m","a","a","m"]

copy_list3=list3.copy()
copy_list3.reverse()

if list3==copy_list3:
    print("palindrome.")
else:
    print("Not palindrome.")

#WAP to count number of 

tup=("C","D","A","A","B","B","A") 
print(tup.count("A"))

list=["C","D","A","A","B","B","A"]
list.sort() #this will sort the list in ascending order
print(list)

