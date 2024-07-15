# Lab 1 : Filling Any Polygon - graficas por computadora
# Autor: Angela Garcia, 22869
#librerias:
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

# Metodo usado: relleno mediante trazado de bordes con colas (queue-based boundaryfill)
# consiste en usar una cola para almacenar los pixeles que se deben rellenar
# y una lista de pixeles visitados para no volver a visitarlos
# se empieza en un punto y se verifica si el pixel esta dentro del poligono
# si esta dentro se pinta y se agregan los pixeles adyacentes a la cola
# se repite el proceso hasta que la cola este vacia
# escogí este metodo porque es el mas eficiente para rellenar poligonos y se miraba corto el pseudocodigo xd

def verificacionPixelDentroDelPoligono(x, y):
    #x, y = punto
    n = len(poligono)
    inside = False
    
    for i in range(n):
        x1, y1 = poligono[i] #actual
        x2, y2 = poligono[(i + 1) % n] #siguiente
        
        if (y1 < y and y2 >= y) or (y2 < y and y1>=y):
            if x1 + (y - y1)/(y2 - y1)*(x2 - x1) < x:
                inside = not inside
    return inside

def fill(x,y, fillcolor, borderColor):
    queue = [(x,y)] #inicializar la cola
    visited = set()#inicializar el conjunto de visitados// 
    while queue:
        x,y = queue.pop(0)
        if (x,y) not in visited: 
            
            visited.add((x,y))
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]: #verificar los pixeles adyacentes //en esta parte use github copilot, no hay conversación porque lo trae integrado
                
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited: 
                    
                    if verificacionPixelDentroDelPoligono(nx, ny):
                        queue.append((nx, ny))
                        rend.glPoint(nx, ny, (1, 0, 0.5) )
    
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
        #jalar los puntos iniciles de cada poligono
        x,y = poligono[0]
        fill(x,y, fillcolor= None, borderColor=None)    
    #punto = (200, 200)
    #print(verificacionPixelDentroDelPoligono(punto, poligono1))
    pygame.display.flip()
    clock.tick(60)

rend.glGenerateFrameBuffer("output.bmp")
pygame.quit()