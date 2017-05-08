from Classes.Pieza import Pieza
from Classes.Tela import Tela
from operator import attrgetter
import copy
import random

piezas_l = []  # Lista con el roden de las piezas
l_piezas = []  # Lista con los objetos de las piezas
p_soluciones = []
multiples_s = []


def InicializarGrasp(li_piezas):
    global piezas_l, l_piezas
    piezas_l = [x for x in range(1, len(li_piezas) + 1)]
    l_piezas = copy.deepcopy(li_piezas)
    l_piezas.sort(key=attrgetter("id"), reverse=False)


def returnListaPiezas():
    global piezas_l
    return piezas_l


def cambiarStatusPiezas():
    global l_piezas
    for p in l_piezas:
        p.setnoasignada()


def printPiezas():
    global l_piezas
    for p in l_piezas:
        print(p.tostring())


def calcularPSoluciones():
    global piezas_l, l_piezas, p_soluciones, multiples_s
    while len(multiples_s) < 10:
        # IDs que ya han sido seleccionados para formar parte de una solución
        ids_seleccionados = []
        lista_areas = [p.getarea() for p in l_piezas]
        menor = max(lista_areas)
        mayor = max(lista_areas)
        menor_id = 0
        cce = 0
        cmin = 0
        alfa = 0.11
        while len(ids_seleccionados) < len(l_piezas):
            posibles_agregar = []
            for p in l_piezas:
                if p.getid() not in ids_seleccionados:
                    lista_areas.append(p.getarea())
            mayor = max(lista_areas)
            menor = max(lista_areas)
            for p in l_piezas:
                if p.getarea() <= menor and p.getid() not in ids_seleccionados:
                    menor_id = p.getid()
                    cmin = p.getarea()
            # print("Menor no asignado " + str(cmin))
            # ids_seleccionados.append(menor_id)
            cce = cmin + (alfa * (mayor - cmin))
            for p in l_piezas:
                if p.getarea() >= cmin and p.getarea() <= cce and p.getid() not in ids_seleccionados:
                    posibles_agregar.append(p.getid())
            if posibles_agregar == []:
                #print("no hay")
                for p in l_piezas:
                    if p.getid() not in ids_seleccionados and p.getarea() == cmin:
                        posibles_agregar.append(p.getid())
                '''
                for p in l_piezas:
                    if p.getid() not in ids_seleccionados:
                        posibles_agregar.append(p.getid())
                '''
            #print("posibles a agregar " + str(posibles_agregar))
            eleccion = random.randrange(len(posibles_agregar))
            ids_seleccionados.append(posibles_agregar[eleccion])
        ids_seleccionados.reverse()
        multiples_s.append(ids_seleccionados)
    for m in multiples_s:
        print(m)
