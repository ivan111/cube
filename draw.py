from PIL import Image, ImageDraw

Root3 = 1.732

color_map = [
    "white", # White
    "green", # Green
    "red", # Red
    "#2080df", # Blue
    "#ff8c00", # Orange
    "yellow", # Yellow
]

def convert_point(pt, width, margin):
    x = margin + int((pt[0] + 4.0) * width / 8.0)
    y = margin + int((5.5 - pt[1]) * width / 8.0)

    return (x, y)

def vec_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def create_cubie_vec(a, b):
    return (int((b[0] - a[0]) / 3), int((b[1] - a[1]) / 3))

def draw_cubie(draw, o, v_x, v_y, colors, outline, width):
    for y_i in range(3):
        for x_i in range(3):
            x = o[0] + v_x[0] * x_i + v_y[0] * y_i
            y = o[1] + v_x[1] * x_i + v_y[1] * y_i

            a = vec_add((x, y), v_x)

            c_i = x_i + y_i * 3
            color = color_map[colors[c_i]]
            draw.polygon([(x, y), a, vec_add(a, v_y), vec_add((x, y), v_y)], fill=color, outline=outline, width=width)

def draw_cube(cube, img_width, margin, bg_color="gray", is_show_mirror=True):
    img = Image.new("RGB", (img_width + margin*2, img_width + margin*2), bg_color)
    draw = ImageDraw.Draw(img)

    fill = "black"
    width = 4

    dfr = convert_point((0, 0), img_width, margin)
    dfl = convert_point((-Root3, 1), img_width, margin)
    ufl = convert_point((-Root3, 3), img_width, margin)
    ubl = convert_point((0, 4), img_width, margin)
    ubr = convert_point((Root3, 3), img_width, margin)
    dbr = convert_point((Root3, 1), img_width, margin)
    ufr = convert_point((0, 2), img_width, margin)

    # mirror
    mg = 0.1

    ml_ufl = convert_point((-Root3 * 2 - mg, 4), img_width, margin)
    ml_ubl = convert_point((-Root3 - mg, 5), img_width, margin)
    ml_dbl = convert_point((-Root3 - mg, 3), img_width, margin)
    ml_dfl = convert_point((-Root3 * 2 - mg, 2), img_width, margin)

    md_dbl = convert_point((0, 0 - mg), img_width, margin)
    md_dbr = convert_point((Root3, -1 - mg), img_width, margin)
    md_dfr = convert_point((0, -2 - mg), img_width, margin)
    md_dfl = convert_point((-Root3, -1 - mg), img_width, margin)

    mb_ubl = convert_point((Root3 + mg, 5), img_width, margin)
    mb_ubr = convert_point((Root3 * 2 + mg, 4), img_width, margin)
    mb_dbr = convert_point((Root3 * 2 + mg, 2), img_width, margin)
    mb_dbl = convert_point((Root3 + mg, 3), img_width, margin)

    u_x = create_cubie_vec(ubl, ubr)
    u_y = create_cubie_vec(ubl, ufl)

    f_x = create_cubie_vec(ufl, ufr)
    f_y = create_cubie_vec(ufl, dfl)

    r_x = create_cubie_vec(ufr, ubr)
    r_y = create_cubie_vec(ufr, dfr)

    ml_x = create_cubie_vec(ml_ufl, ml_ubl)
    ml_y = create_cubie_vec(ml_ufl, ml_dfl)

    mb_x = create_cubie_vec(mb_ubl, mb_ubr)
    mb_y = create_cubie_vec(mb_ubl, mb_dbl)

    md_x = create_cubie_vec(md_dbl, md_dbr)
    md_y = create_cubie_vec(md_dbl, md_dfl)

    draw_cubie(draw, ubl, u_x, u_y, cube.get_up_colors(), fill, width)
    draw_cubie(draw, ufl, f_x, f_y, cube.get_front_colors(), fill, width)
    draw_cubie(draw, ufr, r_x, r_y, cube.get_right_colors(), fill, width)

    if is_show_mirror:
        draw_cubie(draw, ml_ufl, ml_x, ml_y, cube.get_left_colors(), fill, width)
        draw_cubie(draw, mb_ubl, mb_x, mb_y, cube.get_back_colors(), fill, width)
        draw_cubie(draw, md_dbl, md_x, md_y, cube.get_down_colors(), fill, width)

    return img
