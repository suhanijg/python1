class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

    def start_engine(self):
        print("Engine started.")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2018)

car1.display_info()  # Output: Toyota Camry (2020)
car2.display_info()  # Output: Honda Civic (2018)

car1.start_engine()  # Output: Engine started.


