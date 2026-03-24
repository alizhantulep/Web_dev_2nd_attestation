class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        return f"{self.brand} {self.model} is starting."

    def stop(self):
        return f"{self.brand} {self.model} is stopping."

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors, electric=False):
        super().__init__(brand, model, year)
        self.doors = doors
        self.electric = electric

    def start(self):
        if self.electric:
            return f"{self.brand} {self.model} silently powers up!"
        else:
            return super().start()

    def honk(self):
        return f"{self.brand} {self.model} goes beep beep!"

    def __str__(self):
        type_car = "Electric" if self.electric else "Gas"
        return f"{super().__str__()} - {type_car} Car with {self.doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, cc):
        super().__init__(brand, model, year)
        self.cc = cc

    def start(self):
        return f"{self.brand} {self.model} roars to life!"

    def wheelie(self):
        return f"{self.brand} {self.model} does a wheelie!"

    def __str__(self):
        return f"{super().__str__()} - {self.cc}cc Motorcycle"