# Coding起來 - Python工具 - Sphinx操作教學(二) - 如何將reStructured Text(rst)文件轉換成PDF文件 - latex與rst2pdf方法教學 - 更進一步了解Sphinx架構 - Windows系統





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





### 生成PDF文件



#### Method 1: Latex



##### STEP 1: 修改conf.py

在conf.py添加

```Python
#-- Options for latex output ----------------------------

latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'preamble': r'''
\usepackage{xeCJK}

\setCJKmainfont[BoldFont=STZhongsong, ItalicFont=STKaiti]{STSong}
\setCJKsansfont[BoldFont=STHeiti]{STXihei}
\setCJKmonofont{STFangsong}
\XeTexlinebreaklocale "zh"
\XeTexlinebreakskip = Opt plus 1pt
\parindent 2em
\definecolor (VerbatimColor}{rgb}{0.95,0.95,0.95)
\setcounter{tocdepth}{3} \renewcommand\familydefault{\ttdefault}
\renewcommand\CJKfamilydefault{\CJKrmdefault}

''',
}
```





##### STEP2: 將rst檔轉換成tex檔



到專案目錄下執行

```
make latex
```


結果: 會在build中產生latex資料夾，裡面會將原本的rst檔轉換成tex檔

![image2](C:\Users\user\Desktop\Learn-Python-\sphinx\sphinx_more\images\image2.PNG)



##### STEP 3: 將tex檔轉換成pdf檔

到build/latex目錄中執行

```
make
```

或是

```
xelatex (要轉換的tex檔).tex
```


在執行xelatex指令的時候，可能會跳出一堆需要安裝的套件，就給它安裝就對了xd

原理上就會產出我們要的pdf檔確xd

**提醒:** 我照網路上很多的教學步驟走，但是我這邊的latex，在我不同電腦上，有的有問題，於是我再找了下面的方法教大家使用rst2pdf來完成rst轉換pdf





#### Method 2: rst2pdf



##### STEP 1: 安裝套件

```
pip install rst2pdf
```



##### STEP 2: 修改conf.py

把新增的套件放人Sphinx配置

```Python
# -- General configuration ------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


extensions = [
    'sphinx.ext.autodoc', 
    'rst2pdf.pdfbuilder'

]
```



並接著配置pdf輸出相關的配置

```Python
# -- Options for PDF output -------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\
# For example: Guido van Rossum\\Fred L. Drake. Jr., editor"
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# (index.u MyProject', u'My Project', u'Author Name,
# dict(pdf compressed True))
# would mean that specific document would be compressed
# regardless of the global pdf compressed setting.
pdf_documents = [
('index', u'My Learning Note', u'My Learning Note', u'Jack\\Una'),
]


# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['a4', 'my_stylesheets']

# Create compressed PDF
# Use True/False or 1/0
# Example: compressed-True
pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:

pdf_font_path = ['C:\Windows\\Fonts']

# Language to be used for hyphenation support
# pdf_language = 'zh-CN'
pdf_language = 'en'

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
pdf_break_level = 0

# When a section starts in a new page. force it to be even', 'odd',
# or just use any
pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
pdf_verbosity = 0

# If false, no index is generated.
pdf_use_index = True

# If false, no modindex is generated.
pdf_use_modindex= True

# If false, no coverpage is generated.
pdf_use_coverpage = True

# Documents to append as an appendix to all manuals.
#pdf_appendices = []

# Enable experimental feature to split table cells. use it
# if you get "DelayedTable too big" errors
#pdf_splittables = False

# Set the default DPI for images
pdf_default_dpi = 72

# Enable rst2pdf extension modules (default is only vectorpdf)
# you need vectorpdf if you want to use sphinx's graphviz support
#pdf_extension = ['vectorpdf']


# Page template name for "regular" pages
#pdf_page_template= 'cutePage'

# Show Table of Contents at the beginning?
pdf_use_toc = False

# How many levels deep should the table of contents be?
pdf_toc_depth = 4

# Add section number to section references 
pdf_use_numbered_links = True

# Background images fitting mode 
pdf_fit_background_mode = 'scale'
```



我們上面有指定一些pdf的樣式(pdf_stylesheets = ['a4', 'my_stylesheets'])，a4代表輸出的PDF格式為A4紙大小，而後面my_stylesheets就是我們想要自定義一下自己的樣式表



##### STEP 3: 在專案目錄下创建my_stylesheets.json來撰寫字體樣式



在專案目錄下創建my_stylesheets.json來撰寫字體樣式，字體的選擇大家可以參考自己作業系统上有的字體喔


```JSON
{
"embeddedFonts": [
"simkai.ttc"
],

"fontsAlias": {

"stdFont": "simkai",
"stdBold": "simkai".
"stdItalic": "simkai".
"stdBoldItalic": "simkai",
"stdMono": "simkai",
"stdMonoBold": "simkai".
"stdMonoItalic": "simkai",
"stdMonoBoldItalic": "simkai".
"stdSans": "simkai",
"stdSansBold": "simkai",
"stdSansItalic": "simkai",
"stdSansBoldItalic": "sinkai"
},

"styles": [
[
"base",
{
"wordwrap": "CJK"
}
],
[
"literal",
{
"wordwrap": "None"
}
]]}
```



**解釋**


+ embeddedFonts: 代表欲嵌入的字體，我這邊選擇的是中意楷體
+ fontsAlias: 指定各種類型的字要使用的字體，stdFont原文字體，stdBold 粗體字等
+ wordWrap: 設定換行規則，CJK是中日韓文字的換行規則


**提醒:字體必須是TTF類型**



##### STEP 4: 修改make.bat(設定編譯的時候的指令碼)

在make.bat中添加

```
if "%1" == "pdf" (
%SPHINXBUILD% -b pdf %ALLSPHINXOPTS% %BUILDDIR%/pdf
if errorlevel 1 exit /b 1
echo.
echo.Build finished. The pdf files are in %BUILDDIR%/pdf.
goto end
)
```





##### STEP 5: 輸出PDF檔



回到專案目錄中，執行

```
make pdf
```





##### STEP 6: 檢視結果



結果: 在build資料夾中建立了pdf資料夾，我們要的結果會在裡面

![image3](C:\Users\user\Desktop\Learn-Python-\sphinx\sphinx_more\images\image3.PNG)

















## Reference

https://pypi.org/project/rst2pdf/

https://www.sphinx-doc.org/en/master/

http://ralsina.me/static/manual.pdf

https://dormouse-youngs-blog.readthedocs.io/en/latest/rst-pdf.html

https://codertw.com/程式語言/368794/
