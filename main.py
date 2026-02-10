from collections.abc import MutableSet


class Phone:
    def __init__(self, brand: str, price: int, color: str):
        self.brand = brand
        self.price = price
        self.color = color


class PhoneStore:
    def __init__(self, name: str):
        self.name = name
        self.store: PhoneSet = None


class PhoneSet(MutableSet[Phone]):
    def __init__(self, phone_store: PhoneStore):
        phone_store.store = self
        self.elements = set()

    def add(self, phone: Phone):
        self.elements.add(phone)

    def discard(self, phone: Phone):
        self.elements.remove(phone)

