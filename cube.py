White  = 0
Green  = 1
Red    = 2
Blue   = 3
Orange = 4
Yellow = 5

# center piece colors
o_colors = [
    White, Green, Red, Blue, Orange, Yellow,
]

# corner piece colors
c_colors = [
    [White, Blue, Orange],
    [White, Red, Blue],
    [White, Green, Red],
    [White, Orange, Green],
    [Yellow, Orange, Blue],
    [Yellow, Blue, Red],
    [Yellow, Red, Green],
    [Yellow, Green, Orange],
]

# edge piece colors
e_colors = [
    [Blue, Orange],
    [Blue, Red],
    [Green, Red],
    [Green, Orange],
    [White, Blue],
    [White, Red],
    [White, Green],
    [White, Orange],
    [Yellow, Blue],
    [Yellow, Red],
    [Yellow, Green],
    [Yellow, Orange],
]


class Cube:
    def __init__(self, op, cp, co, ep, eo):
        self.op = op
        self.cp = cp
        self.co = co
        self.ep = ep
        self.eo = eo

    @classmethod
    def solved(cls):
        return cls(list(range(6)), list(range(8)), [0] * 8, list(range(12)), [0] * 12)

    def apply_move(self, move):
        new_op = [self.op[p] for p in move.op]
        new_cp = [self.cp[p] for p in move.cp]
        new_co = [(self.co[p] + move.co[i]) % 3 for i, p in enumerate(move.cp)]
        new_ep = [self.ep[p] for p in move.ep]
        new_eo = [(self.eo[p] + move.eo[i]) % 2 for i, p in enumerate(move.ep)]

        return Cube(new_op, new_cp, new_co, new_ep, new_eo)

    def apply_moves(self, mvs):
        state = self

        for move_name in mvs.split(" "):
            if move_name in moves:
                state = state.apply_move(moves[move_name])
            else:
                print("unknown move command: [" + move_name + "]")

        return state

    def get_up_colors(self):
        colors = [""] * 9

        colors[0] = c_colors[self.cp[0]][self.co[0]]
        colors[1] = e_colors[self.ep[4]][self.eo[4]]
        colors[2] = c_colors[self.cp[1]][self.co[1]]
        colors[3] = e_colors[self.ep[7]][self.eo[7]]
        colors[4] = o_colors[self.op[0]]
        colors[5] = e_colors[self.ep[5]][self.eo[5]]
        colors[6] = c_colors[self.cp[3]][self.co[3]]
        colors[7] = e_colors[self.ep[6]][self.eo[6]]
        colors[8] = c_colors[self.cp[2]][self.co[2]]

        return colors

    def get_front_colors(self):
        colors = [""] * 9

        colors[0] = c_colors[self.cp[3]][(self.co[3] + 2) % 3]
        colors[1] = e_colors[self.ep[6]][(self.eo[6] + 1) % 2]
        colors[2] = c_colors[self.cp[2]][(self.co[2] + 1) % 3]
        colors[3] = e_colors[self.ep[3]][self.eo[3]]
        colors[4] = o_colors[self.op[1]]
        colors[5] = e_colors[self.ep[2]][self.eo[2]]
        colors[6] = c_colors[self.cp[7]][(self.co[7] + 1) % 3]
        colors[7] = e_colors[self.ep[10]][(self.eo[10] + 1) % 2]
        colors[8] = c_colors[self.cp[6]][(self.co[6] + 2) % 3]

        return colors

    def get_right_colors(self):
        colors = [""] * 9

        colors[0] = c_colors[self.cp[2]][(self.co[2] + 2) % 3]
        colors[1] = e_colors[self.ep[5]][(self.eo[5] + 1) % 2]
        colors[2] = c_colors[self.cp[1]][(self.co[1] + 1) % 3]
        colors[3] = e_colors[self.ep[2]][(self.eo[2] + 1) % 2]
        colors[4] = o_colors[self.op[2]]
        colors[5] = e_colors[self.ep[1]][(self.eo[1] + 1) % 2]
        colors[6] = c_colors[self.cp[6]][(self.co[6] + 1) % 3]
        colors[7] = e_colors[self.ep[9]][(self.eo[9] + 1) % 2]
        colors[8] = c_colors[self.cp[5]][(self.co[5] + 2) % 3]

        return colors

    def get_left_colors(self):
        colors = [""] * 9

        colors[0] = c_colors[self.cp[3]][(self.co[3] + 1) % 3]
        colors[1] = e_colors[self.ep[7]][(self.eo[7] + 1) % 2]
        colors[2] = c_colors[self.cp[0]][(self.co[0] + 2) % 3]
        colors[3] = e_colors[self.ep[3]][(self.eo[3] + 1) % 2]
        colors[4] = o_colors[self.op[4]]
        colors[5] = e_colors[self.ep[0]][(self.eo[0] + 1) % 2]
        colors[6] = c_colors[self.cp[7]][(self.co[7] + 2) % 3]
        colors[7] = e_colors[self.ep[11]][(self.eo[11] + 1) % 2]
        colors[8] = c_colors[self.cp[4]][(self.co[4] + 1) % 3]

        return colors

    def get_back_colors(self):
        colors = [""] * 9

        colors[0] = c_colors[self.cp[0]][(self.co[0] + 1) % 3]
        colors[1] = e_colors[self.ep[4]][(self.eo[4] + 1) % 2]
        colors[2] = c_colors[self.cp[1]][(self.co[1] + 2) % 3]
        colors[3] = e_colors[self.ep[0]][self.eo[0]]
        colors[4] = o_colors[self.op[3]]
        colors[5] = e_colors[self.ep[1]][self.eo[1]]
        colors[6] = c_colors[self.cp[4]][(self.co[4] + 2) % 3]
        colors[7] = e_colors[self.ep[8]][(self.eo[8] + 1) % 2]
        colors[8] = c_colors[self.cp[5]][(self.co[5] + 1) % 3]

        return colors

    def get_down_colors(self):
        colors = [""] * 9

        colors[0] = c_colors[self.cp[4]][self.co[4]]
        colors[1] = e_colors[self.ep[8]][self.eo[8]]
        colors[2] = c_colors[self.cp[5]][self.co[5]]
        colors[3] = e_colors[self.ep[11]][self.eo[11]]
        colors[4] = o_colors[self.op[5]]
        colors[5] = e_colors[self.ep[9]][self.eo[9]]
        colors[6] = c_colors[self.cp[7]][self.co[7]]
        colors[7] = e_colors[self.ep[10]][self.eo[10]]
        colors[8] = c_colors[self.cp[6]][self.co[6]]

        return colors


moves = {
    'x': Cube([1, 5, 2, 0, 4, 3],
               [3, 2, 6, 7, 0, 1, 5, 4],
               [2, 1, 2, 1, 1, 2, 1, 2],
               [7, 5, 9, 11, 6, 2, 10, 3, 4, 1, 8, 0],
               [0, 0, 0,  0, 1, 0,  1, 0, 1, 0, 1, 0]),

    'y': Cube([0, 2, 3, 4, 1, 5],
               [3, 0, 1, 2, 7, 4, 5, 6],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [3, 0, 1, 2, 7, 4, 5, 6, 11, 8, 9, 10],
               [1, 1, 1, 1, 0, 0, 0, 0,  0, 0, 0,  0]),

    'z': Cube([4, 1, 0, 3, 5, 2],
               [4, 0, 3, 7, 5, 1, 2, 6],
               [1, 2, 1, 2, 2, 1, 2, 1],
               [8, 4, 6, 10, 0, 7, 3, 11, 1, 5, 2, 9],
               [1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1, 1]),

    'U': Cube([0, 1, 2, 3, 4, 5],
               [3, 0, 1, 2, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0]),

    'D': Cube([0, 1, 2, 3, 4, 5],
               [0, 1, 2, 3, 5, 6, 7, 4],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0, 0]),

    'L': Cube([0, 1, 2, 3, 4, 5],
               [4, 1, 2, 0, 7, 5, 6, 3],
               [2, 0, 0, 1, 1, 0, 0, 2],
               [11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0]),

    'R': Cube([0, 1, 2, 3, 4, 5],
               [0, 2, 6, 3, 4, 1, 5, 7],
               [0, 1, 2, 0, 0, 2, 1, 0],
               [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0]),

    'F': Cube([0, 1, 2, 3, 4, 5],
               [0, 1, 3, 7, 4, 5, 2, 6],
               [0, 0, 1, 2, 0, 0, 2, 1],
               [0, 1, 6, 10, 4, 5, 3, 7, 8, 9, 2, 11],
               [0, 0, 1,  1, 0, 0, 1, 0, 0, 0, 1,  0]),

    'B': Cube([0, 1, 2, 3, 4, 5],
               [1, 5, 2, 3, 0, 4, 6, 7],
               [1, 2, 0, 0, 2, 1, 0, 0],
               [4, 8, 2, 3, 1, 5, 6, 7, 0, 9, 10, 11],
               [1, 1, 0, 0, 1, 0, 0, 0, 1, 0,  0,  0]),

    'M': Cube([3, 0, 2, 5, 4, 1],
               [0, 1, 2, 3, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 8, 5, 4, 7, 10, 9, 6, 11],
               [0, 0, 0, 0, 1, 0, 1, 0,  1, 0, 1,  0]),

    'E': Cube([0, 4, 1, 2, 3, 5],
               [0, 1, 2, 3, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11],
               [1, 1, 1, 1, 0, 0, 0, 0, 0, 0,  0,  0]),

    'S': Cube([4, 1, 0, 3, 5, 2],
               [0, 1, 2, 3, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 4, 7, 6, 11, 8, 5, 10, 9],
               [0, 0, 0, 0, 0, 1, 0,  1, 0, 1,  0, 1]),
               }

move_names = []
faces = list(moves.keys())

for face_name in faces:
    move_names += [face_name, face_name + '2', face_name + '\'']
    moves[face_name + '2'] = moves[face_name].apply_move(moves[face_name])
    moves[face_name + '\''] = moves[face_name + '2'].apply_move(moves[face_name])
moves = {
    'x': Cube([1, 5, 2, 0, 4, 3],
               [3, 2, 6, 7, 0, 1, 5, 4],
               [2, 1, 2, 1, 1, 2, 1, 2],
               [7, 5, 9, 11, 6, 2, 10, 3, 4, 1, 8, 0],
               [0, 0, 0,  0, 1, 0,  1, 0, 1, 0, 1, 0]),

    'y': Cube([0, 2, 3, 4, 1, 5],
               [3, 0, 1, 2, 7, 4, 5, 6],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [3, 0, 1, 2, 7, 4, 5, 6, 11, 8, 9, 10],
               [1, 1, 1, 1, 0, 0, 0, 0,  0, 0, 0,  0]),

    'z': Cube([4, 1, 0, 3, 5, 2],
               [4, 0, 3, 7, 5, 1, 2, 6],
               [1, 2, 1, 2, 2, 1, 2, 1],
               [8, 4, 6, 10, 0, 7, 3, 11, 1, 5, 2, 9],
               [1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1, 1]),

    'U': Cube([0, 1, 2, 3, 4, 5],
               [3, 0, 1, 2, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0]),

    'D': Cube([0, 1, 2, 3, 4, 5],
               [0, 1, 2, 3, 5, 6, 7, 4],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0, 0]),

    'L': Cube([0, 1, 2, 3, 4, 5],
               [4, 1, 2, 0, 7, 5, 6, 3],
               [2, 0, 0, 1, 1, 0, 0, 2],
               [11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 0]),

    'R': Cube([0, 1, 2, 3, 4, 5],
               [0, 2, 6, 3, 4, 1, 5, 7],
               [0, 1, 2, 0, 0, 2, 1, 0],
               [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0]),

    'F': Cube([0, 1, 2, 3, 4, 5],
               [0, 1, 3, 7, 4, 5, 2, 6],
               [0, 0, 1, 2, 0, 0, 2, 1],
               [0, 1, 6, 10, 4, 5, 3, 7, 8, 9, 2, 11],
               [0, 0, 1,  1, 0, 0, 1, 0, 0, 0, 1,  0]),

    'B': Cube([0, 1, 2, 3, 4, 5],
               [1, 5, 2, 3, 0, 4, 6, 7],
               [1, 2, 0, 0, 2, 1, 0, 0],
               [4, 8, 2, 3, 1, 5, 6, 7, 0, 9, 10, 11],
               [1, 1, 0, 0, 1, 0, 0, 0, 1, 0,  0,  0]),

    'M': Cube([3, 0, 2, 5, 4, 1],
               [0, 1, 2, 3, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 8, 5, 4, 7, 10, 9, 6, 11],
               [0, 0, 0, 0, 1, 0, 1, 0,  1, 0, 1,  0]),

    'E': Cube([0, 4, 1, 2, 3, 5],
               [0, 1, 2, 3, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11],
               [1, 1, 1, 1, 0, 0, 0, 0, 0, 0,  0,  0]),

    'S': Cube([4, 1, 0, 3, 5, 2],
               [0, 1, 2, 3, 4, 5, 6, 7],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 2, 3, 4, 7, 6, 11, 8, 5, 10, 9],
               [0, 0, 0, 0, 0, 1, 0,  1, 0, 1,  0, 1]),
               }

cube = Cube.solved()

moves["Uw"] = cube.apply_moves("U E E E")
moves["Fw"] = cube.apply_moves("F S")
moves["Rw"] = cube.apply_moves("R M M M")
moves["Dw"] = cube.apply_moves("D E")
moves["Bw"] = cube.apply_moves("B S S S")
moves["Lw"] = cube.apply_moves("L M")

move_names = []
faces = list(moves.keys())

for face_name in faces:
    move_names += [face_name, face_name + '2', face_name + '\'']
    moves[face_name + '2'] = moves[face_name].apply_move(moves[face_name])
    moves[face_name + '\''] = moves[face_name + '2'].apply_move(moves[face_name])

moves["sexy_move"] = cube.apply_moves("R U R' U'")
moves["sune"] = cube.apply_moves("R U R' U R U2 R'")
moves["anti_sune"] = cube.apply_moves("R U2 R' U' R U' R'")

moves["PLL-Aa"] = cube.apply_moves("x' R2 D2 R' U' R D2 R' U R' x")
moves["PLL-Ab"] = cube.apply_moves("x' R U' R D2 R' U R D2 R2 x")
moves["PLL-F"] = cube.apply_moves("R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R")
moves["PLL-Ga"] = cube.apply_moves("R2 U R' U R' U' R U' R2 U' D R' U R D' U")
moves["PLL-Gb"] = cube.apply_moves("F' U' F R2 Uw R' U R U' R Uw' R2")
moves["PLL-Gc"] = cube.apply_moves("R2 F2 R U2 R U2 R' F R U R' U' R' F R2")
moves["PLL-Gd"] = cube.apply_moves("R2 F' R U R U' R' F' R U2 R' U2 R' F2 R2")
moves["PLL-Ja"] = cube.apply_moves("L U' R' U L' U2 R U' R' U2 R")
moves["PLL-Jb"] = cube.apply_moves("R U R' F' R U R' U' R' F R2 U' R' U'")
moves["PLL-Ra"] = cube.apply_moves("R U' R' U' R U R D R' U' R D' R' U2 R' U'")
moves["PLL-Rb"] = cube.apply_moves("R' U2 R U2 R' F R U R' U' R' F' R2 U'")
moves["PLL-T"] = cube.apply_moves("R U R' U' R' F R2 U' R' U' R U R' F'")
moves["PLL-E"] = cube.apply_moves("x' R U' R' D R U R' D' R U R' D R U' R' D' x")
moves["PLL-Na"] = cube.apply_moves("R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R'")
moves["PLL-Nb"] = cube.apply_moves("R' U R U' R' F' U' F R U R' F R' F' R U' R")
moves["PLL-V"] = cube.apply_moves("R' U R U' R' Fw' U' R U2 R' U' R U' R' Fw R")
moves["PLL-Y"] = cube.apply_moves("F R U' R' U' R U R' F' R U R' U' R' F R F'")
moves["PLL-H"] = cube.apply_moves("M2 U M2 U2 M2 U M2")
moves["PLL-Ua"] = cube.apply_moves("R U' R U R U R U' R' U' R2")
moves["PLL-Ub"] = cube.apply_moves("R2 U R U R' U' R' U' R' U R'")
moves["PLL-Z"] = cube.apply_moves("U' M' U M2 U M2 U M' U2 M2")
