# 給自己的Python小筆記: Python進階用法- 想讓變數名稱跟著迴圈動態定義嗎- Locals與Globals 技巧教學



哈囉哈囉，今天想跟大家介紹一個我在工作中常用到的一個小技巧，由於職業的關係，我時常需要導入數據，並賦予不同的變數名稱來同時操作這些不同時間點錄下的資料，但如果想要同時對這種眾多檔案進行一樣的數據處理，總不能要我一個一個定義變數名稱給它們，然後再一個一個進行數據處理，這樣我就沒時間回家寫文章了XD，所以今天要來分享給大家這個，我覺得非常實用的技巧





## 問題1: 如果今天遇到一個需要我們定義很多連續變數的值時，我們該怎麼做呢?





#### 範例1: 一般的作法，我們會分別定義每個變數的值，然後再使用它們

```Python
number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5
number6 = 6
number7 = 7
number8 = 8
number9 = 9
number10 = 10


print(number1)
print(number2)
print(number3)
print(number4)
print(number5)
print(number6)
print(number7)
print(number8)
print(number9)
print(number10)
```

![image1](images\image1.PNG)



**小提醒: 這樣的作法，確實也可以達到我們要的目的，但是如果今天變數一變多，我們有1000個以上的時候，總不能這樣慢慢定義每個變數，會寫到天荒地老，哈哈，所以接下來我們就來看看今天的主角: locals()與globals()如何幫助我們快速實現目的**



#### 範例2: locals與globals簡單變換變數名稱的運用

+ locals()

  

```Python
for i in range(1,10):
    locals()['number'+str(i)] = i
    print('Print In Once: ', locals()['number'+str(i)])
```





+ globals()

  

```Python
for i in range(1,10):
    globals()['number'+str(i)] = i
    print('Print In Once: ', globals()['number'+str(i)])
    
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)
print(number6)
print(number7)
print(number8)
print(number9)
```

![image2](images\image2.PNG)





## 問題2: 如果今天在函式中定義好的變數，要怎麼在另一個函式中此用這些變數呢?



**從上面的結果看起來，不論是locals()還是globals()，都能達到一樣的效果呀，那它們有什麼不同?**

+ locals(): 宣告為區域變數，它在使用上會遇到一個問題，在函式A中定義好的變數，不能在函式B中被使用

```Python
name_list = ['Jack', 'Eric', 'Cathy', 'Jenny', 'James', 'Gary', 'Lucy', 'Candy']

def locals_example():
    for i in range(len(name_list)):
        locals()['name'+str(i)] = name_list[i]
        print(locals()['name'+str(i)])

def greet_example():
    for n in range(len(name_list)):
        print('locals(): Hello' + locals()['name'+str(i)])
        
    
if __name__ == '__main__':
    locals_example()
    greet_example()
```





![image3](images\image3.PNG)

**從最後結果發現，num0並不能在本身函式以外的地方使用，這也正是locals()宣告為區域變數的原因**



+ globals(): 宣告為全域變數，變數就能在任何其他函數中使用

```Python
name_list = ['Jack', 'Eric', 'Cathy', 'Jenny', 'James', 'Gary', 'Lucy', 'Candy']

def globals_example():
    for n in range(len(name_list)):
        globals()['name'+str(n)] = name_list[n]
        print(globals()['name'+str(n)])

def greet_example():
    for n in range(len(name_list)):
        print('globals(): Hello' + globals()['name'+str(n)])
        
    
if __name__ == '__main__':
    globals_example()
    greet_example()
    print(name2)
```



![image4](images\image4.PNG)



從最後結果可以看出，由於name2是被globals()宣告為全域變數的，所以最後可以成功印出



## 既然globals()這麼好用，那全部都用globals就好啦，為什麼還要使用locals呢?

未來當撰寫的程式碼越來越多的時候，可能會出現重複定義同一個變數名稱，就有覆寫的問題，所以要斟酌使用locals或是globals喔





**這篇雖然短短的，但我覺得這個技巧是可以幫助我們節省很長很長的時間，來進行數據處理，希望這次對大家也有大大的幫助~~**

**如果覺得我寫得還行，再幫我拍拍手喔，感謝您**





