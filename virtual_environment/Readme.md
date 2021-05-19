

# 給自己的Python小筆記 - 解決環境套件安裝與版本問題，開始建立一個乾淨的環境 - 如何建立虛擬環境 - env 和 virtualenv 套件教學 - Windows系統





**由於過去不同專案的需求電腦裡累積了一堆套件?不清楚哪些專案需要哪些套件?不同專案所使用的套件版本又不同所造成的問題?解決環境套件安裝與版本問題，開始建立一個乾淨的環境**





嗨嗨，由於最近工作老是被問到，這個專案環境需要安装什麼套件?我用你寫的步驟，但是環境一直有問題?我突然意識到很多套件都是我在過去不同專案中所累積安装的，所以突然被問這個專案需要什麼套件，不知道要怎麼回答，總不能把我安装過的套件通通給他xd 每次問題一來，我第一個腦海裡浮現的是，你在說哪個專案，啊我這邊可以，你為什麼不行xd 然後就只能一句一句幫他看，報錯的原因跟解決所需要的套件，所以我決定在往後的專案中，每次開一個新專案，就建立一個新環境來安装套件，這樣就清楚明瞭了，但總不能每次開新專案，就砍掉以前的吧，所以這時候虛擬環境對我來說的重要性就出來了xd







## 1. 虛擬環境是什麼?



+ 一種獨立出來的Python執行環境，原理是借助虛擬機docker把一部分的內容獨立出來，稱為容器也就是虛擬環境，我們可以在不同的虛擬環境中下載這個專案需要的套件就好，而每個Python虛擬環境互相不影響
+ 建立好後會是一個獨立的資料來,裡面有Python版本和所安装的套件





## 2. 虛擬環境的應用場景



+ 在學習的過程中怕安装了一堆有的沒有的套件影響電腦
+ 每個專案需要的套件版本不同，一直為不同專案重新安裝案件版本很麻煩，像是專案A需要Python3.6.5，但是專案B需要的則是Python2
+ 當被問到這個專案需要什麼套件時，可能會忘記自己安裝了什麼，或因為以前別的專案有安装過所以不知道還需要裝哪些








## 3. Python的虛擬環境套件



### venv

Python内建用來管理與建立虛擬環境的套件，不需要額外下載



#### STEP 1: 建立虛擬環境

command: python-m venv (虛擬環境名稱)

```
python -m venv virtual_env
```

![image1](images\image1.PNG)

**系統就會在執行的目錄底下創建一個virtual_env的folder**



#### STEP 2: 開啟虛擬環境

Command: (虛擬環境資料夾名稱)\Scripts\activate.bat
```
virtual_env\Scripts\activate.bat
```


當命令提示字元前面出現(virtual_env)，像是(virtual_env)(bäse) (資料夾路街)，表示成功進入了，就可以開始嗨了!!

![image2](images\image2.PNG)







#### STEP 3: 退出虛擬環境

Command: (虛擬環境資料夾名稱)\Scripts\deactivate.bat
```
virtual_env\Scripts\deactivate.bat
```
當(virtual env)不見了表示成功退出了

![image3](images\image3.PNG)







### virtualenv





#### STEP 1: 安裝套件

```
pip install virtualenv
```



#### STEP 2: 建立虛擬環境

command: virtualenv (虛擬環境名稱)
```
virtualenv virtual_env_1
```

![image4](images\image4.PNG)





#### STEP 3: 開啟虛擬環境


Command: (虛擬環境資料夾名稱)\Scripts lactivate.bat
```
virtual_env_1\Scripts\activate.bat
```

當命令提示字元前面出現(virtual_env_1)，像是(virtual_env_1)(base) (安料夾路徑)，就表示成功進入了，這樣就可以開始發揮了!!xd



#### STEP 4: 退出虛擬環境

Command: (虛擬環境的資料夾名稱)\Scripts\deactivate.bat
```
virtual_env_1\Scripts\deactivate.bat
```


當(virtual_env_1)不見了，表示成功退出了

**兩個套件步驟幾乎是一樣的，只只差在指令略有不同跟一個要下載套件一個是內建的**





## 4. 補充: 一些管理套件的方法



我們先進到前面建立的虛擬環境中





### 安裝最新版本的套件

command: pip install (套件名稱)
```
pip install plotly
```



### 安裝指定版本的套件

command: pip install (套件名稱)==(套件版本)
```
pip install xlrd==1.2.0
```



### 把安裝好的套件升級到最新版

command: pip install --upgrade (套件名稱)
```
pip install --upgrade xlrd
```



### 查看當前環境有哪些套件

```
pip list
```

**執行結果**

![image5](images\image5.PNG)







### 顯示套件資訊

command: pip show (套件名稱)
```
pip show xlrd
```

**執行結果**

![image6](images\image6.PNG)







### 將安裝的套件輸出成一個清單(txt檔)

command: pip freeze > (套件清單名稱).txt
```
pip freeze > requirement.txt

## 查看清單內容 - Linux
cat requirement.txt
## 查看清單內容 - Windows
type requirement.txt
```

**執行結果**

![image7](images\image7.PNG)





### 透過這份套件清單，直接下載所需套件



command: pip install -r (套件清單名稱).txt
```
pip install -r requirement.txt
```

**執行結果**

![image8](images\image8.PNG)









## Reference

https://docs.python.org/zh-tw/3.9/tutorial/venv.html

https://blog.csdn.net/godot06/article/details/81079064
