import pygame
import ast
import os

# Archivo con las dos matrices (mapa_1 y mapa_2)
MAP_FILE = "mapaaa.py"  # Debe estar en la misma carpeta que este archivo

# Ruta a tu imagen PNG del bloque
IMAGE_PATH = "bloque.png"  # Coloca el PNG en la misma carpeta que este archivo
# Tamaño fijo del bloque (None para usar el tamaño nativo del PNG)
TILE_SIZE = None
# Modo pantalla completa
FULLSCREEN = True


def load_block_image():
    """Carga la imagen del bloque; si no existe, crea un placeholder."""
    try:
        img = pygame.image.load(IMAGE_PATH)
        if TILE_SIZE:
            img = pygame.transform.smoothscale(img, (TILE_SIZE, TILE_SIZE))
    except Exception:
        size = TILE_SIZE if TILE_SIZE else 32
        img = pygame.Surface((size, size), pygame.SRCALPHA)
        img.fill((200, 200, 200))
        pygame.draw.rect(img, (80, 80, 80), img.get_rect(), 2)
    return img


def extract_list_from_source(src, varname):
    """Extrae de manera segura la lista asignada a varname en el código fuente.
    Evita ejecutar import de mapaaa.py (que podría tener código inválido),
    leyendo el archivo como texto y parseando solo la lista.
    """
    key = f"{varname}"
    idx = src.find(key)
    if idx == -1:
        raise ValueError(f"No se encontró {varname} en el archivo.")
    # Buscar el '=' después del nombre
    eq = src.find('=', idx)
    if eq == -1:
        raise ValueError(f"No se encontró '=' para {varname}.")
    # Buscar el primer '[' después de '='
    lb = src.find('[', eq)
    if lb == -1:
        raise ValueError(f"No se encontró '[' inicial de la lista {varname}.")
    # Recorrer para encontrar el ']' que cierra la lista completa (contando anidación)
    depth = 0
    for i in range(lb, len(src)):
        c = src[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                rb = i
                break
    else:
        raise ValueError(f"No se encontró el cierre ']' de la lista {varname}.")

    list_text = src[lb:rb + 1]
    # Usar literal_eval para seguridad (solo literales)
    return ast.literal_eval(list_text)


def load_maps(map_path):
    """Carga mapa_1 y mapa_2 desde mapaaa.py sin importarlo."""
    with open(map_path, 'r', encoding='utf-8') as f:
        src = f.read()
    m1 = extract_list_from_source(src, 'mapa_1')
    m2 = extract_list_from_source(src, 'mapa_2')
    return m1, m2


def compute_screen_size(m1, m2, tile_w, tile_h, gap_tiles=1):
    # Muestra ambos mapas lado a lado, con un espacio (gap) entre ellos
    rows1 = len(m1)
    cols1 = len(m1[0]) if rows1 > 0 else 0
    rows2 = len(m2)
    cols2 = len(m2[0]) if rows2 > 0 else 0

    width = cols1 * tile_w + (gap_tiles * tile_w) + cols2 * tile_w
    height = max(rows1 * tile_h, rows2 * tile_h)
    return width, height


def compute_tile_size_to_fit_screen(m1, m2, display_w, display_h, gap_tiles=1):
    """Devuelve el tamaño de tile (entero) más grande que permite que ambos mapas
    (en formato lado a lado) quepan dentro de display_w x display_h.
    """
    rows1 = len(m1)
    cols1 = len(m1[0]) if rows1 > 0 else 0
    rows2 = len(m2)
    cols2 = len(m2[0]) if rows2 > 0 else 0

    total_cols = cols1 + gap_tiles + cols2
    total_rows = max(rows1, rows2)

    if total_cols <= 0 or total_rows <= 0:
        return 32  # fallback razonable

    ts_w = max(1, display_w // total_cols)
    ts_h = max(1, display_h // total_rows)
    return max(1, min(ts_w, ts_h))

def draw_matrix(screen, matrix, block, tile_w, tile_h, offset_x=0, offset_y=0):
    for y, row in enumerate(matrix):
        for x, val in enumerate(row):
            # En mapaaa.py los valores son strings ("1", "0", etc.). Acepta "1 " con espacios.
            is_one = (val == 1)
            if not is_one and isinstance(val, str):
                is_one = val.strip() == "1"
            if is_one:
                screen.blit(block, (offset_x + x * tile_w, offset_y + y * tile_h))


def main():
    pygame.init()

    # Cargar las dos matrices desde mapaaa.py
    map_path = os.path.join(os.path.dirname(__file__), MAP_FILE)
    try:
        mapa_1, mapa_2 = load_maps(map_path)
    except Exception as e:
        raise SystemExit(f"Error al leer {MAP_FILE}: {e}")

    # Obtener tamaño de pantalla disponible (antes de crear la ventana)
    info = pygame.display.Info()
    disp_w, disp_h = info.current_w, info.current_h

    # Calcular tamaño de tile para que la composición completa quepa en pantalla
    tile_size = compute_tile_size_to_fit_screen(mapa_1, mapa_2, disp_w, disp_h, gap_tiles=1)

    # Ajustar TILE_SIZE global y cargar/escala la imagen del bloque
    global TILE_SIZE
    TILE_SIZE = tile_size
    block = load_block_image()
    tile_w, tile_h = block.get_size()

    # Calcular área de contenido y crear ventana
    screen_w, screen_h = compute_screen_size(mapa_1, mapa_2, tile_w, tile_h, gap_tiles=1)
    flags = pygame.FULLSCREEN if FULLSCREEN else 0
    if FULLSCREEN:
        screen = pygame.display.set_mode((disp_w, disp_h), flags)
        offset_base_x = max(0, (disp_w - screen_w) // 2)
        offset_base_y = max(0, (disp_h - screen_h) // 2)
    else:
        screen = pygame.display.set_mode((screen_w, screen_h), flags)
        offset_base_x = 0
        offset_base_y = 0
    pygame.display.set_caption("Mapas (mapa_1 y mapa_2) -> Bloques PNG")

    # Convertir para acelerar blits (tras crear la pantalla)
    block = block.convert_alpha()

    clock = pygame.time.Clock()
    running = True

    # Offset del segundo mapa (lo ponemos a la derecha del primero con 1 tile de separación)
    offset2_x = offset_base_x + len(mapa_1[0]) * tile_w + 1 * tile_w

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

        screen.fill((20, 20, 20))
        draw_matrix(screen, mapa_1, block, tile_w, tile_h, offset_x=offset_base_x, offset_y=offset_base_y)
        draw_matrix(screen, mapa_2, block, tile_w, tile_h, offset_x=offset2_x, offset_y=offset_base_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
