import typing
import time
from typing import Union


class Car:
    def __init__(self, model: str, horsepowers: int):
        self.model = model
        self.horsepowers = horsepowers

    def __str__(self):
        return f"Model: {self.model}, Horsepowers: {self.horsepowers}"


cars_parameters: list[str, int] = [{"model": "nissan", "horsepowers": 120}, {"model": "honda", "horsepowers": 150}]


def car_creation(parameters: list[dict[str, Union[int, str]]]) -> list[Car]:
    car_obj = []
    for item in parameters:
        model = item['model']
        horsepowers = item['horsepowers']
        car_obj.append(Car(model, horsepowers))
    return car_obj


car_1, car_2 = car_creation(cars_parameters)
print(car_1, car_2)
