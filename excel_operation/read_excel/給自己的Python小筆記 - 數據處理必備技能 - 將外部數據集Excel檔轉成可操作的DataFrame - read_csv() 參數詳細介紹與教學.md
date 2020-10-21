# 給自己的Python小筆記 - 數據處理必備技能 - 將外部數據集Excel檔轉成可操作的DataFrame - read_csv() 參數詳細介紹與教學 



  嗨嗨，今天來介紹一個我在工作上常用到的一個函式 - pandas.read_excel()，它幫助我讀取Excel檔的資料，並轉換成Python可以進行數據處理的DataFrame格式，是一個非常常用的函式 過去我導入的數據集（Excel檔）幾乎都只有一張工作表work sheet，所以一導入就是我要的資料，但就在距離今天不久前，我同事找我分析某份數據集，但它是在某份Excel檔中的第二個工作表（work sheet）裡，當然也是有很麻煩的解決辦法，就是複製第二張工作表的內容，然後貼到另一份新的Excel檔中，就搞定了，但是我總不能每次都這樣，要是有上萬份的檔案，都要這樣處理，我就Amazing了XD，所以我就想仔細地瞭解一下pandas.read_excel()底下到底有哪些參數可以使用，是否可以幫助我解決這個問題，並把我學習到的記錄下來，幫助自己與有需要的大家，下次遇到這個問題，就能夠輕鬆解決



## pandas.read_excel()是要做什麼的？



+ 它幫助我們將Excel檔導入進我們的Python程式中，並轉換成DataFrame格式，方便我們使用Python來對數據進行操作，

+ 它可以導入我們Local端的文件，或從URL上讀取文件，像是Github就有像[https://raw.githubusercontent.com/plotly/datasets/master/data.csv](https://raw.githubusercontent.com/plotly/datasets/master/data.csv?fbclid=IwAR36OVxVnXgqiHzLwzNUmFfj6hAZokEMhqm6J4XbFKjlAcEiBR--dDs3WoQ) 這樣的網址可以讀取網址上的csv數據集data

+ 但它所導入的副檔名須符合像xls, xlsx. xlsm, xlsb和odf的檔案





## pandas.read_excel()參數



```
read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=False, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=True, mangle_dupe_cols=True, **kwds)
```



我接下來會用實作的方式帶大家瞭解這些參數的意義



## 補充： 如何使用Jupyter Notebook快速取得這個函數的參數，以及這個參數的說明呢？  



 **兩種方式** 

+ 第一種： 使用help()函數來幫忙，像是help(pd.read_excel) 

+ 第二種： 把pd.read_excel()打字的輸入線移到函數括號內，並按下Shift + Tab，就會跳出資訊了  





## 實作用的數據介紹 



這份是我自己捏造的數據集喔，我有放在Github上，大家可以下載下來當練習用，這份Excel檔中，有三頁工作表，如下圖第一張工作表是顧客的基本資料，第二張是消費記錄表，第三張是旅遊記錄表 



圖一： 數據集Excrl檔中 - 有三頁工作表 



![image1](images\image1.PNG)



圖二： 第一張工作表 



![image2](images\image2.PNG)



圖三： 第二張工作表 



![image3](images\image3.PNG)



圖四： 第三張工作表





![image4](images\image4.PNG)





## 參數的介紹與實作 



#### 1. io: 欲導入的Excel檔路徑與檔名，像是io = "填入位置路徑 + 檔名"，也可以直接省略io =，直接填入位置路徑加檔名就好 



程式碼範例 

```Python
## 導入Pandas 套件
import pandas as pd

## 讀取檔案
df = pd.read_excel('data/dataset_example.xlsx')

## 顯示資料
df
```

**執行結果**

![image5](images\image5.PNG)







#### 2. sheet_name(str, int, list, or None, default 0) : 讀取指定的工作表 



**可以傳入參數的格式** 

+ 傳入整數(ex. 0,1,2...): 指定特定位置的工作表，像0就是第一張工作表，1就是第二張工作表，以此類推，預設為0，表示導入第一張工作表，並轉換返回一個DataFrame格式的資料表 

+ 傳入字串（string）: 指定特定名稱的工作表，像是"Consumption_Record"就是指定導入名稱為"Consumption_Record"的工作表，並轉換返回一個DataFrame格式的資料表 

+ 傳入串列(ex. [0,1]): 一次導入多個工作表，像[0,1]就是指一次導入第一張與第二張工作表，也可以像[2,"Consumption_Record"]就是導入第三張與名為"Consumption_Record"的工作表，它會返回一個OrderDict類型的數據，並會將這些工作表合併於一個list中 

+ 傳入None: 表示將全部工作表載入，它會返回一個OrderDict類型的數據，並會將這些數據合併在一個list中 

  

**程式碼範例**

```Python
## 導入pandas套件
import pandas as pd

## 讀取第三章工作表
a_int = pd.read_excel('data/dataset_example.xlsx', sheet_name = 2)

## 讀取'Consumption_Record'工作表
b_string = pd.read_excel(io = 'data/dataset_example.xlsx', sheet_name = 'Consumption_Record')

## 讀取第一張與第三張的工作表
c_list = pd.read_excel(io = 'data/dataset_example.xlsx', sheet_name = [0,2])

## 讀取第三張與'Consumption_Record'工作表
d_list = pd.read_excel(io = 'data/dataset_example.xlsx', sheet_name = [2, 'Consumption_Record'])

## 讀取全部的工作表
e_all = pd.read_excel(io = 'data/dataset_example.xlsx', sheet_name = None)
```



**執行結果**

![image6](images\image6.PNG)



![image7](images\image7.PNG)





+ 補充： 從上面的結果，如果我們是傳入一個串列list，像是c_list與d_list那樣，就可以在結果上用像是c_list[2], d_list["Consumption_Record"]，來將合併成OrderDict的數據類型，再次分開成單獨的DataFrame格式，但要指定為我們sheet_name的切割方式，像是如下的程式碼，如果我輸入c_list[1]這樣會報錯，大家要注意這一點

  

+ 程式碼範例

```Python
## 顯示數據
#c_list[0]
c_list[2]
```

```Python
## 顯示數據
#d_list[2]
d_list['Consumption_Record']
```

**執行結果**



![image8](images\image8.PNG)





#### 3. header(int, list of int, default 0): 指定哪一列為最上方的列名 



**參數可以傳入的格式** 

+ 整數（int）: 傳入1，代表指定第二列為列名，以此類推，預設為0，代表指定第一列為列名 

+ 串列：將串列中的列位置都當成是列名，讓多列同時成為列名，像是[0,1,2]就是將第1、2、3列都成為列名

+ 傳入None: 表示不使用任何數據裡的列當成是列名 

  

+ 程式碼範例 

```
## 導入pandas套件
import pandas as pd

## 讀取第一張工作表，且以第一列當列名
a_int = pd.read_excel('data/dataset_example.xlsx', header = 0)

## 讀取第一張工作表，且以第三列為列名
b_int = pd.read_excel('data/dataset_example.xlsx', header = 2)

## 讀取第一張工作表，且以第一，二，三列當列名
c_list = pd.read_excel('data/dataset_example.xlsx', header = [0,1,2])

## 讀取第一張工作表，且不以任何數據列當列名
d = pd.read_excel('data/dataset_example.xlsx', header = None)
```

**執行結果**

![image9](images\image9.PNG)





![image10](images\image10.PNG)



+ 小提醒： 當指定列名為原數據的哪些列或哪一列時，在它上面的列都會被拿掉，像是header = 2的話，原數據前二列的數據就會被拿掉，只產生指定第三列以下的數據列





#### 4. names(array-like, default None): 指定一個自定義的列名 



**可以傳入參數的格式** 

+　串列（list）: 傳入自定義的名稱，但要注意數量要與原數據的列名一樣數量 
+　程式碼範例 

```Python
## 導入pandas套件
import pandas as pd

a_list = pd.read_excel('data/dataset_example.xlsx', names = ['顧客編號', '姓名', '年齡', '身高', '體重', 
                                                             '性別', '職業'])

## 顯示數據
a_list
```

**執行結果**



![image11](images\image11.PNG)





#### 5. nrows(int default None): 指定欲讀取前多少行 



**可以傳入參數的格式** 

+ 整數（int）: 傳入整數，像是傳入6代表讀取前面6行 程式碼範例

```Python
## 導入pandas套件
import pandas as pd

## 只導入前四行數據
a_int = pd.read_excel('data/dataset_example.xlsx', nrows = 4)

## 顯示數據
a_int
```



**執行結果**



![image12](images\image12.PNG)



#### 6. na_values(scaler, str, list-like, or dict, default None): 將指定的欄位字串，改成NaN 

可以傳入參數的格式 

+ 字串（str）：像是如果是用我的範圍數據集傳入'M'，就會將所有'M'的欄位改成NaN 
+ 程式碼範例   

```Python
## 導入pandas套件
import pandas as pd

## 將所有'M'的欄位改成NaN 
a_str = pd.read_excel('data/dataset_example.xlsx', na_values = 'M')

## 顯示數據
a_str
```

**執行結果**



![image13](images\image13.PNG)







#### 7. keep_default_na(bool, default True): 是否將原本為空值的數據導入，並給予NaN 

可以傳入參數的格式 

+ Boolean: 傳入True 或 False，預設為True，代表導入空值，並填為NaN 
+ 程式碼範例

```Python
## 導入pandas套件
import pandas as pd

## 不要傳入有空值的數據
a_bool = pd.read_excel('data/dataset_example.xlsx', keep_default_na = False)

## 顯示數據
a_bool
```

**執行結果**



![image14](images\image14.PNG)





#### 8. skiprows(list-like): 將指定的行數跳過不導入進來 



**可以傳入參數的格式** 

+ 整數（int）: 如果為1，就是跳過第一行，為6，就是跳過第6行，以此類推 

+ 串列（list）: 可以指定跳過哪些行，像是[1,4,5,6] 就是跳過1,4,5,6行

+ lambda函數： 可以使用lambda來指定欲跳過的行 

  

+ 程式碼範例  

```Python
## 導入pandas套件
import pandas as pd

## 跳過第二行
a_int = pd.read_excel('data/dataset_example.xlsx', skiprpws = 2)

## 跳過1,3,6行
b_list = pd.read_excel('data/dataset_example.xlsx', skiprpws = [1,3,6])

## 跳過偶數行
c_func = pd.read_excel('data/dataset_example.xlsx', skiprpws = lambda x: x%2 == 0)
```



**執行結果**



![image15](images\image15.PNG)







#### 9. index_col(int, list of int, default None): 指定哪一列為索引列 



**可以傳入參數的格式** 

+ 整數（int）: 指定哪一列為索引列

+ None: 為預設的值，代表它會自動幫我們創建一列，以0開始的索引列

+ 串列（list）: 指定哪些列為索引列 

  

  

+ 程式碼範例

```Python
## 導入pandas套件
import pandas as pd

## 把第一列當成索引列
a_int = pd.read_excel('data/dataset_example.xlsx', index_col = 0)

## 不把數據中任何一列當成索引列
b_none = pd.read_excel('data/dataset_example.xlsx', index_col = None)

## 把第一，四，六列當成索引列
c_list = pd.read_excel('data/dataset_example.xlsx', index_col = [0,3,5])
```



**執行結果**



![image16](images\image16.PNG)





#### 10. true_values & false_values(list, default None): 指定數據中的哪些值，為True或False 



可以傳入參數的格式 

+ 串列（list）: 指定數據中哪些要轉為True或False的值，像是true_values['M']就是把數據中的'M'轉為True，false_values['M']就是把數據中的'M'轉為False 

  

+ 程式碼範例

```Python
## 導入pandas套件
import pandas as pd

## 將數據集中的'M'改為True，'F'改為Fasle
a_list = pd.read_excel('data/dataset_example.xlsx', true_values = ['M'], false_values = ['F'])

## 顯示數據
a_list
```

**執行結果**



![image17](images\image17.PNG)









#### 11. dtype(Type name  or dict of column -> type, default None): 改變數據類型，預設為None，代表不改變原數據類型 



**可以傳入參數的格式** 

+ Pandas 所以包含的所有數據類型  



![image18](images\image18.png)





+ 程式碼範例 
+ 1. 原本的數據類型 

```Python
## 導入pandas套件 
import pandas as pd

## 導入原本數據的前七行數據
a = pd.read_excel('data/dataset_example.xlsx', nrows = 7)

## 顯示數據資訊
a.info()
```



+ 2. 更改過後的數據類型：先將最後一列NaN值拿掉，並將Age, Height 和 Weight改為浮點數類型



```Python
## 導入pandas套件
import pandas as pd

## 先將最後一列有NaN值得拿掉，並將Age、Height和Weight改為浮點數類型
a = pd.read_excel('data/dataset_example.xlsx', nrows = 7, dtype = {2: 'float64', 3:'float64', 4:'float64'})

## 顯示數據資訊
a.info()
```



**執行結果**



![image19](images\image19.png)





#### 12. usecols(int, str, list-like, or callable default None): 指定讀取excel中哪些列 



**可以傳入參數的格式** 

+ 串列（list）: 指定要解析哪幾列 

+ None: 預設值為None，代表解析所有列 

+ 字串（list）: 指定Excel檔中列的字母序號，使用":"來代表列字母序號的範圍，","來代表要指定哪些列，像是"A:E"，代表解析A到E列，而"A,C,E:F"，代表解析A、E和E到F列 

  

+ 程式碼範例

```Python
## 導入pandas套件
import pandas as pd

## 指定解析第1與4列
a_list = pd.read_excel('data/dataset_example.xlsx', usecols = [0,3])

## 指定解析A列到C列
a_str1 = pd.read_excel('data/dataset_example.xlsx', usecols = 'A:C')

## 指定解析A列到C列
a_str2 = pd.read_excel('data/dataset_example.xlsx', usecols = 'A,C')

## 指定解析A列、B列和D到F列
a_str3 = pd.read_excel('data/dataset_example.xlsx', usecols = 'A,B ,D:F')
```

**執行結果**

![image20](images\image20.PNG)

![image21](images\image21.PNG)









#### 13. squeeze(bool, default False): 當指定解析只有一列時，會回傳成Series格式



**可以傳入參數的格式**

+ Boolean: True 或 False，預設為False，為True時，當指定解析的只有一列，會回傳成Series格式



+ 程式碼範例

```Python
## 導入pandas套件
import pandas as pd

## 指定解析一列，並回傳成Series格式
a = pd.read_excel('data/dataset_example.xlsx', usecols = [2], squeeze = True)

## 顯示數據類型
print(type(a))

## 顯示數據
a
```

**執行結果**



![image23](images\image23.PNG)







### 14. engine(str, default None): 使用哪種的第三方解析庫，都是用來解析Excel檔的



**可以傳入參數的格式**

+ 第三方解析庫： xlrd, openpyxl, odf

+ None: 為預設值，代表不需要使用第三方解析庫

  

  







#### 15. converters(dict, default None): 使用函數來對指定的列，進行自定義的數據處理，可以使用Python的def或lambda方法



**可以傳入參數的格式**

+ 字典（dict）: 第一個參數是key，為指定的列名或列的序列碼，為函數，可以使用Python的def或lambda方法



+ 程式碼範例

```Python
## 導入pandas套件
import pandas as pd

##將Customer_id那一列都加上100，然後Age那一列，在後面都加上years old
a = pd.read_excel('data/dataset_example.xlsx', 
                  converters = {0: lambda x: x+100, 2: lambda x: str(x) + " years old"})

## 顯示數據
a
```

**執行結果**



![image28](images\image28.PNG)





+ **補充： 更多使用Pandas來導入不同文件格式方法，可以直接參考官網（[https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table）的整理喔](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html?fbclid=IwAR2UNL2T1cFyr9-SOKCddilRZTmMaItu5uV6cOcPSSdt1DkSTetfCoXqOT8#io-read-csv-table）的整理喔)**









**當然還有一些參數我沒有介紹到，但這邊列出了許多我們比較常用到的參數，如果大家想瞭解更多，可以直接使用help(pandas.read_excel)這個方法來查詢所有參數的用法說明喔，對這個方法有了很大的了解後，日後我們需要導入Excel檔的時候，就能在導入前先進行初步的數據處理了，像是我們可以先指定好要解析導入哪些列，才不用通通都導入後，再把用不到的列拿掉，如果遇到擁有很多工作表的時候，也能輕鬆指定我們欲導進來的工作表喔**







## Reference



[https://zhuanlan.zhihu.com/p/142972462](https://zhuanlan.zhihu.com/p/142972462?fbclid=IwAR3_b1Njhk1YBcXkJaRxeG0oUvNScUqdXKTQRNrhRB3IKM8Tk5BlSv9TEQY)

[https://blogs.csdn.net/brucewong0516/article/details/79096633](https://blogs.csdn.net/brucewong0516/article/details/79096633?fbclid=IwAR0_mxaz-Gb8PfRgtBUf_ZtWEIfWWrDEZHxlvrvzfVOuKT_gxEwJMleGQ1U)









