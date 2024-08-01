class Car:
    def __init__(self , motor,wheel=4):
        self.wheel=wheel
        self.motor = motor
        print("---------and the motor:", self.wheel,self.motor)
first_car =  Car("motor1")
second_card = Car ("motor2", 10)

print (type(first_car))
print (type(second_card))