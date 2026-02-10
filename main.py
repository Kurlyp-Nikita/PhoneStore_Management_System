from collections.abc import MutableSet


class Phone:
    def __init__(self, brand: str, price: int, color: str):
        self.brand = brand
        self.price = price
        self.color = color

    def __str__(self):
        return f"Марка: {self.brand}, Цена: {self.price}$, Цвет: {self.color}"


class PhoneStore:
    def __init__(self, name: str):
        self.name = name
        self.store: PhoneSet = None

    def __str__(self):
        return f"Имя магазина: {self.name}, телефон: {self.store}"


class PhoneSet(MutableSet[Phone]):
    def __init__(self, phone_store: PhoneStore):
        phone_store.store = self
        self.elements = set()

    def add(self, phone: Phone):
        self.elements.add(phone)

    def discard(self, phone: Phone):
        self.elements.remove(phone)

    def __str__(self):
        return f"{self.elements}"

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, item):
        return item in self.elements

    def __len__(self):
        return len(self.elements)


phone_1 = Phone("Android", 1000, "red")
print(phone_1)

print("-" * 200)

phone_store_1 = PhoneStore("Samsung-Store")
print(phone_store_1)

print("-" * 200)

phone_set_1 = PhoneSet(phone_store_1)
print(phone_set_1)




