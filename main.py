from PIL import Image, ImageDraw

import cube
import draw

Width = 800
Margin = 10

solved_cube = cube.Cube.solved().apply_moves("z2")

t_perm = solved_cube.apply_moves("PLL-T")

img = draw.draw_cube(t_perm, Width, Margin, "#90ee90")
img.show()
#img.save("001.png")
