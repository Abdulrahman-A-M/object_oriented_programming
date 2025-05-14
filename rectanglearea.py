class RectangleArea:
    def __init__(self):
        self.length=0
        self.width=0


    def set_parameters(self,input_length,input_width):
        self.length= float(input_length)
        self.width = float(input_width)

    #def get_area(self):
        return self.length * self.width
    
if __name__ == "__main__":
        rectangle = RectangleArea()

        input_length = input('Please key in the length: ')
        input_width = input('Please key in the width: ')

        
        print(rectangle.set_parameters(input_length,input_width))






