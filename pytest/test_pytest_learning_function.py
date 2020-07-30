## test_pytest_learning_function.py

def multiply(x,y):
  return x*y
def test1():
  assert 2 == multiply(1,2)
 
def test2():
  assert 1 != multiply(1,2)