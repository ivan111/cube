import cube
import draw
from PIL import Image, ImageDraw, ImageFont


setup = ""
str_A = "M2"
str_B = "U2"


solved_cube = cube.Cube.solved()

A = solved_cube.apply_moves(str_A)
B = solved_cube.apply_moves(str_B)
Ap = cube.get_prime_move(A)
Bp = cube.get_prime_move(B)

if setup != "":
    SETUP = solved_cube.apply_moves(setup)
    SETUP_P = cube.get_prime_move(SETUP)
    res = SETUP.apply_move(A).apply_move(B).apply_move(Ap).apply_move(Bp).apply_move(SETUP_P)
else:
    res = A.apply_move(B).apply_move(Ap).apply_move(Bp)

Width = 300
Margin = 10

BG_Color = "white"

font = ImageFont.truetype('meiryo.ttc', 18)

img_res = draw.draw_changed_cube(res.get_changed_list(), Width, Margin, "pink", BG_Color)
d = ImageDraw.Draw(img_res)
res_text = "[" + str_A + ", " + str_B + "]"
if setup != "":
    res_text += " setup=" + setup
d.text((4, 4), res_text, 'black', font=font)

img_J = draw.draw_changed_cube(A.get_changed_list(), Width, Margin, "red", BG_Color)
d = ImageDraw.Draw(img_J)
d.text((4, 4), 'J=A(' + str_A + ')で動く', 'black', font=font)

img_K = draw.draw_changed_cube(B.get_changed_list(), Width, Margin, "green", BG_Color)
d = ImageDraw.Draw(img_K)
d.text((4, 4), 'K=B(' + str_B + ')で動く', 'black', font=font)

p = [[aa and bb for aa, bb in zip(a, b)] for a, b in zip(A.get_changed_list(), B.get_changed_list())]
img_N = draw.draw_changed_cube(p, Width, Margin, "blue", BG_Color)
d = ImageDraw.Draw(img_N)
d.text((4, 4), 'N=JとKの重なり', 'black', font=font)

img_NAp = draw.draw_changed_cube(Ap.get_changed_list2(B), Width, Margin, "blue", BG_Color)
d = ImageDraw.Draw(img_NAp)
d.text((4, 4), 'NA\'=AによってNへ', 'black', font=font)

img_NBp = draw.draw_changed_cube(Bp.get_changed_list2(A), Width, Margin, "blue", BG_Color)
d = ImageDraw.Draw(img_NBp)
d.text((4, 4), 'NB\'=BによってNへ', 'black', font=font)

img = Image.new("RGB", (img_res.width + img_J.width + img_K.width, img_res.height + img_N.height))

img.paste(img_res, (0, 0))
img.paste(img_J, (img_res.width, 0))
img.paste(img_K, (img_res.width + img_J.width, 0))

img.paste(img_N, (0, img_res.height))
img.paste(img_NAp, (img_N.width, img_res.height))
img.paste(img_NBp, (img_N.width + img_NAp.width, img_res.height))

img.save("com.png")
