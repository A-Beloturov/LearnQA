import typing

class Car:
    def __init__(self, model, horsepowers):
        self.model = model
        self.horsepowers = horsepowers

    def GetSTR(self):
        return "Model: " + self.model + " Horsepowers: " + str(self.horsepowers)



cars_parametrs = [{"model": "nissan", "horsepowers": 120}]
def car_creation(parametrs):
    for item in parametrs:
        model = item['model']
        horsepowers = item['horsepowers']
    return Car(model, horsepowers)

#car_2 = Car("honda", 200)
param1 = car_creation(cars_parametrs)
print(param1)


print(car_1.GetSTR())
#print(car_2.GetSTR())

