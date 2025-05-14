#Write a Python class which has two methods set_String and print_String.


#set_String accept a string from the user and print_String print the string in upper case.

class ToUpperCase:
  
  def __init__(self,input_string="hello world"):
    self.input_string=input_string

  def set_String(self,inputString):
     self.input_string=inputString

  def print_String(self):
      return self.input_string.upper()


if __name__=='__main__':
   touppercase=ToUpperCase()
   print(touppercase.print_String())
   input_String = input("Please key in your string: ")
   touppercase.set_String(input_String)
   print(touppercase.print_String())






