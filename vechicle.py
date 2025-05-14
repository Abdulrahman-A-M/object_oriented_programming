class Vechicle: 
    def __init__(self,number_of_wheel,type_of_tank,seating_capcity,maximum_velocity):
        self._number_of_wheels=number_of_wheel
        self.type_of_tank=type_of_tank
        self.seating_capcity=seating_capcity
        self.maximum_velocity=maximum_velocity

    def set_number_of_wheel(self,number=6):#setter
            self._number_of_wheels=number

    def get_number_of_wheel(self):
            return self._number_of_wheels
        
    def make_noise(self,noise ='weee'):
            print(noise)


if __name__=="__main__":
    tesla_model_s=Vechicle(4,'electric',5,250)# <---- this is name object or instance
    print(tesla_model_s._number_of_wheels)
    tesla_model_s.set_number_of_wheel()
    print(tesla_model_s.get_number_of_wheel())
    tesla_model_s.make_noise('eeeeee')







