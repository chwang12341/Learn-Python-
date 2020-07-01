# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 24 19:40:06 2020

# @author: user
# """
# ## Class Basic Design
# class House:
    
#     def __init__(self, address, name, phone_number):
#         self.address = address
#         self.name = name
#         self.phone_number = phone_number
#         self.member = 0
    
#     def move_in(self, amount):
        
#         if amount < 0:
#             raise ValueError("Amazing: people amount can't be negative")
#         else:
#             self.member += amount
            
#     def move_out(self, amount):
        
#         if amount > self.member:
#             raise ValueError('exceed the amount of people here')
#         else:
#             self.member -= amount
            
#     def __del__(self):
#         return "destroy the house"
# little_turtle_home = House('any Town any Street', 'Turtle', '09xx')
# little_turtle_home.move_in(2)
# little_turtle_home.move_in(4)
# little_turtle_home.move_in(2)
# little_turtle_home.move_out(2)
# print(little_turtle_home.member)
# del little_turtle_home
# # print(little_turtle_home)
# ##NameError: name 'little_turtle_home' is not defined






# ## __new__ 方法
# class X(object):
#     def __init__(self,*args,**kargs):
#         print ("init %s" %self.__class__)
#         self.total = 2
#     def __new__(cls,*args,**kargs):
#             print ("new %s" %cls)
#             cls.total = 4
#             return object.__new__(cls, *args, **kargs)
        
#         ## *num 讓我們傳入參數時，可以是tuple
#     def add(cls, *num):
#         for i in num:
#             print(i)
#             print(type(i))
#             cls.total += i
#         print(cls.total)
                
            
# x = X()
# ## 先執行new 再執行init(會幫__new__初始化) 再執行add
# x.add(1,4,8)
# # output
# # new <class '__main__.X'>
# # init <class '__main__.X'>
# # 1
# # <class 'int'>
# # 4
# # <class 'int'>
# # 8
# # <class 'int'>
# # 15




# ## __dict__ 用法 和 __str__用法
# ## https://blog.csdn.net/qq_26442553/article/details/82466382
# ## https://blog.csdn.net/xiaolewennofollow/article/details/51455185?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
# class House:
#     city = "HsinChu"  ## class attribute(__dict__ can't load)
#     def __init__(self, address, name, phone_number):
#         self.address = address
#         self.name = name
#         self.phone_number = phone_number
#         self.member = 0
    
#     def __str__(self):
#         return ("House name: %s, Address: %s, Phone Number: %s"%(self.name,self.address,self.phone_number))
# ## 實際操作
# little_turtle_home = House('any Town any Street', 'Turtle', '0999')
# print(little_turtle_home) ## print type(string) ## same as print(little_turtle_home.__str__()) 
# ## Output
# # House name: Turtle, Address: any Town any Street, Phone Number: 0999
# print(little_turtle_home.__dict__) ##change to dict format 
# ## Out put 
# # {'address': 'any Town any Street', 'name': 'Turtle', 'phone_number': '0999', 'member': 0}
# print(little_turtle_home.__dict__['address'])
# # any Town any Street




# ## __dict__ 應用


# ## create a dict
# class House:
    
#     def __init__(self, address, name, phone_number):
#         self.address = address
#         self.name = name
#         self.phone_number = phone_number

# little_turtle_home = House('any Town any Street', 'Turtle', '09xx')
# print(little_turtle_home.__dict__)
# ## Output
# #{'address': 'any Town any Street', 'name': 'Turtle', 'phone_number': '09xx'}

# ## if your input is dict format
# ## method1:
# class House1:
#     def __init__(self,dict_obj):
#         self.address = dict_obj['address']
#         self.name = dict_obj['name']
#         self.phone_number = dict_obj['phone_number']

# little_turtle_home1 = House1(little_turtle_home.__dict__)
# print(little_turtle_home1.name)
# ## Output
# #Turtle

# # method2: you can use self.__dict__.update() : help you easily parse the dict into variable format
# class House2:
#     def __init__(self,dict_obj):
#       self.__dict__.update(dict_obj)      
      
# little_turtle_home2 = House1(little_turtle_home.__dict__)
# print(little_turtle_home2.name)
# ## Output
# #Turtle



## __getattr__ 、 __setattr__ 用法
class example:
    
    def __init__(self,ax, bx):
        self.a = ax
        self.b = bx
    ## 轉成dict 
    def d(self):
        print(self.__dict__)
        
    def __getattr__(self,name):
        print("__getattr__")
    
    def __setattr__(self,name,value):
        print("__setattr__")
        self.__dict__[name] = value

## execute
E = example(2,8)
E.d()
print(E.x)
E.x = 6
E.d()
# Output
# __setattr__
# __setattr__
# {'a': 2, 'b': 8}
# __getattr__
# None
# __setattr__
# {'a': 2, 'b': 8, 'x': 6}
