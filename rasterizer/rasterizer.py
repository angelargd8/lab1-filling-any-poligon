
#librerias:
import re
import pygame
from pygame.locals import *
from gl import Render

width = 960
height = 540
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
rend = Render(screen)
rend.glColor(1, 0, 0.5) #lineas
#rend.glClearColor(0.5, 1, 1) #fondo

poligono1 = [ (165, 380), (185, 360) , (180, 330),
            (207, 345) ,  (233, 330),  (230, 360) ,
            (250, 380),  (220, 385) , (205, 410), (193, 383)]
poligono2 = [(321, 335), (288, 286), (339, 251) ,(374, 302)]
poligono3 =[(377, 249), (411, 197), (436, 249)]
poligono4= [
    (413, 177), (448, 159), (502, 88),
    (553, 53) ,(535, 36) ,(676, 37) ,
    (660, 52) ,(750, 145) ,(761, 179),
    (672, 192), (659, 214) ,(615, 214),
    (632, 230), (580, 230) ,(597, 215) ,
    (552, 214), (517, 144) ,(466, 180)]
poligono5=[(682, 175), (708, 120), (735, 148), (739, 170)]

"""
- ordenar los puntos de los poligonos
- encontrar las lineas de escaneo
- rellenar las lineasde escaneo
- casos especiales
"""

def drawPoligono(listaPuntos):
    for i in range(len(listaPuntos)):
        puntoActual = listaPuntos[i]
        puntoSiguiente =listaPuntos[(i+1) %len(listaPuntos)]
        rend.glLine(puntoActual, puntoSiguiente)
        xInicio, yInicio= puntoActual ##xFinal, yFinal = puntoSiguiente
        rend.glPoint(xInicio, yInicio)     
        lineasDeEscaneo = lineaDeEscaneo(puntoActual, puntoSiguiente)        

#encontrar las lineas de escaneo (scanlines)
def lineaDeEscaneo(puntoActual, puntoSiguiente):
    lineaDeEscaneo = set()
    #coordnadas minimas y maximas
    yMin = min(puntoActual[1], puntoSiguiente[1])
    yMax= max(puntoActual[1], puntoSiguiente[1])
    
    #agregar las lineas de escaneo ntre las coordenadas minimas y maximas
    for y in range(yMin, yMax +1):
        lineaDeEscaneo.add(y)    
    return sorted(lineaDeEscaneo)


isRunning = True
while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_SPACE or event.key == pygame.K_s:
                rend.glGenerateFrameBuffer("output.bmp")
                
    rend.glClear()

    #for i in range(100):
    #    rend.glPoint(480 + i,270 + i)

    for x in range(0, width, 10):
        rend.glLine((0,0), (x, height))
        rend.glLine((0, height - 1), (x, 0))
        rend.glLine((width - 1, 0), (x, height))
        rend.glLine((width - 1, height - 1), (x, 0))

    rend.glClear()
    
    poligonos= [poligono1, poligono2, poligono3, poligono4, poligono5]
    for poligono in poligonos:
        #ordenar los puntos de los poligonos
        #poligono.sort(key= lambda punto: punto[1])
        #llamar a la funcion de poligonos para que los dibuje
        drawPoligono(poligono)
        
    pygame.display.flip()
    clock.tick(60)

rend.glGenerateFrameBuffer("output.bmp")
pygame.quit()
