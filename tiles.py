import pygame
import sys
from nivel import Nivel
import personajes 
class Main1:
    def __init__(self):
        pygame.init()
        self.White = (100, 180, 230) #color de pantalla
        pygame.display.set_caption("Proyecto 1")  #nombre a la ventana
    #tamaño de pantalla
        self.size = (1200, 750) #tamaño de pantalla
        self.screen = pygame.display.set_mode(self.size)    #tamaño de pantalla
        self.nivel = Nivel()
    def arranque(self):

speed_x=0
speed_y=0




while True:                       #mantener la pantalla abierta            
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() #metodo para poder salir de la pantalla

        class Principal(Personaje):
         def __init__(self):
            super().__init__("Jugador", 100)
            self.image = pygame.image.load("personaje.png")  #variable para cargar imagen del personaje
            self.municion = 0  
            self.direccion = pygame.math.Vector2(100, 100)    #se define que el movimiento tendra un eje X y Y al poner vector2
            if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_LEFT:
                      speed_x=-3
                 if event.key==pygame.K_RIGHT:
                      speed_x=3
                 if event.key==pygame.K_UP:
                      speed_y=-3
                 if event.key==pygame.K_DOWN:
                      speed_x=3
        if coord_y>coord_y-3:
            speed_y=3
        if coord_y>750:
            
                      
            if event.type==pygame.KEYUP:
                 if event.key==pygame.K_LEFT:
                      speed_x=0
                 if event.key==pygame.K_RIGHT:
                      speed_x=0


        coord_x=100
        coord_y=100
        coord_x+=speed_x
        coord_y+=speed_y
        coord_y=coord_y+speed_y
        self.screen.fill(self.White)  #relleno de la pantalla
        self.nivel.corre()
        pygame.display.update()                  #actualización de la pantalla

if __name__ == "__main__":  #llamada de la clase Main1
    juego = Main1()
    juego.arranque()
