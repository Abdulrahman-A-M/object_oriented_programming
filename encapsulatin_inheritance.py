#example of encapsulation 2
class Person:
    def __init__(self,fname,email):
        self.first_name=fname
        self._email=email

    def update_email(self,email):
        self._email=email
    
    def get_email(self):
        return self._email
    

tk = Person('tk','tk@email')
print(tk.first_name,tk.get_email())
tk.update_email('new@email')
print(tk.get_email())


#example of encapsulation 2
class Person:
    def __init__(self,fname,age):
        self.first_name=fname
        self._age=age
    
    def show_age(self):
        return self._get_age()#here function is private and cannot be reached externally
        
    def _get_age(self):
        return self._age
    

tkt = Person('tk',20)
print(tkt.show_age)


#example of inheritance
class Car:
    def __init__(self,num_of_wheels,seating_capacity,max_velocity):
        self.num_of_wheels=num_of_wheels
        self.seating_capacity=seating_capacity
        self.max_velocity = max_velocity
    
    def make_noise(self):
        print('YeeHaaa!')

class ElectricCar(Car):
    def __init__(self, num_of_wheels, seating_capacity, max_velocity,battery):
        super().__init__(num_of_wheels, seating_capacity, max_velocity)
        self.battery=battery
        self.state=''

    def sold_in_state(self,sold_state):
        self.state = sold_state


electriccar=ElectricCar(4,5,250,'10000V')
electriccar.sold_in_state('CA')
electriccar.make_noise()
print(electriccar.num_of_wheels)
print(electriccar.battery)
print(electriccar.state)


