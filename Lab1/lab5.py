class Person:
    def __init__(self, full_name, driving_experience):
        self.full_name = full_name
        self.driving_experience = driving_experience

class Driver(Person):
    def __init__(self, full_name, driving_experience):
        super().__init__(full_name, driving_experience)

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def __str__(self):
        return f"Car: {self.brand}, Class: {self.car_class}, Weight: {self.weight}, Driver: {self.driver.full_name}, Engine: {self.engine.power}HP {self.engine.manufacturer}"

class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, payload_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.payload_capacity = payload_capacity

class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

# Пример использования:
driver1 = Driver("Иван Иванов", 5)
engine1 = Engine(200, "ManufacturerA")
car1 = Car("Toyota", "Sedan", 1500, driver1, engine1)
car1.start()
car1.turn_left()
print(car1)

lorry1 = Lorry("Volvo", "Truck", 8000, driver1, engine1, 5000)
lorry1.stop()
print(lorry1)

sportcar1 = SportCar("Ferrari", "Coupe", 1200, driver1, engine1, 300)
sportcar1.turn_right()
print(sportcar1)