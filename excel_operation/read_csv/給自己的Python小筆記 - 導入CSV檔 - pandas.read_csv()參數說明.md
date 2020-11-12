# 給自己的Python小筆記 - 導入CSV檔 - pandas.read_csv()參數說明





YoYo，今天來介紹另一種使用Pandas來讀取Excel檔的方法，但這次不同的地方是Excel檔的副檔名需要為CSV檔喔，而我們要使用的是pandas.read_csv()這個方法，由於上一篇介紹過的pandas.read_excel()與這次要分享的方法，在很多參數上是相仿的，所以我這篇就不實作囉，大家可以根據這篇的參數說明自己試試看





## read_csv() & read_excel() 都是導入Excel檔，並轉換成Python可操作的DataFrame格式，那它們最大的差別是什麼？ 



答案非常簡單，除了參數的差別，它們使用上的不同在，雖然都是導入Excel檔，但是所導入的Excel檔格式並不相同喔，有些Excel檔需要read_csv()來導入，有些則需要read_excel來導入喔





## pandas.read_csv()所有的參數 



**利用Python查詢pandas.read_csv()所有參數與說明**

```Python
import pandas as pd

help(pd.read_csv)
```



**所有參數**

```
read_csv(filepath_or_buffer: Union[str, pathlib.Path, IO[~AnyStr]], sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal: str = '.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)
```







## 參數介紹 



#### 常使用到的參數





| **參數**           | **傳入參數的值**                                           | **說明**                                                     |
| ------------------ | ---------------------------------------------------------- | ------------------------------------------------------------ |
| filepath_or_buffer | str,  path, object or file-like object                     | 指定檔案路徑，也可以是URL字串（有效的URL包含  http, ftp, s3 位址，或是擁有read()方法的物件，像是open  file或StringIO物件） |
| sep                | str,  default ','                                          | 指定分隔符，預設為','，也就是用逗號分隔，分隔符需要長於一個字符，並且不能是'\s+'，可以使用的分隔符有像是正則表達式的方式："\r\t"等等 |
| delimiter          | str,  default None                                         | 定界符，為備選的分隔符，如果有指定這個參數，sep參數就會失效  |
| delim_whitespace   | bool,  default False                                       | 指定空格（' '  or '\t' ）是否會用於定界符（delimiter），它等同於sep  = '\s+'的效果，如果有指定這個參數，delimiter參數就會失效 |
| header             | int,  list of int,  default 'infer':                       | 指定數據中哪一列為列名，如果傳入1，代表指定第二列為列名，以此類推，預設為0，也就是指定第一列為列名，而傳入[0,1,2]就是將第一、二、三列都當成是列名，傳入None，表示不使用任何數據裡的列當成是列名 |
| names              | array-like,  optional                                      | 指定一個自定義的列名，傳入一個串列，裡面裝自定義的名稱，但要注意數量要與原數據的列同數量 |
| index_col          | int,  str,  sequence of int / str,  or False, default None | 指定哪一列為索引列，傳入整數來指定哪一列來成為索引列，傳入串列，裝多個整數，來指定哪些列為索引列，預設為None，代表它會自動創建以0開始的列，來當索引列 |
| usecols            | list-like  or callable, optional                           | 指定讀取Excel檔中的哪些列，傳入串列（list）來指定要解析導入哪些列，傳入字串（str）用Excel檔中的序列字母來指定要導入哪些列，使用":"來代表字母序號的範圍，","代表咬指定哪些列，像是"A:E"，代表解析導入A到E列，而"A,  C, E:F"，代表解析導入A、C和E到F列，預設值為None，代表解析導入所有列 |
| squeeze            | bool,  default False                                       | 當解析導入的只有一列時，會轉成Series格式                     |
| prefix             | str,  optional                                             | 在header  = None沒有指定列名的時候，給列添加前綴，header為None時，會自動生成0,1,2,3,4...的列名，這時加上prefix  = 'A'，就會產生新的列名為A1,  A2, A3, A4... |
| mangle_dupe_cols   | bool,  default True                                        | 預設為True，代表當有重複出現的列名時，像是'A'...'A'，將列名替換成'A',  'A.1', 'A.2'...'A.N'，如果傳入False，就會將重複名稱的列名覆蓋掉 |
| nrows              | int,  optional                                             | 指定欲讀取前幾行                                             |
| na_values          | scaler,  str,  list-like, or dict,  optional               | 將指定的數據欄位字串值，改為NaN                              |
| skip_blank_lines   | bool,  default True                                        | 當設置為True時，會跳過所有值為空值的行，而不是填入NaN，然後解析導入 |
| dtype              | Type  name or dict of  column -> type, optional            | 改變原數據類型，預設為None，表示不改變原數據類型，像是dtype  = {2: 'float64', 3:'float64', 4:'float64'}，代表會將第三、四、五列的數據類型改為浮點數類型 |



**這篇我想當成是大家在導入CSV檔時候，不用記得所有參數，需要用到的時候，再來看看的小筆記，所以有些可能比較不常用到的參數，我這邊就不做介紹囉，有興趣的大家可以直接參考官網（[https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table）喔](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html?fbclid=IwAR3eZWtkbclFCO_xlCPZmfnYH2XE0Zkfe90_dbNdHTYLEbQCJUuyCseBQhc#io-read-csv-table）喔)**





**想知道更多使用Pandas導入不同檔案類型的方法，也可以參考官網這頁（[https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table）喔**](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html?fbclid=IwAR321Nzr1ADFuL8hNKoSkDF2azeikNPk8qFSfOqLAzzlTLk8bzggolVs8pE#io-read-csv-table）喔)









## Reference



[https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html?fbclid=IwAR1xv1mbDqEk0GyAn2ksSUo-UxWCJ5KOutNASm_8DgsvjwIXJT6GRjTf-5k#io-read-csv-table)

[https://blog.csdn.net/zhangjianjaEE/article/details/78543743](https://blog.csdn.net/zhangjianjaEE/article/details/78543743?fbclid=IwAR2fvTmFPMIOBCmxJPGztpreWtqLtBhhuAZlY-WUBXqamMd5KXld4TMd8_A)