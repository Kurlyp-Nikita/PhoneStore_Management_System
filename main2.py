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


# from functools import wraps
#
# def logger(func):
#     @wraps(func) # чтобы при проверке add.__name__ было add, а не на wrapper ссылалось
#     def wrapper(*args, **kwargs):
#         print(f"Вызов функции: {func.__name__}")
#         print(f"Аргументы: {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Результат: {result}")
#         return result
#     return wrapper
#
#
#
# @logger
# def add(a, b):
#     ''' С @wraps(func) видны док стринги, без не видны, это как пример '''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
# # help(add)
#
# add(1, 2)


# # Задача: Декоратор-счётчик вызовов
# # Нужно:
# # Создать декоратор call_counter, который:
# # Считает, сколько раз была вызвана функция
# # При каждом вызове выводит:
# # Функция <имя> вызвана N раз
# # Возвращает результат функции
# # Работает с аргументами (*args, **kwargs)
# # Использует @wraps(func)
#
#
# from functools import wraps
#
#
# def call_counter(func):
#     count = 0
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         result = func(*args, **kwargs)
#         print(f"Функция {func.__name__} вызвана {count} раз")
#         return result
#     return wrapper
#
#
# @call_counter
# def greet(name):
#     return f"Привет, {name}"
#
#
# greet("Nikita")
# greet("Nikita")
# greet("Nikita")
# greet("Nikita")
#
# print(greet("Alex"))


# Задача: Декоратор-счётчик с атрибутом
# Сделать декоратор call_counter, который:
# 1 При каждом вызове функции увеличивает счётчик вызовов
# 2 Хранит количество вызовов в атрибуте функции, например: func.calls
# 3 Выводит сообщение при вызове функции: "Функция <имя> вызвана N раз"
# 4 Возвращает результат оригинальной функции
# 5 Работает с любым количеством аргументов (*args, **kwargs)
#
# Пример использования:
# @call_counter
# def greet(name):
#     return f"Привет, {name}"
#
# greet("Nikita")  # "Функция greet вызвана 1 раз"
# greet("Alex")    # "Функция greet вызвана 2 раз"
# greet("John")    # "Функция greet вызвана 3 раз"
#
# print(greet.calls)  # 3


# from functools import wraps
#
#
# def call_counter(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         result = func(*args, **kwargs)
#         print(f"Функция {func.__name__} вызвана {wrapper.calls} раз")
#         return result
#     wrapper.calls = 0
#     return wrapper
#
#
# @call_counter
# def greet(name):
#     return f"Привет, {name}"
#
#
# print(greet("Nikita"))
# print(greet("Alex"))
# print(greet("Max"))
# print(greet.calls)




