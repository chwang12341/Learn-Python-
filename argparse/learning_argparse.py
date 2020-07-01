## learning_argparse.py


## import package
from argparse import ArgumentParser

## Introduce

##parameter
## prog : program name
## usage : how to use your program (default=None, it will replace with your program name)
## description: describe about your program
## epilog: additional materials
parser1 = ArgumentParser(prog = "my argparse example", usage = None, 
                         description = "learn how to use argparse",
                         epilog = "https://github.com/chwang12341/Learn-Python-")
# print(parser1)

##ArgumentParser(prog='my argparse example', 
##usage=None, 
##description='learn how to use argparse', 
##formatter_class=<class 'argparse.HelpFormatter'>, 
##conflict_handler='error', 
##add_help=True)


# print(parser1.print_help())
##usage: my argparse example [-h]

##learn how to use argparse

##optional arguments:
##  -h, --help  show this help message and exit
##
##https://github.com/chwang12341/Learn-Python-
##None

## Example
## import package
## from argparse import ArgumentParser

parser = ArgumentParser()
## add static parameters (type=int, str) 
parser.add_argument('runtimes', type=int, help='display an integer')
parser.add_argument('name', type=str, help='display a string')

## add Optional parameters
## dest: after parsing, the variable name
parser.add_argument('--place', type=str, help='display an integer', dest = 'position')
parser.add_argument('--food', type=str, help='display an integer')

args = parser.parse_args()
## print variable
# print (args.runtimes)
# print (args.name)

## function
def count(runtimes,name):
    for i in range(runtimes):
        print(str(name)+' run ' + str(i) +' times' )


##execute function
if __name__ == "__main__":
    ## Optional parameters
    if  args.position:
        print('Place: '+ args.position)
    if args.food:
        print('food: '+ args.food)
    
    ## static parameters
    count(args.runtimes, args.name)