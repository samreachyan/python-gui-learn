class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}.".format(self.name, song)

    def dance(self):
        return "{} is dancing.".format(self.name)


class Penguin(Parrot):
    __type_bird = "Penguin"

    def __init__(self, name, age):
        super().__init__(name, age)
        print("Penguin class is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

    def fly(self):
        print("{} cannot fly.".format(self.__type_bird))


# instantiate the object
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the object's attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old.".format(blu.name, blu.age))

print(blu.sing("'Happy Birthday'"))
print(woo.dance())

penguin = Penguin("Linux", 30)
penguin.run()
penguin.fly()
print(penguin.dance())
