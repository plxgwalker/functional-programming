import datetime
from functools import reduce


class Car:
    def __init__(self, price: float, name: str, year: int):
        self.price = price
        self.name = name
        self.year = datetime.date.today().year - year

    def __str__(self):
        return f"Назва: {self.name}, років: {self.year}, ціна: {self.price}"


def print_cars_info(car_list: list) -> None:
    for car in car_list:
        print(car.__str__())


def more_six(car: Car) -> float:
    if car.year > 6:
        return True
    else:
        return False


if __name__ == "__main__":
    car1 = Car(200, "Tesla model S", 2016)
    car2 = Car(300, "Lada", 1999)
    car3 = Car(150, "BMW m4", 2004)
    car4 = Car(350, "BMW m6", 2012)
    car5 = Car(310, "BMW Alpina b6", 2006)
    car6 = Car(500, "BMW x5", 2019)
    car7 = Car(210, "Mercedes GLS AMG", 2001)
    car8 = Car(175, "BMW m3", 2003)
    car9 = Car(700, "BMW 7", 2003)
    car10 = Car(110, "Lanos max pro plus", 2022)

    cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]

    print(f"Машини:")
    print_cars_info(cars)

    adult_cars = list(filter(more_six, cars))

    print("\nМашини старші за 6 років:")
    print_cars_info(adult_cars)

    prices = []
    for car in adult_cars:
        prices.append(car.price)

    print(f"\nСереднє арефметичне цін машин страших за 6 років: {reduce(lambda a, b: a + b, prices) / len(prices)}")
