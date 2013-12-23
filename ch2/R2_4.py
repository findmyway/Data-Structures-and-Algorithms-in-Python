#!/usr/bin/env python3


class Flower():
    """a class descripe flower"""
    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def set_name(self, name):
        self._name = name

    def set_petals(self, petals):
        self._petals = petals

    def set_price(self, price):
        self._price = price

    def name(self, ):
        return self._name

    def petals(self, ):
        return self._petals

    def price(self, ):
        return self._price

    def descripe(self, ):
        print("""
              name: {0}
              petals: {1}
              price: {2}
              """.format(self._name, self._petals, self._price))

if __name__ == '__main__':
    print("initial a Flower with name=rose petals=9 price=10")
    a = Flower('rose', 9, 10)
    a.descripe()
    print("set name = gardenia")
    a.set_name('gardenia')
    print(a.name())
    print("set_price = 5")
    a.set_price(5)
    print(a.price())
    print("set petals = 1")
    a.set_petals(1)
    print(a.petals())
    a.descripe()
