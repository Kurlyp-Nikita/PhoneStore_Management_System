# lst = [1, 2, 3, 4, 5, 6, 56, 10]  # сам параметр-аргумент, который будет передан функции
#
#
# def func(spisok):
#     count = 0
#     new_list = []
#     for i in spisok:
#         if i % 2 == 0:
#             count += 1
#             new_list.append(i)
#     return f"чётные числа: {new_list},\n" \
#            f"колличество четных чискл: {count}"
#
#
#
# result = func(lst)
# print(result)


# def parameters_dec(x):  # прописываем декоратор с параметром
#     def my_decorator(func):  # прописываем декоратор
#         def wrapper():
#             print("Что-то происходит перед вызовом функции")
#             y = x + 1
#             print(f'Используем параметр {y}')
#             func()  # сюда будут вставляться функции к которым мы будем использовать декоратор
#             print("Что-то происходит после вызова функции")
#
#         return wrapper
#
#     return my_decorator
#
#
# @parameters_dec(74)# теперь прописываем декоратор с параметром
# def say_hello():
#     print("Функция к которй применили декоратор с параметром")
#
#
# # say_hello = parameters_dec(74)(say_hello)
# say_hello()


# def parametr_decorators(param_func):
#     def mydecorator(func):
#         def wrapper(*args, **kwargs):
#             print("декоратор начал работу с парметром функции")
#             param_func()
#             print("функция отработана")
#             result = func(*args, **kwargs)
#             print("отработа сама функция в декораторе")
#             return result
#         return wrapper
#     return mydecorator
#
#
# def hi_func():
#     print("Привет я папрметрическая функция декротатора")
#
#
# @parametr_decorators(hi_func)
# def result(name, age):
#     print(f"Я {name} результат выполнения всего декоратора, мне {age} лет")
#
#
# result("Nikita", 21)


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("До функции")  # что делаем до вызова функции
#         result = func(*args, **kwargs)  # вызываем функцию с её аргументами
#         print("После функции")  # что делаем после
#         return result
#     return wrapper
#
#
# @decorator
# def say_hello(name, age):
#     print(f"Привет, {name}! Тебе {age} лет.")
#
#
# say_hello("Алекс", 25)



# Нужно: Создать декоратор logger, который:

# Выводит:
# имя функции
# переданные аргументы
# Вызывает функцию
# Выводит результат функции
# Возвращает результат


from functools import wraps

def logger(func):
    @wraps(func) # чтобы при проверке add.__name__ было add, а не на wrapper ссылалось
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper



@logger
def add(a, b):
    ''' С @wraps(func) видны док стринги, без не видны, это как пример '''
    return a + b


print(add.__name__)
print(add.__doc__)
# help(add)

add(1, 2)

