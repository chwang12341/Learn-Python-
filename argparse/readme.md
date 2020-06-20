

## Argparse

**for controling variable through external **



### Import Packages

import argparse



### Introduction 

ArgumentParser()  parameter:

+ prog : program name

+ usage : how to use your program (default=None, it will replace with your program name)

+ description: describe about your program

+ epilog: additional materials

![argparse1](https://github.com/chwang12341/Learn-Python-/blob/master/argparse/images/argparse1.PNG?raw=true)



### Example

1. Optional parameters

   + control variable (ex.args.runtimes)
   + type: int 、str

2. Additional parameters

   you can choose to give the paremeter or not

   + use "--" to form addtional parameters

   + deset: after parsing, the variable name

     ex. add parameter: parser.add_argument('--place', type=str, help='display an integer', dest = 'position')

     ​      form variable name: args.position

![argparse2](https://github.com/chwang12341/Learn-Python-/blob/master/argparse/images/argparse2.PNG?raw=true)

### Execute python

go to cmd and try to run your python like this

1. python learning_argparse.py 10 Shane                             : Static Parameter
2. python learning_argparse.py 10 Shane --place forest     : Additional Parameter (**you can choose to give the paremeter or not**)
3. python learning_argparse.py 10 Shane --food meat        : Additional Parameter
4. python learning_argparse.py 10 Shane --place forest --food toast : Additional Parameter

![argparse3](https://github.com/chwang12341/Learn-Python-/blob/master/argparse/images/argparse3.PNG?raw=true)



*reference: <https://wiki.jikexueyuan.com/project/explore-python/Standard-Modules/argparse.html>*