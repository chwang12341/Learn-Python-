## test_fixture_learning.py
## 基本用法 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

## test_fixture_learning.py
##import package
# import pytest
# @pytest.fixture
# def sea_animal():
#     return"Turtles"
# @pytest.fixture
# def farm_animal():
#     return "dogs"
# def forest_animal():
#     return "Monkey"
# def test_turtle_in_sea(sea_animal):
#     assert "Turtles" == sea_animal ## fixture 用法
#     assert "Monkey" == forest_animal() ## 沒有ficture的用法
 
# def test_c_in_sea(sea_animal):
#     assert "t" in sea_animal ## fixture 用法
#     assert "M" in forest_animal() ## 沒有ficture的用法
# def test_two_func_in_one(sea_animal,farm_animal):
#     assert "s" in sea_animal and farm_animal
#     assert "Turtles" == sea_animal 
#     assert "dogs" == farm_animal



## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Scope 用法 與 class 無法代入參數的解決方法 - - - - - - - - - - - - - - - - - - - - - - -
## test_fixture_learning.py
import pytest
@pytest.fixture(scope="function")
def scope_func():
    pass
@pytest.fixture(scope="class")
def scope_class():
    pass
@pytest.fixture(scope="module")
def scope_module():
    pass
@pytest.fixture(scope= "session")
def scope_session():
    pass
## function method
def test_scope1(scope_func, scope_class, scope_module, scope_session):
    assert scope_func == None
    assert scope_class == None
def tes_scope2(scope_class, scope_module, scope_session):
    pass


## class method 
@pytest.mark.usefixtures()
class TestClassMethod:
    def test_scope3(self, scope_func, scope_class, scope_module, scope_session):
        assert scope_func== None
    def test_scope4(self, scope_class, scope_module):
        pass
    
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Fixture decorator - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# import pytest
# @pytest.fixture
# def decorator_implement():
# print('\nHappend before each test start')
# def sea_animal():
# return"Turtles"
# @pytest.fixture
# def farm_animal():
# return "dogs"
# ## function 
# @pytest.mark.usefixtures("decorator_implement")
# def test1():
# print("test 1")
# assert "Turtles" == sea_animal()

# @pytest.mark.usefixtures("decorator_implement")
# def test2(farm_animal):
# print("test 2")
# assert "dogs" == farm_animal
# ## class: inside
# class Test_Decorator:
# @pytest.mark.usefixtures("decorator_implement")
# def test3(self):
# print("test 3")
# assert "Turtles" == sea_animal()

# @pytest.mark.usefixtures("decorator_implement")
# def test4(self, farm_animal):
# print("test 4")
# assert "dogs" == farm_animal
# ## class: outside
# @pytest.mark.usefixtures("decorator_implement")
# class Test_Decorator1:

# def test5(self):
# print("test 5")
# assert "Turtles" == sea_animal()

# def test6(self, farm_animal):
# print("test 6")
# assert "dogs" == farm_animal
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Autos 用法 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## test_fixture_learning.py
# import time
# import pytest
# @pytest.fixture(scope="session", autouse=True)
# def session_range():
# print("\n")
# print("Session Range")
# # print(request.module.__name__)
# # print(time.asctime())

# @pytest.fixture(scope="class", autouse=True)
# def class_range():
# print("\n")
# print("Class Range")
# # print(request.function.__name__)
# # print(time.asctime())
# @pytest.fixture(scope="function", autouse=True)
# def function_range():
# print("\n")
# print("Function Range")
# # print(request.function.__name__)
# # print(time.asctime())
# def test1():
# print("Test 1")


# def test2():
# print("Test 2")


# class TestClass:
# def test3(self):
# print("Test 3")
# def test4(self):
# print("Test 4")
# def test5(self):
# print("Test 5")
# def test6(self):
# print("Test 6")
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# ## Fixture 回傳Value: params 用法 - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# ## test_fixture_learning.py
# import pytest
# @pytest.fixture(params=[2,58,6,"Hi"])
# def test_create_params(request):
#  return request.param
# def test_params(test_create_params):
#  print(test_create_params)
#  assert test_create_params != 8
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -