# Coding起來 - Python pathlib模組 - 快來學習超好用的檔案與資料夾操作模組





## 1. 動機 - 為什麼要用pathlib?



過去我在執行有關路徑的操作，幾乎都是使用os.path，但是因為工作的關係常常會面臨一個問題，就是我的Python要在Windows跟Linux間進行操作，每次都因`\`問題要修改來改去，所以同事就推薦我一個相當好用的模组pathlib

**路徑 / 問題:**

+ Windows作業系統: 我們的路徑會用反斜線`\`

+ Mac/Linux作業系統: 我們的檔將路徑會是前斜線`/`

它不只在出理檔案路徑上相當方便，個人覺得它的系統操作，像是檔案讀寫、確認檔案是否存在、列出資料夾內的所有檔案都是相當方便的





## 2. pathlib是什麼?

+ pathlib將各種檔案與資料夾相關的操作全部封装在Path、WindowPath PosixPath類別中，讓檔案與資料夾的操作更加物件導向

簡單來說就是方便我們進行各種檔案與資料夾操作的模組





## 3. pathlib底下的類別有哪些?




![../_images/pathlib-inheritance.png](https://docs.python.org/3/_images/pathlib-inheritance.png)

圖片來源：官網

+ Path: 為PurePath的子類別，該類別用來表示系統路徑風格的具體路徑(實例化後，它會創建 PosixPath或是WindowsPath，這要看大家的作業系統)
+ PosixPath: 為Path與PurePosixPath的子類，此類別用來表示具體的非Windows文件系统路徑

+ WindowsPath: 為Path與PureWindowsPath的子類，此類別用來表示具體的Windows文件系统路徑

提醒: 大家在實作的時候，其實不用特別用PosixPath跟WindowsPath，只要使用Path,它就會根據我們的作業系統來幫助我們創建對的Path類別喔

**補充:PurePath vs Path**

+ Path是PurePath的子類別
+ PurePath可用的函式，Path也都能夠調用

**主要差別:**

+ PurePath主要是用來提供檔案路徑的方便字符串處理
+ Path是PurePath再加上System Calle操作，也就是透過Path才有辦法與我們的作業系統互動，像是讀寫檔案、查看使用者的home目錄、檢查指定檔案有無存在，創建資料夾等等





## 4. Path的各種操作



### 導入Path套件

```Python
## 導入Path套件
from pathlib import Path
```


### 導入我們的測試檔案路徑

+ 傳遞一個檔案的完整路徑到Path

```Python
path = Path('C:\pathlib')
print(type(path))
print(path)
```
執行結果

```
<class 'pathlib.WindowsPath'>
C:\pathlib
```

結果: 由於我用的是Windows作業系統，所以大家可以看到Path會自動幫我建立一個WindowsPath類別





### 取得檔案名/副檔名

**重要: 這邊有一個[cheat sheet]
(https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheel.pdf)可以馬上找到自己想要在檔案路徑中取得的資訊**

```Python
f_path = Path('C:/pathlib/data/test.txt')

## 取得檔案全名
print(f_path.name)
## 取得檔案副檔名
print(f_path.suffix)
## 取得檔案名
print(f_path.stem)
## 如果有多個副檔名的狀況
print(Path('test.txt.gz').suffixes)
```

執行結果
```
test.txt
.txt
test
['.txt', '.gz']
```

### 取得各種檔案路徑

```Python
## 取得檔案路徑
print(f_path.parent)
## 取得一層一層的路徑
print(list(f_path.parents))
## 把檔案路徑轉換成uri格式
print(f_path.as_uri())
## 取得絕對路徑
print(f_path.absolute())
## 取得路徑中最開始的位置 通常就是我們的磁碟機位置
print(f_path.drive)
```

執行結果

```
C:\pathlib\data
[WindowsPath('C:/pathlib/data'), WindowsPath('C:/pathlib'), WindowsPath('C:/')]
file:///C:/pathlib/data/test.txt
C:\pathlib\data\test.txt
C:
```




### 檢查給定的檔案/資料夾是否存在

重要觀念: 不管我們傳進的路徑是否真的有這個檔案，Path都能指向它，並做到一些操作，所以我們要去檢查檔案是真的存在我們的電腦裡面

```Python
## 檢查檔案是否存在
print(f_path.exists())
folder = Path('C:/pathlib/data')
print(folder.exists())
new_file = Path('C:/projects/pathlib_learning/hello.txt')
print (new_file.exists())
new_folder = Path('C:/project/hello/')
print(new_folder.exists())
```
執行結果

```
True
True
False
False
```





### 建立和刪除檔案

```Python
## 檢查檔案是否存在
new_file = Path('C:/pathlib/data/testl.txt')
print (new_file.exists())
## 創建檔案
new_file.touch()
## 檢查檔案是否存在
print (new_file.exists())
## 刪除檔案
new_file.unlink()
## 檢查檔案是否存在
print(new_file.exists())
```

執行結果

```
False
True
False
```



### 判斷是否為檔案、資料夾、Unix Socket - is_file, is_dir, is_socket

```Python
## 創建一個test3檔案
p = Path('C:/pathlib/data/', 'test3.txt')
p.touch()
## 判斷是否為檔案
print (p.is_file())
## 判斷是否為資料夾
print (p.is_dir())
## 判斷路徑是否指向Unix socket檔案
print(p.is_socket())
```

執行結果

```
True
False
False
```



更多判斷: 大家可以直接參考(https://docs.python.org/3/library/pathlib.html#pathlib_Path.is_file) 裡面有更多判斷的用法





### 寫入/讀取檔案

提醒: 這邊我們再來執行一次write_text，它並不會附加在我們之前寫進的資料後面，而是會覆寫它喔

```Python
## 寫進Good
print(p.write_text('Good'))
## 寫進Morning
print (p.write_text('Morning'))
## 讀取檔案內容
print (p.read_text())
```

執行結果

```
4
7
Morning
```






Path也支援我們常用的讀寫檔案方法 - with open() as

```Python
## with open() as 方法
with p.open('w') as f:
    f.write('Good')
p.read_text()
```

執行結果

```
'Good'
```



### 獲取檔案大小

```Python
## 獲取檔案資訊
print(p.stat())
## 取得檔寮大小
print(p.stat().st_size)
```
執行結果
```
os.stat_result(st_mode=33206, st_ino=30962247438309046, st_dev=477207366, st_nlink=1, st_uid=0, st_gid=0, st_size=4, st_atime=1630227096, st_mtime=1630227096, st_ctime=1630227021)
4
```


結果表示檔案大小為4bytes





### 讀取資料夾內所有檔案與資料夾 - iterdir()

```Python
# 獲取資料夾中所有檔案
for f in Path('files').iterdir():
    print(type(f), f)
```
執行結果
```
<class 'pathlib.WindowsPath'> files\a
<class 'pathlib.WindowsPath'> files\b.txt
<class 'pathlib.WindowsPath'> files\c.csv
<class 'pathlib.WindowsPath'> files\d.docx
<class 'pathlib.WindowsPath'> files\e.csv
<class 'pathlib.WindowsPath'> files\f.csv
```





### 對路徑進行操作 - 結合、判斷

```Python
## 透過/來結合路徑
p = Path('C:/')
print(p / 'test3.txt')
print(p/ 'pathlib' / 'data' / 'test3.txt')
print (p/Path('pathlib') / 'data' / Path('test3.txt'))
## 判斷語句 - 判斷檔案路徑是否一樣
print(Path('C:/test.txt') == Path('C:/test.txt'))
print(Path('C:/test.txt') == Path('c: /testl.txt'))
```

執行結果

```
C:\test3.txt
C:\pathlib\data\test3.txt
C:\pathlib\data\test3.txt
True
False
```





## 補充: 工作上可能會遇到的情境



情境: 當我們需要讀取某個資料夾中的所有csv檔，但是資料夾裡面可能有各種檔案類型，那我們需要怎麼處理？

其實很簡單，就是加上一個副檔名來判斷



```Python
## 獲取資料夾中所有為csv的檔案
csv_files = []
for f in Path('files').iterdir():
    if f.suffix == '.csv':
        csv_files.append(str(f))
csv_files
```
執行結果

```
['files\\c.csv', 'files\\e.csv', 'files\\f.csv']
```



pathlib當然還有很多種方法可以使用!我這邊就先列出我覺得大家可能比較常遇到的問題，如果大家想要了解更進階的操作，再請大家參考官網了喔







## Reference
https://docs.python.org/3/library/pathlib.html
https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheet.pdf
https://docs.python.org/zh-cn/3/library/pathlib.html
https://docs.python.org/3/library/pathlib.html#pathlib.PosixPath
