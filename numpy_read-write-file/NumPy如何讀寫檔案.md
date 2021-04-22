# 給自己的Python小筆記 - Numpy如何讀寫檔案? - NumPy獨有的npy和npz二進制檔案格式和text(.txt)檔案格式 - 讀取/寫入教學





YoYo，過去我幾乎都是用Pandas來讀寫檔案，但因為今天工作上接到別人的code，它用了NumPy的方式來讀寫檔案，我覺得超酷的，所以當然就是要來學習一下啦，今天就來教大家如何使用NumPy來讀寫二進制(Binary)格式和 text(.txt)格式的檔案喔 





## 1. NumPy讀寫方法總表





|方法|說明|
|---|---|
|numpy.save()|將array儲存到npy格式的檔案中|
|numpy.savez()|多個array儲存到npz格式的檔案中|
|numpy.load()|將npy或npz中的array載回|
|numpy.savetxt()|以文字檔(.txt)格式儲存資料|
|numpy.loadtxt()|載回文字檔資料|



## 2. 輸出的檔案說明-npy & npz



+ npy: 用來儲存與載入ndarray所需的資料、圖形，dtype等資訊
+ npzi: 與npy相同功能，但是用來存儲多個陣列





## 3. numpy.save() & load()





1. **函式**
```
save(file, arr, allow_pickle=True, fix_imports=True)
```



2. **參數介紹**

   


+ file: 儲存的檔案名稱，副檔名為.npy，如果沒有設定會自動補上
+ arr: 要儲存的array

+ allow_pickle: 預設為True，允許使用Python Pickle來保存對象數組，不允許使用的原因為安全性(可以執行任意操作)和可移植性(pickle對象可能沒辦法在不同容器上加載)，Python的pickle用於儲存或讀取前，對物件進行序列化與反序列化

+ fix_imports: 僅用於將Python3的對象數組轉換為Python2能兼容的pickle





3. **實作**

```Python
import numpy as np

## 創建一個0到9的array
x = np.arange (10)
print('Save: ', x)

## 保存成npy檔
np.save('numpy_sample.npy', x)

## 不特別設定副檔名,會自動存成npy檔
np.save('numpy_samplel.npy', x)

## #npy
y = np.load('numpy_sample.npy')
print('Load': , y)
```
**執行結果**

```
Save:  [0 1 2 3 4 5 6 7 8 9]
Load:  [0 1 2 3 4 5 6 7 8 9]
```





4. **查看一下npy檔的內容**

```Python
## 查看一下npy裡面的內容
!type numpy_sample.npy
```
**執行結果**

```
�NUMPYv{'descr': '<i4', 'fortran_order': False, 'shape': (10,), }    
```



結果: 為NumPy專用的二進制格式資料







## 4. numpy.savez() & load()



1. **函式**

```
savez(file, *args, **kwds)
```



2. **參數介紹**

+ file: 存儲的檔案名稱，副檔名為.npz，如果沒有設定會自動補上

+ args: 保存到檔案中的數組，由於Python不會知道savez以外的數組名稱，所以數組將被自動保存名稱為"arr_0","arr_1"以此類推，但是也可以自己定義名稱(例子會介紹到)，也就是這些參數是可以任意表達的

+ kwds: 存儲到文件的數組所使用的關鍵字名稱



3. **實作**

```Python
import numpy as np

x= np.arange(0, 10)

y = np.cos(x)

z = np.array([[2,4,6], [3,5,8]])

## 將多個array保存為npz
## y使用了關鍵字引數 cos_array,也就是之後會透過這個指定的關鍵字獲取y值
np.savez ('multiple_array.npz', x, z, cos_array = y)

## 載入npz檔
a = np.load('multiple_array.npz')

## 顯示所有array的名稱
print('Array Name: ', a.files)

## 直接print載回的檔案
print (a)

print('Array x: ', a['arr_0'])
print('Array y: ', a['cos_array'])
print('Array z: ', a['arr_1'])
```

**執行結果**

```
Array Name:  ['cos_array', 'arr_0', 'arr_1']
<numpy.lib.npyio.NpzFile object at 0x00000175C7D1FD08>
Array x:  [0 1 2 3 4 5 6 7 8 9]
Array y:  [ 1.          0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219
  0.96017029  0.75390225 -0.14550003 -0.91113026]
Array z:  [[2 4 6]
 [3 5 8]]
```




4. **查看npx的內容**
```
!type multiple_array.npz
```
**執行結果**

```
PK!|菹��
cos_array.npy���NUMPYv{'descr': '<f8', 'fortran_order': False, 'shape': (10,), }                                                           
�?��(J�?rSW&Ｌ諜���殷螟$�串靽愃kp�'�?�"x	溯�? ����?�/c蕪�聶k戌�'篻PK!nE-儘�	arr_0.npy���NUMPYv{'descr': '<i4', 'fortran_order': False, 'shape': (10,), }                                                           
	PK!�<
���	arr_1.npy���NUMPYv{'descr': '<i4', 'fortran_order': False, 'shape': (2, 3), }                                                          
PK!|菹��
�cos_array.npyPK!nE-儘�	�arr_0.npyPK!�<
���	��arr_1.npyPK��
```



## 5. np.savetxt() & np.loadtxt()



1. **函式**
```
savetxt(fname, X, fmt='%.18e', delimiter='', newline='\n', header=", footer = '', comments='#', encoding=None)
```





2. **參數介绍**

+ fname: 檔案名稱
+ X: 要保存的資料
+ delimiter:設定各種分隔符,字符串或字符分隔的列



3. **實作**

**a.** 

```Python
import numpy as np

x = np.arange(10)
print('Save Text: ', x)

##存成txt檔
np.savetxt('example.txt',x)

##載入txt檔
y = np.loadtxt('example.txt')

print('Load Text: ', y)
```

**執行結果**

```
Save Text:  [0 1 2 3 4 5 6 7 8 9]
Load Text:  [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
```







**b. 將整數array轉成浮點數array儲存，並指定分隔符為驚嘆號**


```Python
import numpy as np

x = np.arange(0, 20).reshape(5, 4)
print('Original array:')
print (x)

## 存成浮點數array,並以宣漢賊畢
np.savetxt('example1.txt', x, fmt="%f", delimiter = "!")

## 載入text檔
y = np.loadtxt('example1.txt', delimiter = "!")
print('Load Text: ')
print (y)
```
**執行結果**

```
Original array:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]]
Load Text: 
[[ 0.  1.  2.  3.]
 [ 4.  5.  6.  7.]
 [ 8.  9. 10. 11.]
 [12. 13. 14. 15.]
 [16. 17. 18. 19.]]
```





4. **查看txt內容**

**a.** 

```Python
!type example.txt
```
**執行結果**

```
0.000000000000000000e+00
1.000000000000000000e+00
2.000000000000000000e+00
3.000000000000000000e+00
4.000000000000000000e+00
5.000000000000000000e+00
6.000000000000000000e+00
7.000000000000000000e+00
8.000000000000000000e+00
9.000000000000000000e+00
```

**b.** 


```Python
!type example1.txt
```

**執行結果**

```
0.000000!1.000000!2.000000!3.000000
4.000000!5.000000!6.000000!7.000000
8.000000!9.000000!10.000000!11.000000
12.000000!13.000000!14.000000!15.000000
16.000000!17.000000!18.000000!19.000000
```



