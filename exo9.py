def population(cities):
 for city in cities:
    if city !="stop":
     resultat = len(city) * 1000000
     

     print(f" the city {city} has {len(city)} letters , so its population is {resultat}")
    

 






cities = []
x=True
while x :
    city = input("Enter the name of a city : ")
    if city== 'stop':   
        x=False
    cities.append(city)   


population(cities)