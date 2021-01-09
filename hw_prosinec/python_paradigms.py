class Animal:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self._purr_sound = "purr"

    def purr(self):
        return self._purr_sound

new_cat = Cat("Číča")
print(new_cat.get_name())
print(new_cat.purr())

