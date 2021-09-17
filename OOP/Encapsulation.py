class Computer:
    """This is computer"""

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

    def __str__(self) -> str:
        print("price is {}".format(self.__maxprice))


c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
del c.__maxprice
c.sell()
c.__str__()
