import typing


class Car:
    def __init__(self, model, horsepowers):
        self.model: str = model
        self.horsepowers: int = horsepowers

    def __str__(self):
        return f"Model: {self.model}, Horsepowers: {self.horsepowers}"


cars_parameters: list = [{"model": "nissan", "horsepowers": 120}, {"model": "honda", "horsepowers": 150}]


def car_creation(parameters: list) -> list:
    car_obj: list = []
    for item in parameters:
        model = item['model']
        horsepowers = item['horsepowers']
        car_obj.append(Car(model, horsepowers))
    return car_obj


car_1, car_2 = car_creation(cars_parameters)
print(car_1, car_2)
