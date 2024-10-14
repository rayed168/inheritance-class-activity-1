class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(vehicle):
    pass
school_bus=Bus("School Volvo",100,15)
print("My name is ",school_bus.name)
print("My max speed is ",school_bus.max_speed)
print("My mileage is ",school_bus.mileage)