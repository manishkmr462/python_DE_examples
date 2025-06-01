class Vehicle:
    name = ''
    def __init__(self, no_of_wheels = 0, power = 0, color = '', geared = False):
        self.no_of_wheels = no_of_wheels
        self.power = power
        self.color = color
        self.geared = geared

    def set_color(self, color=''):
        print("Calling set_color of Vehicle class")
        self.color = color

    @classmethod
    def set_vehicle_name(cls, name):
        cls.name = name

    @staticmethod
    def get_vehicle_name_all_caps():
        return Vehicle.name.upper()


class Bicycle(Vehicle):
    # class variables
    pedals = True
    trans_type = 'chain'
    def __init__(self, no_of_wheels=2, cross_bar=True, carriage=True, longitude=0, latitude=0, height=0):
        # instance/object variables
        super().__init__(no_of_wheels=no_of_wheels)
        self.cross_bar = cross_bar
        self.carriage = carriage
        self.longitude = longitude
        self.latitude = latitude
        self.height = height

    def move_forward(self, **kwargs):
        self.longitude += kwargs['delta_long']
        self.latitude += kwargs['delta_lat']
        if 'delta_height' in kwargs:
            print("Moving forward in different plane")
            self.height += kwargs['delta_height']
        else:
            print("Moving forward in same plane")

    def move_backward(self, delta_long, delta_lat, delta_height):
        self.longitude -= delta_long
        self.latitude -= delta_lat
        self.height -= delta_height
    
    def get_location(self):
        return (self.longitude, self.latitude, self.height)
    
    def set_color(self, color=''): # method overriding
        print("Calling set_color of Bicycle class")
        self.color = color
    
    def __add__(self, second):
        new_no_of_wheels = self.no_of_wheels + second.no_of_wheels
        return Bicycle(no_of_wheels=new_no_of_wheels)
    


b1 = Bicycle(cross_bar=False, carriage=False, longitude=100)
b2 = Bicycle(carriage=False, longitude=120)

print("properites of b1")
print(f"no_of_wheels: {b1.no_of_wheels}")
print(f"cross_bar: {b1.cross_bar}")
print("properites of b2")
print(f"no_of_wheels: {b2.no_of_wheels}")
print(f"cross_bar: {b2.cross_bar}")

b1.move_forward(delta_long = 12, delta_lat = 2, delta_height = 0)

print("properites of b1 after moving forward")
print(f"new location of bicycle is: {b1.get_location()}")

b2.no_of_wheels = 3
print(f"no_of_wheels for b2: {b2.no_of_wheels}")
print(f"no_of_wheels for b1: {b1.no_of_wheels}")

b3 = Bicycle()
print(f"no_of_wheels for b3: {b3.no_of_wheels}")

Bicycle().no_of_wheels = 3
b4 = Bicycle()
print(f"no_of_wheels for b4: {b4.no_of_wheels}")
b4.set_color("Blue")
print(f"color of b4 bicycle is {b4.color}")
b4.move_forward(delta_long = 10, delta_lat = 20, delta_height = 3)
b4.move_forward(delta_long = 10, delta_lat = 20)

b5 = b4 + b3
print(f"no_of_wheels for b5: {b5.no_of_wheels}")

Vehicle().set_vehicle_name('Vehicle 1')
print(f"new name of Vehicle is: {Vehicle().name}")

print(f"new name of the Vehicle in all caps is: {Vehicle().get_vehicle_name_all_caps()}")
