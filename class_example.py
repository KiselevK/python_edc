from abc import ABC, abstractmethod


class JustClass(ABC):  #abstract class a template that developer must follow 
   
    @abstractmethod
    def overwrite_example(self): 
        pass

class SimpleClass(JustClass):  # parent class
    class_var = 'class_var'  # class variable, shares between  all class instance

    def __init__(self, class_var2, user_name) -> None:
        self.user_name = user_name
        self.class_var2 = class_var2  # instance var, works with provided value
        print('This is init was created in SimpleClass, but called from' +
              self.__class__.__name__)

    def overwrite_example(self):  # instance method
        print('overwrite_example from Credit Card')

    # this is decorator change from instance(self) method to class method
    @classmethod
    def print_some_data(cls, data):  # cls hold class obj not instance
        return len(data)

    # this is decorator change from instance(self) method to class method
    @classmethod
    def set_a(cls, a):  # cls hold class obj not instance
        cls.a = a

    @property
    def the_class_user_name(self):
        user_name = self.user_name.upper()
        return user_name

    @staticmethod
    def convert_something_x2(number):
        return number*2

    def __eq__(self, __value: object) : #this is overwrite defualt method 
        pass

class ChildClass(SimpleClass):  # inheritance childclass(parent)
    def overwrite_example(self):
        print('overwrite_example was overwrited from childClass')


print('------------')
# simple_class_obj1 is a var instance that refers to object of the SimpleClass
simple_class_obj1 = SimpleClass('123', 'kyrylo')
simple_class_obj2 = SimpleClass('321', 'Kyrylo')
child_class_obj = ChildClass('100', 'Kyrylo')

print('------------')
print("Call simple_class_obj1 value is " + simple_class_obj1.class_var)
print("Call simple_class_obj2 value is " + simple_class_obj2.class_var)
print("Call simple_class_obj1 value is " + simple_class_obj1.class_var2)
print("Call simple_class_obj2 value is " + simple_class_obj2.class_var2)

print('------------')
simple_class_obj1.set_a(10)  # set a variable in classmethod
print(f"This is simple_class_obj1 a var {simple_class_obj1.a}")
print(f"This is  simple_class_obj2 a var {simple_class_obj2.a}")
print(f"This is  SimpleClass.a a var {SimpleClass.a}")

print('------------')
print(simple_class_obj1.print_some_data(
    'print some data from simple_class_obj1'))
print(simple_class_obj2.print_some_data(
    'print some data from simple_class_obj2 and this all'))
print(SimpleClass.print_some_data('simple class'))  # call a property


print('------------')
simple_class_obj1.overwrite_example()
child_class_obj.overwrite_example()

print('---------------')
print("propery "+simple_class_obj1.the_class_user_name)

print(f'Static {SimpleClass.convert_something_x2(5)}') 