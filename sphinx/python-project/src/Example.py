# -*- coding: utf-8 -*-
## Example.py
"""
.. centered:: Learing Sphinx
.. codeauthor:: Shane <chwang12341@gmail.com>
"""
## 建立一個House
class House:
     
    """  House 這個class 有什麼
>>>  __init__(self, address, name, phone_number)
    初始化一個House
>>>  move_in(self, amount)
    遷入
    
    >>>  move_out(self, amount)
    遷出
>>>  __del__(self)
    毀掉
    
    
    這邊我們建立一個little turle 的家做示範
## 建立一個House(little_turtle_home) 並給予基本資料
    little_turtle_home = House('any Town any Street', 'Turtle', '09xx')
    little_turtle_home.move_in(2)
    little_turtle_home.move_in(4)
    little_turtle_home.move_in(2)
    little_turtle_home.move_out(2)
    ## print 出成員人數
    print(little_turtle_home.member)
    ## 毀掉房子
    del little_turtle_home
    # print(little_turtle_home)
    ##NameError: name 'little_turtle_home' is not defined
"""
    def __init__(self, address, name, phone_number):
        self.address = address
        self.name = name
        self.phone_number = phone_number
        self.member = 0
    
    ## 遷入的fucntion
    def move_in(self, amount):
        
        if amount < 0:
            raise ValueError("Amazing: people amount can't be negative")
        else:
            self.member += amount
    
    ## 遷出的function
    def move_out(self, amount):
        
        if amount > self.member:
            raise ValueError('exceed the amount of people here')
        else:
            self.member -= amount
    ## 破壞房子的方法
    def __del__(self):
        return "destroy the house"
## 建立一個House(little_turtle_home) 並給予基本資料
little_turtle_home = House('any Town any Street', 'Turtle', '09xx')
little_turtle_home.move_in(2)
little_turtle_home.move_in(4)
little_turtle_home.move_in(2)
little_turtle_home.move_out(2)
## print 出成員人數
print(little_turtle_home.member)
## 毀掉房子
del little_turtle_home
# print(little_turtle_home)
##NameError: name 'little_turtle_home' is not defined
def print_hello():
    """
    哈囉
    >>> print('hello')
    
    """
print('Hello')