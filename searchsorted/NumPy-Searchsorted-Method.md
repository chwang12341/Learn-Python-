# 給自己的Python小筆記 - NumPy中的 searchsorted用法 - 實作數據装箱(分組)





 ## 1.  Searchsorted 函數



```
np.searchsorted(a, v, side='left', sorter = None)
```

說明: 於數組a中插入數組v，但不實際插人，而是返回一個索引列表，表示V中的元素應該插在a中哪個位置

**重要提醒: ** 預設的狀況下sorter=None，也就是a數組要為升序數組，也就是要排好從小到大的數組





## 2. 參數




|參數|傳入|說明|
|---|---|
|a|1-D array_like|輸入數組(Input Array)，條件: 當sorted = None時，a必須是升序數組;否則，sorted 不可以為None，存放a中元素的索引(index)，用來反映a數組的升序排列方式|
|v|array_like|用來插入a數組的值，可以是單個元素 、list或是array|
|side|{'left', 'right'}, optional(可選)|
|查詢的方向: 當side = 'left時，會返回第一個符合條件的元素位置; 當side = 'right時, 會返回最後一固符合條件的元素位置，如果都沒有符合的索引，會返回0或N(a的長度)，0表示插入的值比輸人數组的最小值還小，N表示插入的值比輸人數組的最大值還大|
|sorter|1-D array_like, optional(可選)|存儲a數组中元素的index，index對應元素升序|





## 3. 實作



### 構建輸入數組
```Python
## 導人NumPy套件
import numpy as np

## 構建一個NumPy 數組
x = np.array([0,2,8,10,14,17,19,25,29,32,36,58])
x
```

**執行結果**

```
array([ 0,  2,  8, 10, 14, 17, 19, 25, 29, 32, 36, 58])
```





### 1. 插人單個元素




#### A. 插入輸入數組中沒有的元素(介於最大與最小值之間的數)
```Python
## 插入單個元素
ind1 = np.searchsorted(x, 28)
print ('Insert 28:  ', ind1)

## 設定side=left
ind2 = np.searchsorted(x, 28, side = 'left')
print ('Insert 28 and set side = left:  ', ind2)

## 設定side = right
ind3 = np.searchsorted(x, 28, side = 'right')
print('Insert 28 and set side = right: ', ind3)
```

**執行結果**

```
Insert 28:   8
Insert 28 and set side = left:   8
Insert 28 and set side = right:  8
```



#### B. 插入比輸入數組最小值更小的元素



```Python
## 插入比輸人數組的最小值更小的元素

## 設定side = left
ind1 = np.searchsorted(x, -2, side = 'left')
print('Insert 28 and set side = left:  ', ind1)

## 設定side = right
ind2 = np.searchsorted (x, -2, side = 'right')
print('Insert 28 and set side = right:  ', ind2)
```

**執行結果**

```
Insert 28 and set side = left:   0
Insert 28 and set side = right:   0
```





#### C.  插入比輸入數組最大值更大的元素



```Python
## 插入比輸入數组最大值更大的元素
## 設定side = left
ind1 = np.searchsorted (x, 99, side = 'left')
print ('Insert 28 and set side = left:  ', ind1)

## 設定side = right
ind2 = np.searchsorted(x, 99, side = 'right')
print('Insert 28 and set side = right:  ', ind2)
```

**執行結果**

```
Insert 28 and set side = left:   12
Insert 28 and set side = right:   12
```





#### D. 插入值跟輸入數組裡面的元素相等



```Python
## 播入信跟輸人數组裡面的元素相等
## 設定side=left
ind1 = np.searchsorted(x, 2, side = 'left')
print ('Insert 28 and set side = left:  ', ind1)

## 設定side = right
ind2 = np.searchsorted(x, 2, side = 'right')
print('Insert 28 and set side = right:  ', ind2)



## 當插人值跟輸入數組裡面的元素相等, side -'left'和s ide = 'right'結果是不一樣的
## 1.side = left: 會返回與相同元素一樣的位置
## 2.side=right:會返回相同元素的下一個位置
```

**執行結果**

```
Insert 28 and set side = left:   1
Insert 28 and set side = right:   2
```







**結果:當插入值跟输入數組裡面的元素相等，side = 'left'和side = 'right'結果是不一樣的**

1. side="left": 會返回與相同元素一樣的位置

2. side="right": 會返回相同元素的下個位置





### 2. 插入數組

```Python
## 插入值為一個數組
## 設定side = left
ind1 = np.searchsorted(x, [-2,3,8,9,26,28,58,66], side = 'left')
print ('Insert 28 and set side = left:  ', ind1)

## 設定side = right
ind2 = np.searchsorted(x, [-2,3,8,9, 26, 28, 58,66], side = 'right')
print('Insert 28 and set side = right:', ind2)
```

**執行結果**

```
Insert 28 and set side = left:   [ 0  2  2  3  8  8 11 12]
Insert 28 and set side = right: [ 0  2  3  3  8  8 12 12]
```



結果: 返回一個數組







### 3. 當輸人數據沒有排好序(升序)的狀況


**解決方法:** 這時候就要設定sorter，透過np.argsort()找到沒有排好序的翰人數據的正確(升序)索引數組，再带進sorter就可以解決了


```Python
## 當輸入數組不是升序的狀況
## 隐機排列x數組
np.random.shuffle(x)
print ('x = ', x)


## 要先存放x的正確排序索引值
x_sort_index = np.argsort(x)
print('x_sort_index: ', x_sort_index)

## 接下來才能執行插人

## 設定side = left
ind1 = np.searchsorted (x, [-2,3,8,9,26,28, 58,66], side ='left', sorter = x_sort_index)
print('Insert 28 and set side = left:  ', ind1)

## 設定side=right
ind2 = np.searchsorted (x, [-2,3,8,9, 26,28, 58, 66], side = 'right', sorter = x_sort_index)
print('Insert 28 and set side right: ', ind2)
```

**執行結果**

```
x =  [29 19 10 58  2 17 14 36 25 32  0  8]
x_sort_index:  [10  4 11  2  6  5  1  8  0  9  7  3]
Insert 28 and set side = left:   [ 0  2  2  3  8  8 11 12]
Insert 28 and set side right:  [ 0  2  3  3  8  8 12 12]
```



## 應用範例:數據裝箱(分組)



+ 舉例: 我們有1000 個值，想將它們分別放人各個不同的數組分組中，並快速地找到它們在分組數組中的位置， 此時就可以使用searchsorted()函數找到這些值應該被放人哪個箱子

  

  


```Python
import numpy as np
import matplotlib.pyplot as plt

## 隨機產生一個一維並擁有100個標準正態分布的值
np.random.seed(66)
x = np.random.randn(100)

## 自定義一個數據分組, 區間-5到5平均取20個數據點,每個區間為一個數據分組
bins = np.linspace (-5, 5, 20)


## counts為x數值落入區間的計數
counts = np.zeros_like(bins)

## 使用searchsorted, 來獲得x每個數據點在bins中落人的區間序號
i = np.searchsorted(bins, x)
print('Searchsorted Index: ',i)


## 使用at和add, 對x元素在每個區間的元素個數進行計算
np.add.at(counts, i, 1)

## 視覺化
plt.plot(bins, counts, ds = 'steps')
```

**執行結果**

![2](images\2.PNG)