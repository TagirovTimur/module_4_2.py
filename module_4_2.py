def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
##inner_function() при таком вызове, функция не срабатывает, так как находится все области видимости
test_function() # при вызове функции в области видимости, срабатывает нужная нам функция, как в неё и заложено