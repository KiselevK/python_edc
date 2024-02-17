# simple func
def my_func():
    print('this is simple func')
# func with args


def my_funk_with_args(somevalue):
    print(f'this is value: {somevalue}')


def my_func_with_return(yourvalue):
    return yourvalue

def my_funk_with_def_args(myval1 = 'myval1', myval2='myval2'):
    """This is doc string of this func"""#it will show some info for this func
    print(f'Defualt value for myval1 is myval1 but now it is {myval1}, for myval2 is myval2 but now it is {myval2}')
 

# call function
my_func()
my_funk_with_args("some data")
print(my_func_with_return('i want to print it'))
my_funk_with_def_args(myval2='newval')
