import pygame 
import mapa
from tiles import Tile  #llamada a la clase Tile del archivo tile
from personajes import Aspecto

class Nivel:
    def __init__(self):
        self.screen = pygame.display.get_surface()    #sirve para que se muestren siempre a la pantalla los procesos
        self.Sprite_fondo= pygame.sprite.Group()      #Una clase contenedora para almacenar y administrar múltiples objetos Sprite.
        self.caja = pygame.sprite.Group()
        self.crearmapa()                                #llamada a la función crearmapa
    def crearmapa(self):        #leer cada coordenada de la matriz
        for row_intex, row in enumerate(mapa.mapa):  #linea
            for col_index, col in enumerate(row):  #columnas de cada linea
                x = col_index * 68 #tamaño de la imagen por cada x
                y = row_intex * 68 #tamaño de la imagen por cada y
                if col == "z":
                    Tile((x,y), [self.Sprite_fondo, self.caja])
                if col == "x":
                    Nube((x,y), [self.Sprite_fondo])
                if col == "p":
                    Aspecto((x,y), [self.Sprite_fondo, self.caja])
    def corre(self):
        self.Sprite_fondo.draw(self.screen)
