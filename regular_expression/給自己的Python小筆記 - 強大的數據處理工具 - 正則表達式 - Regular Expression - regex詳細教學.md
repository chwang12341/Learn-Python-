# 給自己的Python小筆記 - 強大的數據處理工具 - 正則表達式 - Regular Expression - regex詳細教學 







  哈囉，今天想來講一個我在工作上，常常需要用到的工具，我常常需要在一整堆的系統資訊、System Trace等等資料中，萃取出我需要的資料，並自動整理成表格的形式，這時候強大的正則表達式（Regular Expression, regex）就幫了我一個很大的忙，所以今天就來一起好好的學習它吧





## 正則表達式是什麼？ 



+ 對於我而言，它是一個非常強大且實用的字串處理方法，它幫助我們從擁有大量字符的文本中，取得我們所需的資訊

+ 正則表達式（Regular Expression 、regex、regexp or Re）透過我們自行定義的字符串規則，幫助我們從文本中找尋對應規則的字符串 

+ 過濾出我們所需的資料後，幫助我們將這些資料組成串列，方便我們對文本進行下一步的分析 

+ 舉個例子：我們要在文章中的眾多文字資料中，找尋文章提到的人物的身份證資料，我們就會去定義一個規則，第一個字符要是大寫的英文，後面要接續著九個數字，接著它就會根據這個規則找尋匹配的字符串，收集好後，回傳給我們





## Python 與 正則表達式？ 



正則表達式是一種輕量型的程式語言，它並不是Python底下的一個套件而已，像是我也用過Javascript來使用正則表達式處理文本字符串資料，在Python中，我們只要引入re模組就能使用這個強大的字符串處理語言囉



+ **基本的匹配**

![image1](images\image1.png)



+ **補充：常見的[...]匹配規則**



![image2](images\image2.png)





+ **定義好的字符集** 



![image3](images\image3.png)





+ **邊界上的匹配** 



![image4](images\image4.png)







+ **數量上的匹配（通常用在其它匹配符之後） **



![image5](images\image5.png)







**補充 group()：簡單來說，就是幫助我們方便看出匹配出來的字符有哪些** 



+ **邏輯與分組的概念** 



![image6](images\image6.png)





+ **特殊用法（不是用於分組）** 





![image7](images\image7.png)







+ **轉義字符** 



![image8](images\image8.png)





+ **特殊情況：當需要匹配一些在正則表達式中有特殊意義的字符時，像是\d、\w、\s等，此時就要多加一個"\"**







![image9](images\image9.png)





+ **正則表達式的修飾符號** 

  

  大部分的正則表達式函數中，都會有一個參數flags，它是用來控制匹配的模式的，裡面有如下表的標誌可以供選擇，如果想一次指定多個標誌，可以使用OR("|")，像是re.I | re.S等組合





![image10](images\image10.png)













## 正則表達式的貪婪與非貪婪模式 



通常在過程中匹配的字符數量，會有兩種情況：貪婪與非貪婪，而Python中的預設模式為貪婪模式 



+ 貪婪：，不斷嘗試匹配更多的字符 

  

+ 非貪婪：盡可能的嘗試少匹配字符，它會盡量減少匹配重複的字符 



+ 程式碼舉例：

```Python
import re

## 貪婪模式
print(re.search('go*', 'goooooood').group()) ## 'gooooooo'

## 非貪婪模式
print(re.search('go*?', 'goooooood').group()) ## 'g'
```

**執行結果**

```
gooooooo
g
```



#### 怎麼使用非貪婪模式呢？ 



我自己的實作心得是在語法後面加上一個"?"，如下圖的非貪婪模式介紹  



![image11](images\image11.png)





#### 非貪婪模式的常見用法  .*？的用法介紹 



+ .*？ ：盡量匹配較少的字符
+ 大多用在像是`.*？a`的地方，意思是前面匹配任何的字符，直到字母a出現

```Python
re.search('.*?e','a_b*c defg').group()
```





## 正則表達式的函數介紹與實作 



#### 1. match 函數用法 



+ re.match會從文本中的起始位置開始進行文字符的匹配，如果不是一開始第一個字符就匹配成功的話，就會直接返回一個none，簡單來說就是欲匹配的文本一開始就要符合我們定義的字符規則，不符合直接回傳none，符合就會回傳字符位置資訊 



+ 函數語法格式 

```Python
re.match(pattern, string, flags)
```



+ 參數介紹 

| 參數    | pattern                                                      |
| ------- | ------------------------------------------------------------ |
| pattern | 匹配的規則，使用正則表達式的語法撰寫                         |
| string  | 要進行匹配的字符串                                           |
| flags   | 設定一些正則表達式的匹配方式，像是規則是忽略大小寫，或使用UNICODE字符規則來解析字符等，如果沒有特別需求，可以忽略不寫 可以選擇的標誌，可以參考我上面有提到的正則表達式修飾符號 |

+ pattern: 匹配的規則，使用正則表達式的語法撰寫
+ string: 要進行匹配的字符串
+ flags: 設定一些正則表達式的匹配方式，像是規則是忽略大小寫，或使用UNICODE字符規則來解析字符等，如果沒有特別需求，可以忽略不寫 可以選擇的標誌，可以參考我上面有提到的正則表達式修飾符號







+ 使用group()函數來獲取匹配的字符，而不是返回一個字符的位置 

| 獲取匹配字符的方法 | 描述                                        |
| ------------------ | ------------------------------------------- |
| groups()           | 將匹配好的字符組合起來，形成一個tuple元數組 |
| group(num=0)       | 選擇第幾個匹配好的字符                      |

+ groups(): 將匹配好的字符組合起來，形成一個tuple元數組
+ group(num=0):   選擇第幾個匹配好的字符



+ **程式碼舉例1** 

```Python
import re

text = 'https://matters.news/@CHWang'
text1 = 'Matters.news'


print(re.match('https', text))
print(re.match('https', text).span())
print(re.match('matters', text))
print(re.match('matters', text1))
print(re.match('matters', text1, flags = re.I))
```

**執行結果**

```
<re.Match object; span=(0, 5), match='https'>
(0, 5)
None
None
<re.Match object; span=(0, 7), match='Matters'>
```



+ **程式碼舉例2：關於group的用法**



```Python
import re


text = 'Jack lives in HsinChu and he is 25 years old, but ...'

match_result = re.match(r'(.*) lives in ([a-z]*) and he is (\d+).*', text, re.I)
                        
                        
print(match_result.group())
print(match_result.group(1))
print(match_result.group(2))
print(match_result.group(3))

print(type(match_result.groups()))
print(match_result.groups())
```

**執行結果**

```
Jack lives in HsinChu and he is 25 years old, but ...
Jack
HsinChu
25
<class 'tuple'>
('Jack', 'HsinChu', '25')
```



#### 2. Search 函數用法 



+ re.search會搜尋整個字符串，然後找到匹配的字符並且傳回，如果失敗，沒有匹配到任何字符則傳回none，如果成功，就會傳回一個匹配的對象，就可以使用group()來取得匹配成功的字符 



+ 函數語法格式 

```
re.search(pattern, string, flags) 
```



+ 參數的用法與match是一樣的喔，這邊就不在說明 



+ 程式碼範例1 

```Python
import re

text = 'https://medium.com/@chwang12341'
text1 = 'Medium.Com'

print(re.search('https://', text))
print(re.search('dium', text))
print(re.search('medium', text).span())

print(re.search('co',text1))
print(re.search('co',text1, flags = re.I).span())
```

**執行結果**

```
<re.Match object; span=(0, 8), match='https://'>
<re.Match object; span=(10, 14), match='dium'>
(8, 14)
None
(7, 9)
```



+ 程式碼範例2：使用groups()與group(num)來取得字符

```Python
import re

text = 'Jen likes to eat cake and drink coke, but ...'

match_result = re.search('(.*) likes to eat (\w+) and drink ([a-z]*)', text, re.I|re.M)

print(match_result.group())
print(match_result.group(1))
print(match_result.group(2))
print(match_result.group(3))

print(match_result.groups())
```

**執行結果**

```
Jen likes to eat cake and drink coke
Jen
cake
coke
('Jen', 'cake', 'coke')
```



+ **小筆記：大家有看出match與search的差別嗎？其實差別就在match一定要從起始位置開始匹配成功，而search則不用的喔！！**







#### 3. findall 函數用法 



+ re.findall會直接找尋所有匹配的字符，裝進串列後返回，如果沒有找到匹配的字符，就會回傳一個空的串列喔

  

+ 小筆記：re.findall會匹配所有符合規則的字符，而re.search與re.match只會匹配一次而已喔

  

+ 函數格式

```
 findall(pattern, string, pos, endpos)
```



+ 參數說明 

  + pattern: 匹配的規則，使用正則表達式的語法來撰寫

  + string:欲進行匹配的字符串 

  + pos: 可選擇的參數，不一定要寫，指定開始匹配的位置，預設為0，也就是起始字符的位置

  + endpos: 可以選擇的參數，不一定要添加，指定結束匹配字符串的位置

  

+ 程式碼舉例：

```Python
import re

find_pattern = re.compile(r'[a-z]+', re.I)

match_result1 = find_pattern.findall('good 66 day Tom_28 Yep')
match_result2 = find_pattern.findall('good98MMorning66 Jen666 Yeah', 6,20)

print(match_result1)
print(match_result2)
```

**執行結果**

```
['good', 'day', 'Tom', 'Yep']
['MMorning', 'Jen']
```





#### 4. sub 函數用法 



+ 匹配好字符後，將它替換成我們想要的字符，這個方法相當方便，我們在進行數據處理時，有時候會有一些多餘的不要的空格、符號等等，就可以透過這個方法來一次拿掉



+ 函數語法格式 re.sub(pattern, repl, string, count = 0, flags) 

  

+ 參數解釋 

  

  + pattern: 匹配的規則，使用正則表達式的語法來撰寫
  + repl: 欲替換的字符，也可以用函數的形式傳入喔

  + string: 要進行匹配的字符串
  + count: 匹配好字符後，替換的最大數量，預設為0，表示要全部替換
  + flags: 設定一些正則表達式的方式，像是規則是否忽略大小寫、使用UNICODE字符規則來解析字符等，如果沒有特別需求可以忽略不寫 可以選擇的標誌，可以參考我上面有提到的正則表達式修飾符號喔 





+ 程式碼舉例1: 

```Python
import re 

text = 'Jack/25/1993 and Jen/23/1995'

## 把中間的and與空格拿掉，用&替換
sub_result1 = re.sub('\sand\s', '&', text)
print(sub_result1)

## 狀況一: 再把/拿掉
sub_result2 = re.sub('/', '', sub_result1)
print(sub_result2)

## 狀況二: 再把/拿掉，但只要拿掉前兩個
sub_result3 = re.sub('/', '', sub_result1, 2)
print(sub_result3)
```

**執行結果**

```
Jack/25/1993&Jen/23/1995
Jack251993&Jen231995
Jack251993&Jen/23/1995
```



+ 程式碼舉例2：repl使用函數傳入時

```Python
import re

text = 'Jack66Jen58Ken28,Cathy38'

## 將匹配好的數字做平方計算
def square(match_result):
    num = int(match_result.group('number'))
    
    return str(num**2)

## 給定我們匹配值一個名稱，用?P<name>
final_result = re.sub('(?P<number>\d+)', square, text)

print(final_result)
```

**執行結果**

```
Jack4356Jen3364Ken784,Cathy1444
```





#### 5. Compile 函數



+ re.compile可以幫助我們編譯正則表達式，並生成一個pattern對象，來供給match、search、findall函數使用，簡單來說，就是我們只要定義好一次正則表達式的規則，就能用這個定義好的pattern規則，來提供match、search、findall函數匹配字符 



+ 用了這個方法後，我們就不用每次使用匹配函數時，都要重新寫一次正則表達式語法，但明明匹配的規則與寫法是一樣的

  

+ 函數語法格式： 

```
re.compile(pattern, flags)
```



+ 參數介紹
  +  pattern: 匹配的規則，使用正則表達式的語法來撰寫
  +  flags: 設定正則表達式匹配的一些模式



+ 程式碼舉例：

```Python
import re

text = '68Jack66Jen58Ken28,Cathy38'

## 匹配字母，並忽略大小寫
pattern = re.compile(r'([a-z]+)', re.I)

## match預設從第一個位置開始匹配
compile_result1 = pattern.match(text)
print(compile_result1) ## None，因為match會從第一個位置開始匹配，如果不通過就會返回none

## 從第3個位置開始匹配
compile_result2 = pattern.match(text, 2, 20)
print(compile_result2) 


print(compile_result2.group(0)) 
print(compile_result2.start(0))
print(compile_result2.end(0))
print(compile_result2.span()) 
```

**執行結果**

```
None
<re.Match object; span=(2, 6), match='Jack'>
Jack
2
6
(2, 6)
```



+ **補充用法說明** 

  + group(): 匹配好後，會回傳一個tuple，會根據匹配成功的字符一組一組返回，但由於match方法只會回傳一組，所以只要寫group()就好，其他的話，諾我們想要回傳第一組就寫group(0)，以此類推
  + start(): 起始位置，傳入要查詢的組別，像是第一組就寫start(0)，以此類推
  + end(): 結束位置，傳入要查詢的組別，像是第一組就寫end(0)，以此類推

  + span(): 傳回（起始位置,結束位置）





#### 6. finditer 函數用法 



+ re.finditer的用法與re.findall相似，找到所有符合匹配規則的字符後，以迭代器的形式傳回

  

+ 函數語法格式：

```
 re.finditer(pattern, string, flags) 
```



+ 程式碼舉例：

```Python
import re

match_result = re.finditer(r'[a-z]+', '68Jack66Jen58Ken28,Cathy38', re.I)


for name in match_result:
#     print(name)
    print(name.group())
```

**執行結果**

```
Jack
Jen
Ken
Cathy
```





#### 7. split 函數用法 



+ re.split將匹配的字符進行切割，並且回傳一組串列

  

+ 函數語法格式： 

```
re.split(pattern, string, maxsplit, flags)
```





+ 參數介紹
  + pattern: 匹配的規則，使用正則表達式的語法撰寫
  + string: 欲進行匹配的字符串
  +  maxsplit: 分割的次數，如maxsplit=1，代表分割一次，預設為0，表示不限分割次數
  + flags: 設定一些匹配的模式 



+ 程式碼舉例：

```Python
#### import re

text = 'Jack66Jen58Ken28Cathy'

## 用數字來做為分隔依據
print(re.split('\d+', text))

## 分隔，並將數字也傳進陣列
print(re.split('(\d+)', text))

## 如果匹配的一句剛好在前後的位置，就會傳回空值
text1 = '66Jack66Jen58Ken28Cathy38'
print(re.split('\d+', text1))

## 如果找不到匹配會回串全部字串
print(re.split('\s+', text1))
```

**執行結果**

```
['Jack', 'Jen', 'Ken', 'Cathy']
['Jack', '66', 'Jen', '58', 'Ken', '28', 'Cathy']
['', 'Jack', 'Jen', 'Ken', 'Cathy', '']
['66Jack66Jen58Ken28Cathy38']
```





## 重要筆記：匹配時將我們需要爬取的數據，用（）來包住它的匹配規則，才會被獨立出來放入串列 



舉個例子來說，我們想要爬取文本字符串中符合我們指定格式的字符串，但是我們只想要取得|Example_format|前後的數值，並分別放入串列，這時候我們就需要將它們括號起來，像是(\d+)|Example_format|(\d+)這樣  



#### 指定的字符串格式：6658|Example_format|666



程式碼舉例:

```Python
import re

text = '6658|Example_format|2020'

print(re.findall(r'(\d+)(?:\WExample_format\W)(\d+)', text))
```

**執行結果**

```
[('6658', '2020')]
```





**這樣的話，之後大家就可以在有很大量字符串的數據文本中，爬取符合我們需求格式的資料，而且我們不只要爬取符合這個格式的資料，還要只收集我們在這個格式中需要的數據值**



**太好了，會了強大的正則表達式（Regular Expression）後，我們就能在茫茫文字海中爬取各種我們所需的資料囉，真的超級實用！！感謝大家的閱讀，如果覺得我寫得還行XD，在幫我拍拍手鼓勵一下，或有問題也可以在底下留言跟我討論討論喔～～**







## Reference

[https://www.itread01.com/content/1552631899.html](https://www.itread01.com/content/1552631899.html?fbclid=IwAR3A_iZfIng-WL7QvoHJv8gHTza5Ni1aDQIythmOBXKD47k6-G7-ODlev1c)

[https://www.runoob.com/python/python-reg-expression.html#flags](https://www.runoob.com/python/python-reg-expression.html?fbclid=IwAR2P398Nv4Qc6KJV2MS8hyoxTQWhU0T5fQJD0jJZ0Ke2ZenCE6mUgqbzlkU#flags)

[https://kknews.cc/zh-tw/code/mjnv352.html](https://kknews.cc/zh-tw/code/mjnv352.html?fbclid=IwAR0KX7xUqSrV9mhnSwdAGjYCwpl5Vb8IGE5qmaokzYFCYoTf3D7zS5uXj3A)

[https://docs.python.org/zh-tw/3/howto/regex.html](https://docs.python.org/zh-tw/3/howto/regex.html?fbclid=IwAR2P398Nv4Qc6KJV2MS8hyoxTQWhU0T5fQJD0jJZ0Ke2ZenCE6mUgqbzlkU)

