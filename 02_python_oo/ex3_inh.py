'''
            Car: color seat
            |
            RacingCar: speed
'''
class Car(object):
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat

    def method1(self):
        print('it is a simple car')

    def __str__(self):
        return f'Car details:color: {self.color} and no of seats: {self.seat}'

class RacingCar(Car):
    def __init__(self, color, seat, speed):
        Car.__init__(self, color, seat)
        # super().__init__(color, seat)
        self.speed=speed
    #aka overriding
    def method1(self):
        print('it is a racing car')
        # Car.method1(self)

    def __str__(self):
        return f'Racing Car details:color: {self.color} and no of seats: {self.seat} speed is {self.speed}'

ob= RacingCar('blue',2,120)
ob.method1()
print(ob)
