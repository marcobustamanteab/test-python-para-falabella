import string

alphabet = list(string.ascii_uppercase)

patentes = {}
id = 1

for letter in alphabet:
    for number in range(1000):
        if number < 10:
    	    patente = f"{letter * 3}{'0' * 2}{number}"
        elif number < 100:
            patente = f"{letter * 3}0{number}"
        else:
            patente = f"{letter * 3}{number}"
        
        patentes[id] = patente
        id += 1

find_by_key = int(input("Ingresa el ID de la patente: "))

result = patentes.get(find_by_key)

if result:
    	print("La patente es:", result)
else:
    	print("No existe una patente asociada con ese ID")
    	
find_by_value = input("Ingresa la patente: ")
if find_by_value in list(patentes.values()):
	index = list(patentes.values()).index(find_by_value)
	id = list(patentes.keys())[index]
	print("El ID es:", id)
else:
	print("No se encuentran registros de la patente...")