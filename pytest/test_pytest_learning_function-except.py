##test_pytest_learning_function-except.py


##import package
import pytest
number = 10
def number_game(x):
 if x == int(number):
   raise ValueError("BOOM! Value Wrong")
 
 else:
   # print("you pass")
   pass
 
# number_game(0) #you pass
# number_game(10) #ValueError: BOOM! Value Wrong
def test_game1():
    with pytest.raises(ValueError):
        number_game(10)
 
def test_game2():
 # assert number_game(2) == print("you pass")
     assert number_game(2) == None
