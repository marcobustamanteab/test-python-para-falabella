import string
from flask import Flask

"""
repo: https://github.com/marcobustamanteab/test-python-para-falabella.git

-importamos String para poder usar ascii_uppercase y lo guardamos en la variable alphabet
-declaramos un diccionario vacio llamado 'patentes' e inicializamos la id en 1
-iteramos con letter la variable que contiene el alfabeto y anidamos con otra iteración para los números
-luego de condicionar el formato de texto a retornar, le asignamos ese valor a la clave id 'patentes[id]'
-sumamos += 1 a ID para que continue con la siguiente iteracion hasta llegar a la última ID
-guardamos en la variable 'find_by_key' el valor de la ID ingresada por teclado
-guardamos en result el valor obtenido a través del método .get de nuestro diccionario y condicionamos para ver si encuentra o no el valor asociado a la clave
-guardamos en 'find_by_value' el valor de la patente ingresada por teclado y condicionamos para comparar los valores de nuestro diccionario y el texto ingresado

"""


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
    print(f"La patente es: {result}")
else:
    print("No existe una patente asociada con ese ID")

find_by_value = input("Ingresa la patente: ")

if find_by_value in list(patentes.values()):
	index = list(patentes.values()).index(find_by_value)
	id = list(patentes.keys())[index]
	print(f"El ID es: {id}")
else:
	print("No se encuentran registros de la patente....")