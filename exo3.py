def DiscountCalculation(a ,b,c):
     
     



     if c in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
          
          a=90*a/100
     else :

          a=80*a/100
     if  b>5:  
          a=95*a/100  

     return a
     

          










Total = float(input("Total amount: "))
items= int(input("Number of items: "))
day = input ("Day of the week:")
x=DiscountCalculation(Total,items,day)
print(f"Total price after discount:{x}dinars")
