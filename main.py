import random
import tkinter
from PIL import ImageTk

import cube
import draw

Width = 580
Margin = 10

BG_Color = "#90ee90"

cur_index = 0
is_q = True

solved_cube = cube.Cube.solved().apply_moves("z2")

pll_names = random.sample(cube.pll_names, len(cube.pll_names))

root = tkinter.Tk()

root.title('cube')
root.geometry('600x800')
root.resizable(False, False)

frame1 = tkinter.Frame(root, width=600, height=600)
frame2 = tkinter.Frame(root, width=600, height=200)

# Frameサイズを固定
frame1.propagate(False)
frame2.propagate(False)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)

def get_cur_image():
    pre_y = "y " * random.randint(0, 3)
    post_y = " y" * random.randint(0, 3)

    state = solved_cube.apply_moves(pre_y + pll_names[cur_index] + "'" + post_y)

    return draw.draw_cube(state, Width, Margin, BG_Color)

image = ImageTk.PhotoImage(get_cur_image())
label_img = tkinter.Label(frame1, image=image)
label_img.pack(expand=True, fill=tkinter.BOTH)

def click_btn(event=None):
    global is_q, cur_index

    if is_q == False and cur_index == len(pll_names)-1:
        return

    if is_q:
        label_name['text'] = pll_names[cur_index]
        label_move['text'] = cube.pll_notes[pll_names[cur_index]]

        if cur_index == len(pll_names)-1:
            button["state"] ="disabled"
    else:
        cur_index += 1

        label_name['text'] = ''
        label_move['text'] = ''

        img = ImageTk.PhotoImage(get_cur_image())
        label_img.configure(image=img)
        label_img.image = img

    is_q = not is_q

button = tkinter.Button(frame2, text='次へ', command=click_btn)
button.pack(padx=5, pady=10)

label_name = tkinter.Label(frame2, text='', font=('System', 14))
label_name.pack(padx=5, pady=10)

label_move = tkinter.Label(frame2, text='', font=('System', 14))
label_move.pack(padx=5, pady=10)

root.bind("<space>", click_btn)

root.mainloop()
