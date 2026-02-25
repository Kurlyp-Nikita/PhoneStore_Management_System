class Mediator:
    def __init__(self, model):
        self.model = model

    def get(self, pk: int):
        return self.model.pizzas[pk]

    def all(self):
        list_pizza = [pizza for pizza in self.model.pizzas]
        return list_pizza

    def filter(self, **kwargs):
        result = []

        for pizza in self.model.pizzas:
            match = True
            for key, value in kwargs.items():
                if pizza[key] != value:
                    match = False
                    break

            if match:
                result.append(pizza)

        return result

    def count(self):
        return len(self.model.pizzas)

    def first(self):
        return self.model.pizzas[0]

    def last(self):
        return self.model.pizzas[-1]


class Pizza:
    pizzas = [
        {'id': 0, 'name': 'Пеперони', 'price': 500, 'vegetarian': False},
        {'id': 1, 'name': '4 Сыра', 'price': 550, 'vegetarian': True},
        {'id': 2, 'name': 'С ананасом', 'price': 450, 'vegetarian': False},
        {'id': 3, 'name': 'Маргарита', 'price': 400, 'vegetarian': True},
    ]


class MyModel:
    objects = Mediator(Pizza)


obj_1 = MyModel.objects.get(0)
obj_2 = MyModel.objects.all()
obj_3 = MyModel.objects.filter(vegetarian=False)
obj_4 = MyModel.objects.count()
obj_5 = MyModel.objects.first()
obj_6 = MyModel.objects.last()

print(obj_1)
print(obj_2)
print(obj_3)
print(obj_4)
print(obj_5)
print(obj_6)



