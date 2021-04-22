# 給自己的Python小筆記 - 如何自動刪除檔案和資料夾? - 各種方法教學







## 1. 總表 - 刪除檔案與資料夾的方法比較



|方法|模組|說明|
|---|---|---|
|os.remove()|os|刪除檔案|
|os.unlink()|os|刪除檔案|
|rmdir()|os|刪除資料夾,但資料夾必須為空|
|Path().unlink()|pathlib|刪除檔案|
|removedirs()|os|遞迴刪除資料來,當子資料夾們成功刪除(資料夾必須為空)，才會到其父資料們嘗試刪除|
|glob()|glob|使用匹配的模式搭配remove()來刪除對應規則的檔案|
|rmtree()|shutil|直接刪除整個非空的資料夾|


## 2. os.remove() 方法





1. **說明:**用以刪除指定路径的檔案

2. **可能報錯原因:**

+ 指定的檔案非檔案(像是資料夾)或根本不存在
+ 沒有權限刪除檔案

3. **舉例:** 刪除sample資料夾中的sample_file.txt，並使用try-except來捕捉刪除時遇到的錯誤






```Python
import os

path = 'sample/'

file = 'sample/sample_file.txt'

print('Sample Folder:', os.listdir(path))

try:

    os.remove(file)

except OSError as e:

    print('Delete Problem: ', e)

else:
    print('Delete File')
    print('Sample Folder: ', os.listdir(path))
```

**執行結果**

```
Sample Folder: ['level1', 'not_null', 'python_file.py', 'sample.txt', 'sample_file.txt', 'sample_file1.txt', 'sample_file_example.txt', 'test_folder']
Delete File
Sample Folder:  ['level1', 'not_null', 'python_file.py', 'sample.txt', 'sample_file1.txt', 'sample_file_example.txt', 'test_folder']
```



## 3. os.unlink() 方法



1. **說明:** 用以刪除指定路徑的檔案
2. **舉例:** 刪除sample資料夾中的python_file.py


```Python
import os

path = 'sample/'


print('Sample Folder: ', os.listdir(path))

os.unlink('sample/python_file.py')

print('Delete File')
print('Sample Folder: ', os.listdir(path))
```
**執行結果**

```
Sample Folder:  ['level1', 'not_null', 'python_file.py', 'sample.txt', 'sample_file1.txt', 'sample_file_example.txt', 'test_folder']
Delete File
Sample Folder:  ['level1', 'not_null', 'sample.txt', 'sample_file1.txt', 'sample_file_example.txt', 'test_folder']
```





## 4. rmdir() 方法 - 刪除空的資料夾



1. **說明:** 刪除資料夾，但資料夾必須為空

2. **舉例:** 刪除sample資料夾中的test_folder


```Python
import os

path = 'sample/'

folder = 'sample/test_folder'
print('Sample Folder:', os.listdir(path))

try:

    os. rmdir(folder)

except OSError as e:

    print('Delete Problem: ', e)

else:

    print('Delete File')
    print('Sample Folder: ', os. listdir(path))
```



**執行結果**

```
Sample Folder: ['level1', 'not_null', 'sample.txt', 'sample_file1.txt', 'sample_file_example.txt', 'test_folder']
Delete File
Sample Folder:  ['level1', 'not_null', 'sample.txt', 'sample_file1.txt', 'sample_file_example.txt']
```





## 5. Pathlib 模組 - 刪除檔案



1. 說明: 用以刪除指定路徑的檔案
2. 舉例: 刪除sample資料夾中的sample_file.txt


```Python
from pathlib import Path

path = 'sample/'

file = Path('sample/sample_file1.txt')

print('Sample Folder: ', os.listdir(path))

try:

    file.unlink()
    print('Delete File')
    print('Sample Folder: ', os.listdir(path))

except OSError as e:
    print (f"Delete Problem: {e.strerror}")

```

**執行結果**

```
Sample Folder:  ['level1', 'not_null', 'sample.txt', 'sample_file1.txt', 'sample_file_example.txt']
Delete File
Sample Folder:  ['level1', 'not_null', 'sample.txt', 'sample_file_example.txt']
```



## 6. removedirs() - 刪除資料夾




1. 說明: 遞迴刪除資料夾，當子資料夾們成功刪除(資料夾必須為空)，才會到其父資料夾們嘗試刪除
2. 舉例: 我建立兩層資料夾(levell裡面包含level2)，level2為空的資料夾，levell為只有装載level2的資料夾，我要將level1整個刪除


```Python
import os

path = 'sample/'
folder = 'sample/level1/level2'

print('Sample Folder: ', os.listdir(path))

try:

    os.removedirs (folder)

except OSError as e:

    print('Delete Problem:', e)

else:

    print('Delete File')
    print('Sample Folder: ', os.listdir(path))
```

**執行結果**

```
Sample Folder:  ['level1', 'not_null', 'sample.txt', 'sample_file_example.txt']
Delete File
Sample Folder:  ['not_null', 'sample.txt', 'sample_file_example.txt']
```





## 7. glob - 使用匹配模式來刪除檔案



1. 說明: 使用匹配的模式搭配remove()來刪除對應規則的檔案

2. 舉例: 刪除sample資料夾中所有以sample_為開頭的txt檔案


```Python
import os

import glob

## 刪除以sample_為開頭的txt檔案
all_text = glob.glob('sample/sample_*.txt')

path = 'sample/'

print('Sample Folder: ', os.listdir(path))

for t in all_text:
    try:
        os.remove(t)

    except OSError as e:

        print('Delete Problem: ', e)

print('Delete File')
print('Sample Folder: ', os.listdir(path))
```

**執行結果**

```
Sample Folder:  ['not_null', 'sample.txt', 'sample_file_example.txt']
Delete File
Sample Folder:  ['not_null', 'sample.txt']
```







## 8. rmtree() - 直接刪除整個非空的資料夾



舉例: 刪除整個not_null 資料夾


```Python
import shutil

path = 'sample/'

folder = 'sample/not_null'

print('Sample Folder: ', os.listdir(path))

try:

    shutil.rmtree (folder)

except OSError as e:

    print('Delete Problem: ', e)

else:

    print('Delete File')
    print('Sample Folder: ', os.listdir(path))
```
**執行結果**

```
Sample Folder:  ['not_null', 'sample.txt']
Delete File
Sample Folder:  ['sample.txt']
```






