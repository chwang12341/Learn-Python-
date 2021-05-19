# 給自己的Python小筆記 - 如何將字符串中的語句 轉換成可以執行的Python命令? - eval() 函數使 用教學



YoYo~~不知道大家有沒有遇到過要執行的Python語句包覆在字符串裡面，也就是這條語句是字符串類型，但是我們又需要去執行這裡面的Python程式，而不是只是執行一個字符串，這時候就會需要用到eval()這個魔法了XD





## 1. eval() 函數與參數介紹



+ 函數
```
eval(source, globals=None, locals=None, /)
```
+ 參數介紹

1. source: 傳人 Python表達式的字符串或是compile()傳回的程式碼物件

2. globals(): 為一個可選參數，是全局命名的空間，如果使用的話，就一定要是一個字典形式

3. locals(): 為一個可選參數，是局部命名的空間，如果使用的話(不為None)，可以是任何的映射(mapping)

**提醒:** 如果只有給定globals，則locals預設就為全局變量

**補充:** 如果不瞭解命名空間的朋友們，可以參考一下這篇:https://www.runoob.com/python3/python3-namespace-scope.html，我覺得寫得很詳細喔

**觀念: Python用globals()來記錄全局變數，而用locals()來記錄局部變數，而這些變數都是以字典的格式存在這兩個命名空間中**









## 2. 實作



### a. 數值運算
```Python
x = '(23+6-9)*8'
print(type(x))
print(x)
## eval
print('------------ eval() ---------------')

print(type(eval(x)))
print(eval(x))
```
**執行結果**

```
<class 'str'>
(23+6-9)*8
------------ eval() ---------------
<class 'int'>
160
```





### b. 變數使用
```Python
x = int(input('Give a number:'))
print('plus 2')
eval('x + 2')
```
**執行結果**

```
Give a number:6
plus 2
```

Out[7]:

```
8
```





### c. 字典轉換
```Python
x="{'Student': 'A',  'Score': 99}"
print(type(x))

print('--------------eval------------------')
print(type(eval(x)))
print(eval(x))
```
**執行結果**

```
<class 'str'>
--------------eval------------------
<class 'dict'>
{'Student': 'A', 'Score': 99}
```





### d. globals locals

+ globals() 應用: 將score變量帶入


```Python
## 全局變量 globals 應用
print(eval('x + 2', {'x': 6}))
print(eval("{'Student': 'Ken', 'Score': score}", {'score': 99}))
```

**執行結果**

```
8
{'Student': 'Ken', 'Score': 99}
```




+ 當globals 和 locals 同時給的時候
```Python
## locals 和 globals 都給定字典
print(eval('x + 2',{'x': 6},{'x':8}))
print(eval("{'Student':'Ken','Score': score}", {'score': 99}, {'score': 60}))

## 使用locals()來獲取局部命名空間的字典，並同時取全局與局部的值，只要不同就能同時使用
name = "Allen"
print(eval("{'Student': name, 'score': score}", {'score': 99}, locals()))
```

**執行結果**

```
10
{'Student': 'Ken', 'Score': 60}
{'Student': 'Allen', 'score': 99}
```







**結果:會以locals的變數來決定**

**筆記: 同時取全局與局部的值,只要不同就能同時使用**







## 3. 安全性



**狀況:** 當程式中有input()這個的函式，讓使用者可以輸入語句到程式時

input()會將使用者輸入的語句轉換成字符串，而此時如果又用eval()轉換成Python程式語句時，可能就存在危險性，像是如下，使用者可以透過一些Python語句來獲取電腦的資訊





輸入:

1. `__import__('os').system('dir')` 獲取資料夾目錄

2. `__import__('os').system('id')` 獲取電腦使用者的ID與群組ID

```Python
t = input('输入格:')
eval(t)
```



**執行例子**

```
输入格:__import__('os').system('dir') 
```

Out[12]:

```
0
```

只要使用os這個模組就能輕鬆獲取電腦的一些資訊，所以使用上要特別注意這個問題



















