def les2parties(nombre):
     
    entiere= int(nombre)  
    decimale  = str(nombre).split('.')[1]

    # Afficher les résultats
    print(f"La partie entière est : { entiere}")
    print(f"La partie décimale est : { decimale}")













nombre = float(input("Entrez un nombre : "))
les2parties(nombre)