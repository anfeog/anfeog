import math, os

OUT = r"X:\ANIME\PRUEBA\github-profile\assets"
os.makedirs(OUT, exist_ok=True)

# Paleta muestreada del fondo de caja (Gen 3)
DEEP  = "#1E6FB8"
BASE  = "#2E82CC"
MID   = "#4098DE"
LIGHT = "#5FB0EC"
SOFT  = "#82C6F4"
PALE  = "#A8DCFF"
FOAM  = "#D2EEFF"
WHITE = "#FFFFFF"


def rects_to_svg(grid, cols, rows, px, w, h, extra=""):
    """Fusiona horizontalmente celdas del mismo color para reducir el nº de <rect>."""
    parts = []
    for y in range(rows):
        x = 0
        while x < cols:
            c = grid[y][x]
            if c is None:
                x += 1
                continue
            run = 1
            while x + run < cols and grid[y][x + run] == c:
                run += 1
            parts.append(
                f'<rect x="{x*px}" y="{y*px}" width="{run*px}" height="{px}" fill="{c}"/>'
            )
            x += run
    body = "".join(parts)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img">{body}{extra}</svg>'
    )


def wave(grid, cols, rows, base_row, amp, period, phase, color):
    """Rellena desde la cresta de la ola hacia abajo, con la cresta cuantizada a pixel."""
    for x in range(cols):
        hgt = round((math.sin(2 * math.pi * x / period + phase) + 1) / 2 * amp)
        crest = base_row - hgt
        for y in range(max(0, crest), rows):
            grid[y][x] = color


def dither(grid, cols, row, color, step=2, offset=0):
    """Trama de damero: la textura pixelada del fondo original."""
    for x in range(cols):
        if (x + offset) % step == 0:
            grid[row][x] = color


# ---------------------------------------------------------------- BANNER
# Rampa fina: bandas cercanas entre sí para que la trama sea textura, no rayas
RAMP = ["#1B6AB4", "#2274BD", "#297EC6", "#3189CF", "#3A94D8",
        "#439FE0", "#4DAAE8", "#57B5EF", "#62BFF4", "#6FC8F8"]

PX, COLS, ROWS = 6, 200, 38
W, H = COLS * PX, ROWS * PX
g = [[RAMP[0] for _ in range(COLS)] for _ in range(ROWS)]

WATER_ROWS = 30                      # el oleaje ocupa solo el tramo final
band_h = WATER_ROWS / len(RAMP)
for y in range(ROWS):
    idx = min(int(y / band_h), len(RAMP) - 1)
    g[y] = [RAMP[idx]] * COLS

# Trama de damero en cada transición de banda: dos filas, densidad decreciente
for i in range(1, len(RAMP)):
    edge = int(i * band_h)
    if edge < ROWS:
        dither(g, COLS, edge, RAMP[i - 1], 2, 0)
    if edge - 1 >= 0:
        dither(g, COLS, edge - 1, RAMP[i], 4, 2)

# Oleaje inferior, de atrás hacia adelante
wave(g, COLS, ROWS, 32, 3, 44, 0.0, PALE)
wave(g, COLS, ROWS, 35, 3, 31, 1.9, FOAM)
wave(g, COLS, ROWS, 38, 3, 23, 3.6, WHITE)

TITLE = "ANDR&#201;S FELIPE ORTIZ"
SUB = "Ingenier&#237;a Industrial &#183; Anal&#237;tica de Datos &#183; Automatizaci&#243;n"
text = (
    f'<text x="{W//2}" y="118" text-anchor="middle" '
    f'font-family="Verdana,DejaVu Sans,sans-serif" font-size="46" font-weight="bold" '
    f'letter-spacing="3" fill="#0C3D6B" opacity="0.35">{TITLE}</text>'
    f'<text x="{W//2}" y="115" text-anchor="middle" '
    f'font-family="Verdana,DejaVu Sans,sans-serif" font-size="46" font-weight="bold" '
    f'letter-spacing="3" fill="#FFFFFF">{TITLE}</text>'
    f'<text x="{W//2}" y="152" text-anchor="middle" '
    f'font-family="Verdana,DejaVu Sans,sans-serif" font-size="17" '
    f'letter-spacing="1" fill="#DCF2FF">{SUB}</text>'
)
open(os.path.join(OUT, "banner.svg"), "w", encoding="utf-8").write(
    rects_to_svg(g, COLS, ROWS, PX, W, H, text)
)

# ---------------------------------------------------------------- DIVISOR
PX2, COLS2, ROWS2 = 6, 200, 6
W2, H2 = COLS2 * PX2, ROWS2 * PX2
d = [[RAMP[3] for _ in range(COLS2)] for _ in range(ROWS2)]
d[0] = [RAMP[1]] * COLS2
d[1] = [RAMP[2]] * COLS2
dither(d, COLS2, 1, RAMP[1], 2, 0)
dither(d, COLS2, 2, RAMP[2], 2, 1)
wave(d, COLS2, ROWS2, 4, 2, 37, 0.0, PALE)
wave(d, COLS2, ROWS2, 6, 2, 25, 2.2, FOAM)
open(os.path.join(OUT, "divider.svg"), "w", encoding="utf-8").write(
    rects_to_svg(d, COLS2, ROWS2, PX2, W2, H2)
)

for f in ("banner.svg", "divider.svg"):
    print(f, os.path.getsize(os.path.join(OUT, f)), "bytes")
