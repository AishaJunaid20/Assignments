# Python DataType 
#integer
number:int=255
print(number)
print(type(number))

#String
name:str="Aisha"
print(name)
print(type(name))

#Float
percentage:float=85.25
print(percentage)
print(type(percentage))

#Boolean
text_Boolean:bool=True
print(text_Boolean)
print(type(text_Boolean))

#list
Name_list:list=["apple","banana","cherry"]
print(Name_list)
print(type(Name_list))
print(Name_list[0])

#Dictionary
name:dict={"name":"Aisha","fathername":"junaid"}
print(name)
print(type(name))

#tuples
fruits:tuple=("apple","cherry","grapes")
print(fruits)
print(fruits[1])
print(type(fruits))

#Set
name:set={"ali","sana","sana"}
print(name)
print(type(name))

#None 
none_data:None=None
print(none_data)
print(type(none_data))


#Python Keywords
import keyword
print("Python Keyword",keyword.kwlist)

#Special Keyword
a=None 
if None is None :
    print("a is None")

#Deining a function using def keywords 
def GIAIC():
    print("Hello Student ")
    GIAIC()    