mylist = [1,2,3,4]
my_list = [1, "Hello", 3.14, True, [5, 6, 7], {'key': 'value'}, None]
print(my_list)
mytuple = (1,2,3,4)

#mytuple[0] = 10
mylist[0] = 10

print(mylist)

mylist.append(13)

print(mylist)
print(mylist.count(10))
print(len(mylist))
mylist.insert(2,123)
print(mylist)

print(f'index {my_list.index(3.14)}')
my_list.pop(2)
my_list.remove('Hello')
print(my_list)

newlist = [var * 2 for var in mylist]
print(newlist)