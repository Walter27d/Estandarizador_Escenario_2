import re
from itertools import product
import diccionarios_escenario2

diccionario_B = diccionarios_escenario2.get_b()
diccionario_U = diccionarios_escenario2.get_u()
diccionario_M = diccionarios_escenario2.get_m()
diccionario_L = diccionarios_escenario2.get_l()
diccionario_R = diccionarios_escenario2.get_r()
diccionario_F = diccionarios_escenario2.get_f()
diccionario_C = diccionarios_escenario2.get_c()
diccionario_T = diccionarios_escenario2.get_t()


def verificar_patron_escenario2(cadena, patron):
    busqueda = re.search(patron, cadena)
    if busqueda:
        return busqueda.groups()
    else:
        return None


def extraer_componentes_direccion_escenario2(cadena):
    componentes_direccion_escenario2 = {
        "Barrio": "",
        "Urbanizacion": "",
        "NombreUrbanizacion": "",
        "TipoPiso": "",
        "NumeroPiso": "",
        "Manzana": "",
        "TipoPredio": "",
        "Casa": "",
        "LoteParcela": "",
        "Sector": "",
        "Kilometro": "",
        "IdentificadorPredio": "",
        "UnhandledPattern": "",
        "UnhandledData": "",
        "InputPattern": "",
        "UserOverrideFlag": "",
        "LineaPatron": "",
        "DireccionEjemplo": ""
    }

    for M in diccionario_M.keys():
        patron_1 = r'^({})\s+(\d{{1,3}})\s+$'.format(re.escape(M))
        componentes_1 = verificar_patron_escenario2(cadena, patron_1)
        if componentes_1 is not None:
            componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_1[0])
            componentes_direccion_escenario2["InputPattern"] = 'M|^|+|^|'
            componentes_direccion_escenario2["LineaPatron"] = '5189'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA 27 '
            return componentes_direccion_escenario2

        patron_3 = r'^({})\s+([A-Z]+)\s+(\d+)$'.format(re.escape(M))
        componentes_3 = verificar_patron_escenario2(cadena, patron_3)
        if componentes_3 is not None:
            componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_3[0]), componentes_3[1], componentes_3[2]
            componentes_direccion_escenario2["InputPattern"] = 'M|+|^'
            componentes_direccion_escenario2["LineaPatron"] = '498'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'MANZANA GUTIERREZ 27'
            return componentes_direccion_escenario2

        patron_11 = r'^({})\s+(\d+)\s+([A-Z]+)\s+(\d+)\s+$'.format(re.escape(M))
        componentes_11 = verificar_patron_escenario2(cadena, patron_11)
        if componentes_11 is not None:
            componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_11[0]), componentes_11[1]
            componentes_direccion_escenario2["UnhandledData"] = componentes_11[2], componentes_11[3]
            componentes_direccion_escenario2["InputPattern"] = 'M|^|+|^|'
            componentes_direccion_escenario2["LineaPatron"] = '226'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'MZ 27 ARBOL 2 '
            return componentes_direccion_escenario2

    for L, B in product(diccionario_L.keys(), diccionario_B.keys()):
        patron_5 = r'^({})\s+({})$'.format(re.escape(L), re.escape(B))
        componentes_5 = verificar_patron_escenario2(cadena, patron_5)
        if componentes_5 is not None:
            componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_5[0]), diccionario_B.get(componentes_5[1])
            componentes_direccion_escenario2["InputPattern"] = 'L|B'
            componentes_direccion_escenario2["LineaPatron"] = '1241'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'CENTROCOMERCIAL CIUDADELA'
            return componentes_direccion_escenario2
 
    for F, M, M2 in product(diccionario_F.keys(), diccionario_M.keys(), diccionario_M.keys()):
        patron_6 = r'^({})\s+(\d+)\s+({})\s+({})\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(F), re.escape(M), re.escape(M2))
        componentes_6 = verificar_patron_escenario2(cadena, patron_6)
        if componentes_6 is not None:
            componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_6[0]), componentes_6[1]
            componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_6[2]), diccionario_M.get(componentes_6[3]), componentes_6[4], componentes_6[5]
            componentes_direccion_escenario2["InputPattern"] = 'F|^|M|M|+|+'
            componentes_direccion_escenario2["LineaPatron"] = '1334'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 17 MANZANA EDIFICIO JARDIN PLAZA'
            return componentes_direccion_escenario2
 
    for F, B, B2 in product(diccionario_F.keys(), diccionario_B.keys(), diccionario_B.keys()):
        patron_7 = r'^({})\s+(\d+)\s+({})\s+({})\s+([A-Z]+)$'.format(re.escape(F), re.escape(B), re.escape(B2))
        componentes_7 = verificar_patron_escenario2(cadena, patron_7)
        if componentes_7 is not None:
            componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_7[0]), componentes_7[1]
            componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_7[2]), diccionario_M.get(componentes_7[3]), componentes_7[4]
            componentes_direccion_escenario2["InputPattern"] = 'F|^|B|B|+'
            componentes_direccion_escenario2["LineaPatron"] = '1334'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 19 BARRIO SUPERMANZANA A'
            return componentes_direccion_escenario2
 
    for F, B in product(diccionario_F.keys(), diccionario_B.keys()):
        patron_8 = r'^({})\s+(\d+)\s+({})\s+([A-Z]+)\s+([A-Z]+)$'.format(re.escape(F), re.escape(B))
        componentes_8 = verificar_patron_escenario2(cadena, patron_8)
        if componentes_8 is not None:
            componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_8[0]), componentes_8[1]
            componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_8[2]), componentes_8[3], componentes_8[4]
            componentes_direccion_escenario2["InputPattern"] = 'F|^|B|+|+'
            componentes_direccion_escenario2["LineaPatron"] = '1406'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'PLANTA 2 SUPERMANZANA PLAZA NORTE'
            return componentes_direccion_escenario2
 
        patron_9 = r'^({})\s+(\d+)\s+({})\s+([A-Z]+)$'.format(re.escape(F), re.escape(B))
        componentes_9 = verificar_patron_escenario2(cadena, patron_9)
        if componentes_9 is not None:
            componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_9[0]), componentes_9[1]
            componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_9[2]), componentes_9[3]
            componentes_direccion_escenario2["InputPattern"] = 'F|^|B|+'
            componentes_direccion_escenario2["LineaPatron"] = '1424'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'TZ 10 BARRIO TOBERIN'
            return componentes_direccion_escenario2
 
        patron_10 = r'^({})\s+(\d+)\s+({})$'.format(re.escape(F), re.escape(B))
        componentes_10 = verificar_patron_escenario2(cadena, patron_10)
        if componentes_10 is not None:
            componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_10[0]), componentes_10[1], diccionario_B.get(componentes_10[2])
            componentes_direccion_escenario2["InputPattern"] = 'F|^|B'
            componentes_direccion_escenario2["LineaPatron"] = '1439'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 201 CIUDADELA'
            return componentes_direccion_escenario2

#    for M, M2, L, C in product(diccionario_M.keys(), diccionario_M.keys(), diccionario_L.keys(), diccionario_C.keys()):
#        patron_2 = r'^({})\s+([A-Z]+)\s+({})\s+([A-Z]+)\s+({})\s+(\d+)([A-Z]+)\s+({})\s+([A-Z]+)$'.format(re.escape(M), re.escape(M2), re.escape(L), re.escape(C))
#        componentes_2 = verificar_patron_escenario2(cadena, patron_2)
#        if componentes_2 is not None:
#            componentes_direccion_escenario2["Manzana"] = diccionario_M.get(componentes_2[0]), componentes_2[1], diccionario_M.get(componentes_2[2]), componentes_2[3]
#            componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_2[4]), componentes_2[5], componentes_2[6]
#            componentes_direccion_escenario2["TipoPiso"] = diccionario_C.get(componentes_2[7]), componentes_2[8]
#            componentes_direccion_escenario2["InputPattern"] = 'M|+|M|+|L|>|C|+'
#            componentes_direccion_escenario2["LineaPatron"] = '592'
#            componentes_direccion_escenario2["DireccionEjemplo"] = 'EDIFICIO GIRASOLES TORRE AZUL APARTAMENTO 6A PISO UNO'
#            return componentes_direccion_escenario2
# 
#    for L, U, L2 in product(diccionario_L.keys(), diccionario_U.keys(), diccionario_L.keys()):
#        patron_4 = r'^({})\s+(\d+)\s+({})\s+({})\s+(\d+)$'.format(re.escape(L), re.escape(U), re.escape(L2))
#        componentes_4 = verificar_patron_escenario2(cadena, patron_4)
#        if componentes_4 is not None:
#            componentes_direccion_escenario2["TipoPredio"] = diccionario_L.get(componentes_4[0]), componentes_4[1]
#            componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_4[2]), diccionario_L.get(componentes_4[3]), componentes_4[4]
#            componentes_direccion_escenario2["InputPattern"] = 'L|^|U|L|^'
#            componentes_direccion_escenario2["LineaPatron"] = '1032'
#            componentes_direccion_escenario2["DireccionEjemplo"] = 'APARTAMENTO 10 URBANIZACION PORTERIA 2'
#            return componentes_direccion_escenario2
#
#    for F, M, B, M2, B2 in product(diccionario_F.keys(), diccionario_M.keys(), diccionario_B.keys(), diccionario_M.keys(), diccionario_B.keys()):
#        patron_12 = r'^({})\s+(\d+)\s+({})\s+({})\s+({})\s+([A-Z]+)\s+({})$'.format(re.escape(F), re.escape(M), re.escape(B), re.escape(M2), re.escape(B2))
#        componentes_12 = verificar_patron_escenario2(cadena, patron_12)
#        if componentes_12 is not None:
#            componentes_direccion_escenario2["TipoPredio"] = diccionario_F.get(componentes_12[0]), componentes_12[1]
#            componentes_direccion_escenario2["Barrio"] = diccionario_B.get(componentes_12[3]), diccionario_M.get(componentes_12[4]), componentes_12[5], diccionario_B.get(componentes_12[6])
#            componentes_direccion_escenario2["UnhandledData"] = componentes_12[2]
#            componentes_direccion_escenario2["InputPattern"] = 'L|^|U|L|^'
#            componentes_direccion_escenario2["LineaPatron"] = '1391'
#            componentes_direccion_escenario2["DireccionEjemplo"] = 'OFICINA 8 EDIFICIO CIUDADELA MODULO NEGRO CD'
#            return componentes_direccion_escenario2

    for U in diccionario_U.keys():
        patron_13 = r'^({})\s+(\d+)\s+([A-Z]+)$'.format(re.escape(U))
        componentes_13 = verificar_patron_escenario2(cadena, patron_13)
        if componentes_13 is not None:
            componentes_direccion_escenario2["Urbanizacion"] = diccionario_U.get(componentes_13[0]), componentes_13[1], componentes_13[2]
            componentes_direccion_escenario2["InputPattern"] = 'U|^|+'
            componentes_direccion_escenario2["LineaPatron"] = '1669'
            componentes_direccion_escenario2["DireccionEjemplo"] = 'URBANIZACION 27 ARBOLEDAS'
            return componentes_direccion_escenario2

    return None
