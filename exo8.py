def fizzBuzz(number):
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    
    elif number % 3 == 0:
        print("Fizz")
    
    elif number % 5 == 0:
        print("Buzz")
     
   
n = int(input("Number: "))

 
fizzBuzz(n)
