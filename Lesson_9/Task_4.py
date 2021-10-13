from random import choice


class Car:
    """ Main cer"""
    direction = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a police car? {p}')

    def go(self):
        print(f'{self.name}: Car went.')

    def stop(self):
        print(f'{self.name}: Car stopped!')

    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'


class TownCar(Car):
    """ City car"""

    def show_speed(self):
        return f'{sels.name}: Car.speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    """ Cargo truck"""

    def show_speed(self):
        return f'{sels.name}: Car.speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """ SportsCar"""


class PoliceCar(Car):
    """Patrol car"""

    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p)


police_car = PoliceCar('"Полицайка', 'белый', 80)
work_car = WorkCar('"Грузовичок"', 'хаки', 40)
sport_car = SportCar('"Спортивка"', 'красный', 120)
town_car = TownCar('"Малютка"', 'желтый', 65)

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()