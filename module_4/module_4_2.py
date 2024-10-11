def test_fucntion(a):
  
  def inner_function():
    print(a)
    print("Я в области видимости функции test_function")
  inner_function()

#inner_function() # not defined if not call test function
test_fucntion(1)  # inner_function is possible to call if test function is called

