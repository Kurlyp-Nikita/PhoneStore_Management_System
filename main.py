from collections.abc import MutableSet


class Phone:
    def __init__(self, barnd: str, name: str, price: int, color: str):
        self.brand = barnd
        self.name = name
        self.price = price
        self.color = color
        self.phone_store = None

    def __str__(self):
        return f"Брэнд: {self.brand}, \n" \
               f"Марка: {self.name}, \n" \
               f"Цена: {self.price}$, \n" \
               f"Цвет: {self.color}"


class PhoneStore:
    def __init__(self, name: str):
        self.name = name
        self.phone: PhoneSet = None

    def __str__(self):
        return f"Имя магазина: {self.name} \n" \
               f"Телефоны: \n\n" \
               f"{self.phone} \n\n"


class PhoneSet(MutableSet[Phone]):
    def __init__(self, phone_store: PhoneStore):
        phone_store.phone = self
        self.elements = set()

    def add(self, phone: Phone):
        self.elements.add(phone)

    def discard(self, phone: Phone):
        self.elements.remove(phone)

    def __str__(self):
        return "\n\n".join(str(i) for i in self.elements)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, item):
        return item in self.elements

    def __len__(self):
        return len(self.elements)


phone_samsung_1 = Phone("Samsung", "Samsung A55", 1500, "red")
phone_samsung_2 = Phone("Samsung", "Samsung A52", 1200, "green")
phone_samsung_3 = Phone("Samsung", "Samsung A50", 1000, "black")

phone_apple_1 = Phone("Apple", "Iphone 5", 1200, "black")
phone_apple_2 = Phone("Apple", "Iphone 6", 1500, "gold")
phone_apple_3 = Phone("Apple", "Iphone 10", 2000, "yellow")


phone_store_1 = PhoneStore("Samsung-Store")
phone_store_2 = PhoneStore("Apple-Store")

phone_set_1 = PhoneSet(phone_store_1)
phone_set_1.add(phone_samsung_1)
phone_set_1.add(phone_samsung_2)
phone_set_1.add(phone_samsung_3)
phone_set_1.discard(phone_samsung_3)
print(phone_store_1)
print(len(phone_set_1))
print("-" * 200)


phone_set_2 = PhoneSet(phone_store_2)
phone_set_2.add(phone_apple_1)
phone_set_2.add(phone_apple_2)
phone_set_2.add(phone_apple_3)
phone_set_2.discard(phone_apple_3)


print(phone_store_2)
print(len(phone_set_2))

# it = iter(phone_set_2)
# print(next(it))
# print(next(it))

