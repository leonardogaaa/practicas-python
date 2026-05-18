import pygame
import sys
import random

# --- 1. Inicialización de Pygame ---
pygame.init()

# --- 2. Configuración de la Pantalla ---
ANCHO, ALTO = 800, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego de Pong")

# --- 3. Colores ---
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (19,255,0)
AMARILLO = (204, 255, 0)
# --- 4. Variables del Juego ---
VELOCIDAD_RAQUETA_IA = 14

# Raqueta del Jugador
raqueta_jugador_ancho = 20
raqueta_jugador_alto = 100
raqueta_jugador_x = ANCHO - raqueta_jugador_ancho - 10 # Cerca del borde derecho
raqueta_jugador_y = ALTO // 2 - raqueta_jugador_alto // 2
raqueta_jugador = pygame.Rect(raqueta_jugador_x, raqueta_jugador_y, raqueta_jugador_ancho, raqueta_jugador_alto)


# Raqueta de la IA
raqueta_ia_ancho = 20
raqueta_ia_alto = 100
raqueta_ia_x = 10 # Cerca del borde izquierdo
raqueta_ia_y = ALTO // 2 - raqueta_ia_alto // 2
raqueta_ia = pygame.Rect(raqueta_ia_x, raqueta_ia_y, raqueta_ia_ancho, raqueta_ia_alto)

# Pelota
pelota_radio = 10
pelota_x = ANCHO // 2
pelota_y = ALTO // 2
pelota_dx = random.choice([-5, 5]) # Dirección inicial aleatoria en X
pelota_dy = random.choice([-5, 5]) # Dirección inicial aleatoria en Y
pelota_rect = pygame.Rect(pelota_x - pelota_radio, pelota_y - pelota_radio, pelota_radio * 2, pelota_radio * 2)

# Puntuación
puntuacion_jugador = 0
puntuacion_ia = 0
FUENTE = pygame.font.Font(None, 74) # Fuente para el texto

# --- 5. Bucle Principal del Juego ---
CLOCK = pygame.time.Clock()
FPS = 60

running = True
while running:
    # --- 5.1 Manejo de Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # El jugador controla con el ratón
        if pelota_dx==10 or pelota_dx==-10:
            pelota_dx=-11


        if event.type == pygame.MOUSEMOTION:
            raqueta_jugador.y = event.pos[1] - raqueta_jugador_alto // 2
            # Asegurar que la raqueta no salga de la pantalla
            if raqueta_jugador.top < 0:
                raqueta_jugador.top = 0
            if raqueta_jugador.bottom > ALTO:
                raqueta_jugador.bottom = ALTO

    # --- 5.2 Lógica del Juego ---

    # Mover la pelota
    pelota_rect.x += pelota_dx
    pelota_rect.y += pelota_dy

    # Rebotar en los bordes superior/inferior
    if pelota_rect.top <= 0 or pelota_rect.bottom >= ALTO:
        pelota_dy *= -1

    # Rebotar en las raquetas
    if pelota_rect.colliderect(raqueta_jugador):
        pelota_dx *= -1
        # Pequeño ajuste para evitar que se quede pegada
        pelota_rect.right = raqueta_jugador.left 
    
    if pelota_rect.colliderect(raqueta_ia):
        pelota_dx *= -1
        pelota_dx+=0.5
        # Pequeño ajuste para evitar que se quede pegada
        pelota_rect.left = raqueta_ia.right

    # Si la pelota sale por los lados (puntuación)
    if pelota_rect.left <= 0: # La IA no pudo devolverla
        puntuacion_jugador += 1
        pelota_rect.x, pelota_rect.y = ANCHO // 2, ALTO // 2 # Reiniciar pelota
        pelota_dx = random.choice([-5, 5]) # Nueva dirección aleatoria
        pelota_dy = random.choice([-5, 5])
    elif pelota_rect.right >= ANCHO: # El jugador no pudo devolverla
        puntuacion_ia += 1
        pelota_rect.x, pelota_rect.y = ANCHO // 2, ALTO // 2 # Reiniciar pelota
        pelota_dx = random.choice([-5, 5]) # Nueva dirección aleatoria
        pelota_dy = random.choice([-5, 5])

    # Lógica de la IA (sigue la pelota)
    if pelota_rect.x<ANCHO//2:
        if raqueta_ia.centery < pelota_rect.centery:
            raqueta_ia.y += VELOCIDAD_RAQUETA_IA
        elif raqueta_ia.centery > pelota_rect.centery:
            raqueta_ia.y -= VELOCIDAD_RAQUETA_IA
    
    # Asegurar que la raqueta de la IA no salga de la pantalla
    if raqueta_ia.top < 0:
        raqueta_ia.top = 0
    if raqueta_ia.bottom > ALTO:
        raqueta_ia.bottom = ALTO

    # --- 5.3 Dibujar en la Pantalla ---
    PANTALLA.fill(NEGRO) # Fondo negro

    pygame.draw.rect(PANTALLA, BLANCO, raqueta_jugador) # Dibujar raqueta del jugador
    pygame.draw.rect(PANTALLA, BLANCO, raqueta_ia)      # Dibujar raqueta de la IA
    pygame.draw.circle(PANTALLA, BLANCO, pelota_rect.center, pelota_radio) # Dibujar pelota
    pygame.draw.rect(PANTALLA, VERDE, raqueta_jugador, 4)
    pygame.draw.rect(PANTALLA, AMARILLO, raqueta_ia, 4)
    # Dibujar la línea central (opcional)
    pygame.draw.aaline(PANTALLA, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))

    # Mostrar puntuación
    texto_puntuacion_jugador = FUENTE.render(str(puntuacion_jugador), True, BLANCO)
    texto_puntuacion_ia = FUENTE.render(str(puntuacion_ia), True, BLANCO)
    PANTALLA.blit(texto_puntuacion_ia, (ANCHO // 4, 10))
    PANTALLA.blit(texto_puntuacion_jugador, (ANCHO * 3 // 4 - texto_puntuacion_jugador.get_width(), 10))

    # --- 5.4 Actualizar Pantalla ---
    pygame.display.flip()

    # Controlar FPS
    CLOCK.tick(FPS)

# --- 6. Salir de Pygame ---
pygame.quit()
sys.exit()