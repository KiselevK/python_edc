invar = input('Put your data: ')

match invar:
    case '1':
        print('1')
    case '2':
        print('2')
    case _:
        print('noVal')

tempVar = "this is simple test"


if 'simple test' in tempVar:
    print('simple test in tempVar')

if 'hard' in tempVar:
    print('Hard in tempVar') #would not display

if 'are' in tempVar:
    print("are in tempVar")
elif 'is' in tempVar:
    print('just slicing = ' + tempVar[8:]) # will display everething after character number 8
elif 'simple' in tempVar:
    print('this will not show do privius if works')
else:
    print('nothing match')

data1 = [True, True, False] 
data2 = [True, True, True]

if all(data1) == False:
    print(f"data1 contains {data1}, so all function retuns {all(data1)}")

if all(data2):
    print(f"data2 contains {data2}, so all function retuns {all(data2)}. Also if checks function for True or False. This is the reason why it pass")