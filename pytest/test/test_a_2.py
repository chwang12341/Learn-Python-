## test_a_2.py
## Import package
import pytest
@pytest.mark.run(order=5)
def test_fifth_func():
 print('Order 5 Function')
 
@pytest.mark.run(order=6)
def test_Sixth_func():
 print('Order 6 Function')
 
 
@pytest.mark.run(order=7)
def test_Seventh_func():
 print('Order 7 Function')
 
@pytest.mark.run(order=8)
def test_Eigth_func():
 print('Order 8 Function')