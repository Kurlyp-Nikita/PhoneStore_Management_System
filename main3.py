# # Атрибуты класса, атрибута.
#
# class User:
#
#     work = "IT" # Атрибуты класса, этот общий для всех экземпляров
#
#     def __init__(self, name: str):
#
#         # Атрибуты экземпялара класса
#         self.name = name
#         self.age: int = 21
#
#
# user = User("Nikita")
#
#
# a = user.name
# b = user.age
# c = user.work
#
# print(a)
# print(b)
# print(c)
#


# def func(name):
#     # определяем функцию, которая будет использоваться как callback
#     return f"Hi {name}"  # callback возвращает приветствие
#
#
# def func_process(callback_func):  # функция которая принимает callback
#
#     name = input("Введите своё имя: ")  # получаем данные от пользователя
#
#     if name:  # условие работы callback
#         # здесь начинается работа callback-функции:
#         # callback срабатывает в момент вызова callback_func(name)
#         # callback не выполняется при передаче функции, только при вызове
#
#         res = callback_func(name)  # вызываем переданную функцию
#         print(res)
#     else:
#         print("Имя не введено, callback не сработал")
#
#
# func_process(func)  # вызов функции, передаём callback



fishing_list = []


def on_bite():
    fishing_name = input('Введите название пойманой рыбы: ')
    fishing_list.append(fishing_name)
    print(f'Рыба поймана! {fishing_name} добавлена в список.')
    print(f'Всего поймано рыб: {len(fishing_list)}')


def fishing_process(func_callback):
    while True:

        print('Меню состояния рыбалки:\n'
              '1. Клюёт\n'
              '2. Поклёвка\n'
              '3. Пока тихо\n'
              '4. Остановить рыбалку')

        state = input('Введите состояние рыбалки: ')

        if state == '1':
            func_callback()

        elif state == '2':
            print('жди клёва')

        elif state == '3':
            print('сиди терпи поклёвки')

        elif state == '4':
            print('Рыбаклка окончена')
            break


fishing_process(on_bite)




