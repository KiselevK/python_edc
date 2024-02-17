i = 0
while True:
    i+=1
    if i == 2:
        break
i = 0
while i == 10:
    i+=1


mylist = ['1', '2', '3']

for val in mylist:
    print(val)

for index, value in enumerate(mylist):
    print(f'i = {index}, v = {value}')

for i in range(10):
    print(i)

for i in "Text":
    print(i)