# Coding起來 - Python工具 - Sphinx操作教學(二) - 如何將reStructured Text(rst)文件轉換成PDF文件 - latex與rst2pdf方法教學 - 更進一步了解Sphinx架構 - Windows系統(上篇)





去年，我有寫一篇對於Sphinx的初探,帶大家建立Sphinx文件，那篇也解釋了為什麼要用Sphinx的觀念，這篇我想带大家再進一步了解Sphinx的架構跟如何将rst檔輸出成pdf，而不是html檔





## 1. 簡單介紹



+ Sphinx是由Python語言所創建的
+ Sphinx可以快速將註解整理成文檔,是一個開發專案上非常好用的文件管理工具
+ Sphinx可以將reStructured Text(rst)檔轉換成不同檔案格式的文檔，像是html、pdf、markdown、LaTex、ePub等



**官網介紹:**

+ Sphinx是一個工具，它能拘輕易地創建智慧和優雅的文檔
+ 由Georg Brandl提出，並由BSD授權
+ 最初是為了Python文檔建立，且具有使用多種語言紀錄文檔的出色功能



**主要特色有:**

+ 输出格式: HTML(包含Windows HTML的幫助)、LaTex(用來輸出PDF格式)、ePub、Texinfo 、manual pages、plain text
+ 廣泛的交叉引用: 語意標紀和對function、class、citation、gossary terms和其它相關資訊的自動鏈接
+ 層次化結構: 輕鬆定義文檔樹，並自動鏈接兄弟姊妹，父母和孩子
+ 自動索引: 常規索引和特定語言的模塊索引
+ 程式碼處理: 使用Pygments螢光筆自動highlighting
+ 擴充: 自動測試程式碼段，包括來自Python模塊的文檔(API docs)等
+ 使用者貢獻的擴充: 使用者貢獻了數十個擴展，而且大多數可以從PyPl安装

**

**翻譯於官網:** https://www.sphipx-doc.org/en/master/







## 2. 環境



### 安装Anaconda(非必須)

網址: https://www.anaconda.com/products individual

由於我是使用Anaconda Prompt來執行下面的命令，所以大家可以選擇是否要跟我一樣



### 安裝Sphinx



```
pip install -U Sphinx
```



### 建立虛擬環境(非必須)



```
## 建立虛擬環境環境
python -m venv sphinx_example
## 激活虛擬環境
sphinx_example\Scripts\activate.bat
```



### 安裝LaTex



**Windows:**

+ MikTex: https://miktex.org/download

(要運行MikTex還需要安装Perl)

+ Perl: https://strawberryperl.com/

由於接下來我們要使用LaTex來幫助我們把Tex檔轉換成PDF檔，所以我們需要LaTex這個環境，如果大家的操作系統(ex. Linux macOS)跟我的不一樣，可以參考這篇 https://mg.readthedocs.io/latexmk.html，它會教大家怎麼配置LaTex環境



### 安裝rst2pdf



另一個將rst檔轉換成PDF檔的套件

**安裝:**

```
pip install rst2pdf
```





## 3. 實作



### 創建Sphinx專案
```
sphinx-quickstart
```


中間的過程會詢問一些專案的基本設定喔，大家可以直接按Enter跳過，或是參考我第一篇的介紹喔



創建好後，會多出這些資料夾

![image1](images\image1.PNG)





### Sphinx中的目錄架構

```
Sphinx Project

|  make.bat
|  Makefile
|
|-  build
L  source
        |  conf.py
        |  index.rst
        |- static
        L _templates
```


1. Makefile: 一個包含各種創建文件指令的項目工程檔案，我們用它來方便我們在建立文檔時，可以輸出成各種檔案格式的文件
2. build: 用來放輸出的檔案
3. make.bat: Windows操作系統所使用的命令語句
4. source: 存放專案源文件的地方，其實就是我們專案的code和檔案那些
   + templates: 使用者自定義的模板
   + static: 靜態文件，像是使用者自定義的樣式表、圖片等
   + index.rst: 首頁，檔案的開始文件，也是用它來告訴Sphinx建立文檔的時候需要包含哪些檔案
   + conf.py: 存放Sphinx相關的設定







### 簡單修改一下我們的專案內容



**修改index.rst**

```rst
Hello!! Welcome to My Documentation
================================


..  toctree::
    :maxdepth: 2
    :caption: Contents:

    Example

Indices and tables
==================
*  :ref: `genindex`

*  :ref: `mod index`

*  :ref: `search`
```





**創建一個Example.rst在同一個目錄下，並撰寫**

```rst
Section 1: Introduction
====================


more detail:  _`My Github link <https://github.com/chwang12341>`_
```





有了這些設定後，我們就準備好要進行生成PDF的動作了喔，由於篇幅的關係，所以我會將接下來的實作放在下一篇喔!!如果大家想一次看，也可以到我的Github中，我會把完整的一篇放在一起







## Reference

https://www.sphinx-doc.org/en/master/

http://ralsina.me/static/manual.pdf

https://dormouse-youngs-blog.readthedocs.io/en/latest/rst-pdf.html

https://codertw.com/程式語言/368794/
