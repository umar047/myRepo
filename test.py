'''
class Vehicle:
    def __init__(self, price, color):
        self.price = price
        self.color = color

    def show_details(self):
        print("the vehicle price is",self.price)
        print("the vehicle color is",self.color)

v1 = Vehicle(5000,'green')
v1.show_details()

class Car(Vehicle):
    def __init__(self, price, color,millage,hp):
        super().__init__(price, color)
        self.millage = millage
        self.hp = hp
    def show_car_details(self):
        print("i am a car")
        print("the millage of car is",self.millage)
        print("the hp of car is",self.hp)

c1 = Car(3000,'Black',1000,700)
c1.show_car_details()
c1.show_details()


class Parent1():
    def str_one(self,str1):
        self.str1 = str1
    def show_str1(self):
        print("the str1 is",self.str1)

class Parent2():
    def str_two(self,str2):
        self.str2 = str2
    def show_str2(self):
        print("the str2 is",self.str2)

class Derived(Parent1,Parent2):
    def str_three(self,str3):
        self.str3 = str3
    def show_str3(self):
        print("the str3 is",self.str3)

a1 = Derived()
a1.str_one("umar")
a1.str_two("iqbal")
a1.str_three("hamza")

a1.show_str1()
a1.show_str2()
a1.show_str3()
'''
class Parent():
    def student_name(self,name):
        self.name = name
    def show_name(self):
        print("the name of student is",self.name)
class child(Parent):
    def student_age(self,age):
        self.age = age
    def show_age(self):
        print("the age of student is",self.age)
class grandchild(child):
    def student_gender(self,gender):
        self.gender = gender
    def show_gender(self):
        print("the gender of student is",self.gender)
    
a1 = grandchild()

a1.student_name("umar iqbal")
a1.student_age(26)
a1.student_gender("male")

a1.show_name()
a1.show_age()
a1.show_gender()





    
        


  
