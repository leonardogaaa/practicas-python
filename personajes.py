import pygame, sys

class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def mostrar_info(self):
        print(f"{self.nombre} - Vida: {self.vida}")


class Principal(Personaje):
    def __init__(self):
        super().__init__("Jugador", 100)
        self.image = pygame.image.load("personaje.png")  #variable para cargar imagen del personaje
        self.municion = 0  
        self.direccion = pygame.math.Vector2(100, 100)    #se define que el movimiento tendra un eje X y Y al poner vector2
    def teclado(self):     #movimiento con el teclado
        keys = pygame.key.get_pressed()  #verifca todo el tiempo si una tecla es precionada
        if keys[pygame.K_RIGHT]:         #verifica si la tecla derecha es presionada
            self.direccion.x = 1
        elif keys[pygame.K_LEFT]:       #verifica si la tecla Izquierda es presionada
            self.direccion.y = -1
        else: 
            self.direccion.x = 0        #si no se preciona nada no avanza
    def update(self):
        self.teclado()                  
    def mostrar_info(self):
        print(f"{self.nombre} - Vida: {self.vida}, Munición: {self.municion}")


class Enemigo(Personaje):
    def __init__(self, numero):
        super().__init__(f"Enemigo {numero}", 100)

class Jefe(Personaje):
    def __init__(self):
        super().__init__("Jefe Final", 400)
        self.posicion = 0  
        self.direccion = 1  


jugador = Principal()
enemigo1 = Enemigo(1)
enemigo2 = Enemigo(2)
jefe = Jefe()

jugador.mostrar_info()
enemigo1.mostrar_info()
enemigo2.mostrar_info()
jefe.mostrar_info()