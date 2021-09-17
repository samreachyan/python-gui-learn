class Parrot:
    """This is Parrot class for fly and swim attribute"""

    def __init__(self, name):
        self.__name = name

    def fly(self):
        print("{} can fly".format(self.__name))

    def swim(self):
        print("{} cannot swim".format(self.__name))


class Penguin:
    def __init__(self, name):
        self.__name = name

    def fly(self):
        print("{} cannot fly".format(self.__name))

    def swim(self):
        print("{} can swim".format(self.__name))


# common interface calling method
def flying_bird(bird):
    bird.fly()


# instantiat objects
blu = Parrot("Blu")
peggy = Penguin("Peggy")

# passing objects
flying_bird(blu)
flying_bird(peggy)

print(blu.__doc__)
