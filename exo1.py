def CalculatingTaxiRides(a,b):
    taxis =a // b

    verif =a % b
    if verif > 0 :
        taxis += 1



    return  taxis




people = int(input("How many people need a ride? "))

capacity = int(input("How many people fit in one taxi? "))
result =CalculatingTaxiRides(people, capacity)

print(f"Number of taxis needed: {result}")






