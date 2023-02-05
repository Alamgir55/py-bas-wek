class Cat:
    def __init__(self, name):
        self.name = name
        print("Inside cat in it")

    def meow(self):
        print(f"{self.name} meow")


class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purr!!")


class Lion(Cat):
    def __init__(self, name, pride_name):
        print("Inside lion in it")
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f"{self.name} roar!!")
