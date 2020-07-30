## test_b_1.py
## Import package
import pytest
@pytest.mark.run(order=1)
def test_first_func():
 print('Order 1 Function')
 
@pytest.mark.run(order=2)
def test_Second_func():
 print('Order 2 Function')
 
 
@pytest.mark.run(order=3)
def test_Third_func():
 print('Order 3 Function')
 
@pytest.mark.run(order=4)
def test_Forth_func():
 print('Order 4 Function')