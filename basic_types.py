#Immutable Types
intvar = 3
floatvar = 3.3
boolVar = True
str = "Hello world"
tuplesVar = ("1", '2', '3') 

# Mutable Types

listVar = ['1','2','3']
dictVar = {'key1':"value1"}
#objVar = SomeClass()


print(">>>>>>>>>>List type and place in memory Mutable type <<<<<<<")
print(type(listVar))
print(hex(id(listVar)))
listvar2 = listVar
print(hex(id(listvar2)))
listVar.append('123')
print(hex(id(listvar2)))
print(hex(id(listVar)))
print(listvar2)
print(listVar)
listvar2 = list(listVar)
print(hex(id(listvar2)))

print(">>>>>>>>>>Int type and place in memory immutable type <<<<<<<")
print(type(intvar))
print(hex(id(intvar)))
intvar2 = intvar
print(hex(id(intvar2)))
intvar += 2
print(hex(id(intvar)))
intvar2 += 3
print(hex(id(intvar2)))