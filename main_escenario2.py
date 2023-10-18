import streamlit as st
import estandarizador_escenario2
import time
inicio = time.time()

direccion = input("Por favor, ingresa direccion: ")

lista_direcciones = [direccion]

def get_diccionario(diccionario: dict):
    dictionary_depurado: dict = {}
    if diccionario is not None:
        for i in diccionario.keys():
            if diccionario[i] != "":
                dictionary_depurado[i] = diccionario[i]
        return dictionary_depurado
    else:
        return dictionary_depurado


#lista_direcciones = ["EDIFICIO GIRASOLES TORRE AZUL APARTAMENTO 6A PISO UNO"]

for i in lista_direcciones:
    componentes = estandarizador_escenario2.estandarizar_direccion(i)
    print(i)
    print(get_diccionario(componentes))
    print("-------------------------------------------")

fin = time.time()
print(fin-inicio)
