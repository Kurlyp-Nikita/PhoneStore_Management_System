from collections.abc import MutableSet


class Phone:
    def __init__(self, barnd: str, system: str, price: int, color: str):
        self.brand = barnd
        self.system = system
        self.price = price
        self.color = color
        self.phone_store = None

    def __str__(self):
        return f"Брэнд: {self.brand}, \n" \
               f"ОС: {self.system}, \n" \
               f"Цена: {self.price}$, \n" \
               f"Цвет: {self.color}"


class PhoneStore:
    def __init__(self, name: str):
        self.name = name
        self.phone: PhoneSet = None

    def __str__(self):
        return f"Имя магазина: {self.name} \n" \
               f"Телефон: \n\n" \
               f"{self.phone} \n\n"


class PhoneSet(MutableSet[Phone]):
    def __init__(self, phone_store: PhoneStore):
        if not isinstance(phone_store, PhoneStore):
            raise TypeError("Указан не магазин телефонов!")

        if phone_store.phone != None:
            raise NotImplemented("Для указанного магазина уже существует салон!")

        phone_store.phone = self
        self.elements = set()

    def add(self, phone: Phone):
        if not isinstance(phone, Phone):
            raise TypeError("Добавляемый объект должен быть телефоном!")

        if phone.phone_store != None:
            raise ValueError(f"{phone} находится в другом магазине.")

        if not phone in self.elements:
            self.elements.add(phone)

    def discard(self, phone: Phone):
        self.elements.remove(phone)

    def __str__(self):
        return " ".join(str(i) for i in self.elements)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, item):
        return item in self.elements

    def __len__(self):
        return len(self.elements)


phone_1 = Phone("Samsung", "Android", 1000, "red")
phone_2 = Phone("Aple", "Iphone", 1200, "black")
print(phone_1)

print("-" * 200)

phone_store_1 = PhoneStore("Samsung-Store")
phone_set_1 = PhoneSet(phone_store_1)


phone_store_2 = PhoneStore("Apple-Store")
phone_set_2 = PhoneSet(phone_store_2)


phone_set_1.add(phone_1)
print(phone_store_1)


phone_set_2.add(phone_2)
print(phone_store_2)



