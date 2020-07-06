# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:23:50 2020

@author: user
"""

class House:
 tv_amount = 1 #類別屬性
 def __init__(self, human, name):
     self.human = human ##實體屬性
     self.name = name ##實體屬性
     House.add_tv(1) ## static
     House.add_tv1(2) ## class
 
 @staticmethod
 def add_tv(i):
     House.tv_amount += i
 
 @classmethod
 def add_tv1(cls,i):
     cls.tv_amount += i
little_turtle_home = House(1, "Turtle")
print(little_turtle_home.name) # Turtle
print(little_turtle_home.human) #1
print(little_turtle_home.tv_amount) #4
print(House.tv_amount)# 4
little_turtle_home1 = House(1, "Turtle")
print(little_turtle_home1.tv_amount) #7
print(House.tv_amount) #7


## import abstract package
import abc
class old_Turtle(abc.ABC):
 @abc.abstractmethod
 def swim(self):
     print('I can swim')
     return NotImplemented
 
class young_turtle(old_Turtle):
    def swim(self):
        print('I can swim fast')
 
    def eat(self):
        print('I can eat')
 
class little_turtle(old_Turtle):
    def eat(self):
        print('I can eat') 
 
 
 
print(young_turtle().swim()) # I can swim fast
print(young_turtle().eat()) # I can eat
print(little_turtle().eat()) # TypeError: Can't instantiate abstract class little_turtle with abstract methods swim


class House:
 
    def __init__(self, address, name, phone_number):
        self.__address = address
        self.__name = name
        self.phone_number = phone_number
        self.member = 0
little_turtle_home = House('any Town any Street', 'Turtle', '09xx')
print(little_turtle_home.phone_number) ## 沒封裝: 09xx
print(little_turtle_home.__address) ## 有封裝: AttributeError: 'House' object has no attribute 'address'

class House:
 
    def __init__(self, address, name, phone_number):
        self.__address = address
        self.__name = name
        self.phone_number = phone_number
        self.member = 0
 
    def get_attribute(self):
        return self.__address
little_turtle_home = House('any Town any Street', 'Turtle', '09xx')
print(little_turtle_home.phone_number) ## 沒封裝: 09xx
# print(little_turtle_home.address) ## 有封裝: AttributeError: 'House' object has no attribute 'address'
print(little_turtle_home.get_attribute()) ## 有封裝，但換個方法get起來 : any Town any Street

## 建立一個 Class
class House: 
 def __init__(self, address, name, phone_number):
   self.address = address
   self.name = name
   self.phone_number = phone_number
 ## 再建立一個class
 class material:
   def __init__(self, material):
     self.material = material
   def find(self):
     return "find out material!!"
## 先建立一個little_turtle_home
little_turtle_home = House('any Town any Street', 'Turtle', '09xx')
## 再建立一個在little_turtle_home底下的class 
new_little_turtle_home = little_turtle_home.material("brick")
## 使用這個class的function
print(new_little_turtle_home.find()) #find out material!!
## 查看House class 底下的資訊
print(little_turtle_home.address , little_turtle_home.name, little_turtle_home.phone_number, end=' ') # any Town any Street Turtle 09xx
## 在House底下建立個另一個class material ，沒辦法用它查看外層class House的資訊
# print(new_little_turtle_home.address , new_little_turtle_home.name, new_little_turtle_home.phone_number) # 'material' object has no attribute 'address'
## 使用這個class的屬性
print(new_little_turtle_home.material) # brick
## 查看原本建立的class little_turtle_home 底下的class material
print(little_turtle_home.material) # <class '__main__.House.material'>