#Juego de la vida Mikebarsa 23/08/22
"""
Programa juego de la vida
Este programa simula en una interfaz gráfica (rejilla) el juego diseñado por el matemático John Conway
"""
#Bibliotecas
import pygame
import numpy as np
import time
import random
pygame.init()
"""
==============================================Funciones secundarias==============================================
"""
#Datos para la creación de la rejilla
Rejilla = ancho, largo = 800, 800
color_fondo = 30, 30, 30
filas = 40
columnas = 40
pantalla = pygame.display.set_mode(Rejilla)#Indica las proporciones de la pantalla
pantalla.fill(color_fondo)#Colorea con el color de fondo (negro)
def creac_rejilla(pantalla):
"""
(funciones, ciclos y ciclos anidados)
recibe: pantalla
Esta función crea la interfaz gráfica que será la rejilla para el juego con un color de fondo definido por un 
gris muy oscuro en la escala RGB
"""
#Esta función se encarga de crear y mostrar una rejilla en "blanco"
    for num_filas in range (0, 800, 20): 
        for contador in range (0, 800, 20):
            celula = pygame.rect.Rect(contador, num_filas, 20, 20)#Da las proporciones y posición de la célula
            pygame.draw.rect(pantalla, (120, 120, 120), celula, 1)#Rellena la célula de color negro
            pygame.display.flip()#Muestra lo anterior en pantalla
            
def creacion_estatus():
"""
(operadores, funciones, listas, listas anidadas, ciclos y ciclos anidados)
Esta función crea una matriz con células vivas/muertas al azar, asimismo, la muestra en pantalla
devuelve: status
"""
    status=[]
    for num_filas in range (40): 
        lista=[]
        for contador in range (40):
            lista.append(random.randint(0, 1))
        status.insert(num_filas,lista)
    for num_filas in range (40):
        for contador in range (40):
            if status[num_filas][contador] == 0:
                celula = pygame.rect.Rect(contador*20, num_filas*20, 20, 20)
                pygame.draw.rect(pantalla, (120, 120, 120), celula, 1)
                pygame.display.flip()
            if status[num_filas][contador] == 1:
                celula = pygame.rect.Rect(contador*20, num_filas*20, 20, 20)
                pygame.draw.rect(pantalla, (120, 120, 120), celula, 0)
    pygame.display.flip()
    return status
"""
==============================================Funciones primaria==============================================
"""
def juego(status):
"""
(operadores, funciones, listas, listas anidadas, ciclos y ciclos anidados)
recibe: status
Esta función evalúa el estado aleatorio generado anteriormente y de acuerdo a las reglas de el juego de la vida,
genera una matriz diferente y por ende muestra en pantalla una rejilla acorde a las reglas.
"""
    for i in range (1):
        creac_rejilla(pantalla)
        pygame.display.flip()
        time.sleep(2)
        #COLOREADO Y ASIGNACIÓN DE VALOR
        new_status = []
        for y in range (40):
            new_statusx=[]
            for x in range (40):
                vecinos = 0
                izq_up_y = (y-1)%40
                izq_up_x = (x-1)%40
                m_up_y = (y-1)%40
                m_up_x = x%40
                der_up_y = (y-1)%40
                der_up_x = (x+1)%40
                izq_m_y = y%40
                izq_m_x = (x-1)%40
                der_m_y = y%40
                der_m_x = (x+1)%40
                izq_d_y = (y+1)%40
                izq_d_x = (x-1)%40
                m_d_y = (y+1)%40
                m_d_x = x%40
                der_d_y = (y+1)%40
                der_d_x = (x+1)%40
                vecinos = (status[izq_up_x][izq_up_y])+\
                          (status[m_up_x][m_up_y])+\
                          (status[der_up_x][der_up_y])+\
                          (status[izq_m_x][izq_m_y])+\
                          (status[der_m_x][der_m_y])+\
                          (status[izq_d_x][izq_d_y])+\
                          (status[m_d_x][m_d_y])+\
                          (status[der_d_x][der_d_y])
                #print(x, y)
                #print((status[x][y]))
                #print(vecinos)
                if (status[y][x]) == 0:
                    if vecinos == 3:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 0)
                        new_statusx.append(1)
                    else:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 1)
                        new_statusx.append(0)
                elif (status[y][x]) == 1:
                    if vecinos==2:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 0)
                        new_statusx.append(1)
                    elif vecinos==3:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 0)
                        new_statusx.append(1)
                    else:
                        celula = pygame.rect.Rect(x*20, y*20, 20, 20)
                        pygame.draw.rect(pantalla, (120, 120, 120), celula, 1)
                        new_statusx.append(0)
                #if (new_statusx[contador])==1:
                    #print("Viva")
                #elif (new_statusx[contador])==0:
                    #print("Muerta")
            #print(new_statusx)
            new_status.append(new_statusx)
        new_status.append(new_statusx)
        status = new_status
        pygame.display.flip()
"""
==============================================Main==============================================
"""
def main():
    creac_rejilla(pantalla)
    status=creacion_estatus()
    juego(status)
main()
