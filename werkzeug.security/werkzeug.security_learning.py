# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:08:55 2020

@author: user
"""
## 加密與驗證實作 
## 首先導入我們需要的Packages
from werkzeug.security import generate_password_hash, check_password_hash

## 建立一個帳號機制
class Account:
    
    ## 帳號設置
    def __init__(self, name):
        self.name = name
    
    ## 密碼設置，但記得不能讓別人能夠閱讀
    @property
    def password(password):
        assert False, "You can not read password"
        
    ## 給予密碼
    @password.setter
    def password(self, password):
        ## 產生一組加鹽雜湊加密的產出值
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha1', salt_length = 10)
    
    ## 驗證機制
    def verify_password(self, password):
       return ('Login Succuess' if check_password_hash(self.password_hash, password) == True else 'Sorry Login failed' )
   
## 先創個帳號
little_turtle = Account('little_turtle')
## 確定一下帳號名稱
print(little_turtle.name) #ittle_turtle
## 設置密碼
little_turtle.password = 'Big1234'
## 查看密碼: 注意我們不能讓別人查看密碼
# print(little_turtle.password) #AssertionError: You can not read password
## 驗證密碼 
print(little_turtle.verify_password('Small1256')) # Sorry Login failed 登入失敗啦
print(little_turtle.verify_password('Big1234')) # Login Succuess 登入成功