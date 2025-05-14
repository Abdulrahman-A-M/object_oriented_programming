import random

class GuessNumber:
    def __init__(self,given_range=100):
        self.result = random.randint(1,given_range)

    def guess(self,input_guess=0):
        if input_guess == self.result:
            return "Correct"
        elif input_guess > self.result:
            return "Too big"
        else:
            return "Too small"
        

if __name__=='__main__':
    
     while True:
        try:
            given_range=int(input('Please enter a number larger then 0 (for exmaple 100), and computer will make a random number: '))
            if given_range <= 0:
                print('please enter number larger then 0.')
                continue
            break
          
        except:
            print('Please key a vaild number')
     guessnumber =GuessNumber(given_range)

     answer=guessnumber.guess()
     m = int(input("Please key in no more than how many times (smartness) you believe you can make it: "))
     n =0

     while answer !='Correct':
         n +=1
         input_number=int(input("please put your guess < %d: " %given_range))
         answer=guessnumber.guess(input_number)
         print(answer)

     if n <= m:
         print('Good job you are a smart.')
     else:
          print('Good, you need to play more.')
