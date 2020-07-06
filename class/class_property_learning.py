# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:06:51 2020

@author: user
"""

## property 基本用法 (有無property的區別)
class House:
    
    def __init__(self, address, name, phone_number):
        self.address = address
        self.name = name
        self.phone_number = phone_number
    
    @property
    def full_information(self):
        print("這是過去我們用print的方法:   address:%s, name:%s, phone_number:%s" %(self.address, self.name, self.phone_number))
        return "new method:  address:%s, name:%s, phone_number:%s" %(self.address, self.name, self.phone_number)
little_turtle_home = House('any Town any Street', 'Turtle', '09xx')
print(little_turtle_home.full_information)
## 如果不加 @property print 會得到 <bound method House.full_information of <__main__.House object at 0x000001A8B051E988>>
## 如果加上@property print 會得到 
## 這是過去我們用print的方法:   address:any Town any Street, name:Turtle, phone_number:09xx
##new method:  address:any Town any Street, name:Turtle, phone_number:09xx

little_turtle_home.full_information = "address:any county, name:Fish, phone_number:06xx"
## AttributeError: can't set attribute

class House:
    
    def __init__(self, name):
        self.name = name
    
    @property
    def full_name(self):
        return self.name
    
    @full_name.setter
    def full_name(self, value):
        self.name = value
    
    @full_name.deleter
    def full_name(self):
        del self.name
        print('have a nice day')
    
    
little_turtle_home = House('Turtle')
print(little_turtle_home.full_name)
## Turtle
little_turtle_home.full_name = 'Fish'
print(little_turtle_home.full_name)
## Fish
del little_turtle_home.full_name
## have a nice day
little_turtle_home.full_name = 'Star'
print(little_turtle_home.full_name)
## Star