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

    def __repr__(self):
        return ', '.join(["op=" + str(self.op), "cp=" + str(self.cp), "co=" + str(self.co), "ep=" + str(self.ep), "eo=" + str(self.eo)])

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

    def __eq__(self, other):
        return (self.op == other.op and
            self.cp == other.cp and
            self.co == other.co and
            self.ep == other.ep and
            self.eo == other.eo)

    def get_up_pattern(self):
        # corner 0, 1, 2, 3 edge 4, 5, 6, 7
        # corner: 0 = up色なし, 1 = upがup色, 2 = upの時計周りの位置がup色, 3 = upの反時計周りの位置がup色
        # edge: 0 = up色なし, 1 = upがup色, 2 = upでない面がup色
        c = o_colors[self.op[0]] # up color

        p = []

        for i in range(4):
            res = 0
            for k in range(3):
                if c == c_colors[self.cp[i]][(self.co[i] + k) % 3]:
                    res = k + 1
                    break

            p.append(res)

        for i in range(4):
            res = 0
            for k in range(2):
                if c == e_colors[self.ep[i+4]][(self.eo[i+4] + k) % 2]:
                    res = k + 1
                    break

            p.append(res)

        return p

    # 上面の横側面のパターンを取得する
    def get_up_side_pattern(self):
        p1 = c_colors[self.cp[0]][(self.co[0] + 1) % 3]
        p2 = c_colors[self.cp[0]][(self.co[0] + 2) % 3]
        p3 = e_colors[self.ep[4]][(self.eo[4] + 1) % 2]
        p4 = c_colors[self.cp[1]][(self.co[1] + 1) % 3]
        p5 = c_colors[self.cp[1]][(self.co[1] + 2) % 3]
        p6 = e_colors[self.ep[5]][(self.eo[5] + 1) % 2]
        p7 = c_colors[self.cp[2]][(self.co[2] + 1) % 3]
        p8 = c_colors[self.cp[2]][(self.co[2] + 2) % 3]
        p9 = e_colors[self.ep[6]][(self.eo[6] + 1) % 2]
        p10 = c_colors[self.cp[3]][(self.co[3] + 1) % 3]
        p11 = c_colors[self.cp[3]][(self.co[3] + 2) % 3]
        p12 = e_colors[self.ep[7]][(self.eo[7] + 1) % 2]

        return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]

    def get_oll_number(self):
        for i in range(1, len(oll_notes)):
            state = moves["OLL-" + str(i) + "'"]

            for k in range(4):
                if self.get_up_pattern() == state.get_up_pattern():
                    return i

                state = state.apply_moves("U")

        return 0

    def get_oll_name(self):
        for i in range(1, len(oll_notes)):
            state = moves["OLL-" + str(i) + "'"]

            for k in range(4):
                if self.get_up_pattern() == state.get_up_pattern():
                    if k == 0:
                        return str(i)
                    elif k == 1:
                        return str(i) + "_U"
                    elif k == 2:
                        return str(i) + "_U2"
                    else:
                        return str(i) + "_U'"

                state = state.apply_moves("U")

        return 0

    U_MAP = [0, 2, 3, 4, 1, 5]  # get_up_side_patternで取得した側面の色リストの色をUして、色を変える

    def get_pll_name(self):
        for name in pll_names:
            state = moves[name + "'"]

            for k in range(4):
                p = self.get_up_side_pattern()
                p1 = state.get_up_side_pattern()
                p2 = [self.U_MAP[p] for p in p1]
                p3 = [self.U_MAP[p] for p in p2]
                p4 = [self.U_MAP[p] for p in p3]

                if p == p1 or p == p2 or p == p3 or p == p4:
                    return name

                state = state.apply_moves("U")

        return ""

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


def get_prime_move(mv):
    solved_cube = Cube.solved()

    state0 = solved_cube.apply_move(mv)
    state = state0
    prev = state0

    while solved_cube != state:
        prev = state
        state = state.apply_move(mv)

    return prev

move_names = []
faces = list(moves.keys())

for face_name in faces:
    move_names += [face_name, face_name + '2', face_name + '\'']
    moves[face_name + '2'] = moves[face_name].apply_move(moves[face_name])
    moves[face_name + '\''] = moves[face_name + '2'].apply_move(moves[face_name])

moves["sexy_move"] = cube.apply_moves("R U R' U'")
moves["sune"] = cube.apply_moves("R U R' U R U2 R'")
moves["anti_sune"] = cube.apply_moves("R U2 R' U' R U' R'")

pll_names = ["PLL-Aa", "PLL-Ab", "PLL-F", "PLL-Ga", "PLL-Gb", "PLL-Gc", "PLL-Gd",
             "PLL-Ja", "PLL-Jb", "PLL-Ra", "PLL-Rb", "PLL-T", "PLL-E", "PLL-Na",
             "PLL-Nb", "PLL-V", "PLL-Y", "PLL-H", "PLL-Ua", "PLL-Ub", "PLL-Z"]

pll_notes = {}

pll_notes["PLL-Aa"] = "x' R2 D2 R' U' R D2 R' U R' x"
pll_notes["PLL-Ab"] = "x' R U' R D2 R' U R D2 R2 x"
pll_notes["PLL-F"] = "R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R"
pll_notes["PLL-Ga"] = "R2 U R' U R' U' R U' R2 U' D R' U R D' U"
pll_notes["PLL-Gb"] = "F' U' F R2 Uw R' U R U' R Uw' R2"
pll_notes["PLL-Gc"] = "R2 F2 R U2 R U2 R' F R U R' U' R' F R2"
pll_notes["PLL-Gd"] = "R2 F' R U R U' R' F' R U2 R' U2 R' F2 R2"
pll_notes["PLL-Ja"] = "L U' R' U L' U2 R U' R' U2 R"
pll_notes["PLL-Jb"] = "R U R' F' R U R' U' R' F R2 U' R' U'"
pll_notes["PLL-Ra"] = "R U' R' U' R U R D R' U' R D' R' U2 R' U'"
pll_notes["PLL-Rb"] = "R' U2 R U2 R' F R U R' U' R' F' R2 U'"
pll_notes["PLL-T"] = "R U R' U' R' F R2 U' R' U' R U R' F'"
pll_notes["PLL-E"] = "x' R U' R' D R U R' D' R U R' D R U' R' D' x"
pll_notes["PLL-Na"] = "R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R'"
pll_notes["PLL-Nb"] = "R' U R U' R' F' U' F R U R' F R' F' R U' R"
pll_notes["PLL-V"] = "R' U R U' R' Fw' U' R U2 R' U' R U' R' Fw R"
pll_notes["PLL-Y"] = "F R U' R' U' R U R' F' R U R' U' R' F R F'"
pll_notes["PLL-H"] = "M2 U M2 U2 M2 U M2"
pll_notes["PLL-Ua"] = "R U' R U R U R U' R' U' R2"
pll_notes["PLL-Ub"] = "R2 U R U R' U' R' U' R' U R'"
pll_notes["PLL-Z"] = "U' M' U M2 U M2 U M' U2 M2"

for name in pll_names:
    moves[name] = cube.apply_moves(pll_notes[name])

moves["PLL-Aa'"] = moves["PLL-Ab"]
moves["PLL-Ab'"] = moves["PLL-Aa"]
moves["PLL-F'"] = moves["PLL-F"]
moves["PLL-Ga'"] = moves["PLL-Gb"]
moves["PLL-Gb'"] = moves["PLL-Ga"]
moves["PLL-Gc'"] = moves["PLL-Gd"]
moves["PLL-Gd'"] = moves["PLL-Gc"]
moves["PLL-Ja'"] = moves["PLL-Ja"]
moves["PLL-Jb'"] = moves["PLL-Jb"]
moves["PLL-Ra'"] = moves["PLL-Ra"]
moves["PLL-Rb'"] = moves["PLL-Rb"]
moves["PLL-T'"] = moves["PLL-T"]
moves["PLL-E'"] = moves["PLL-E"]
moves["PLL-Na'"] = moves["PLL-Na"]
moves["PLL-Nb'"] = moves["PLL-Nb"]
moves["PLL-V'"] = moves["PLL-V"]
moves["PLL-Y'"] = moves["PLL-Y"]
moves["PLL-H'"] = moves["PLL-H"]
moves["PLL-Ua'"] = moves["PLL-Ub"]
moves["PLL-Ub'"] = moves["PLL-Ua"]
moves["PLL-Z'"] = moves["PLL-Z"]

oll_notes = [""] * 58

oll_notes[1] = "R U2 R2 F R F' U2 R' F R F'"
oll_notes[2] = "F R U R' U' F' Fw R U R' U' Fw'"
oll_notes[3] = "Fw R U R' U' Fw' U' F R U R' U' F'"
oll_notes[4] = "Fw R U R' U' Fw' U F R U R' U' F'"
oll_notes[5] = "Rw' U2 R U R' U Rw"
oll_notes[6] = "Rw U2 R' U' R U' Rw'"
oll_notes[7] = "Rw U R' U R U2 Rw'"
oll_notes[8] = "Rw' U' R U' R' U2 Rw"
oll_notes[9] = "R U R' U' R' F R2 U R' U' F'"
oll_notes[10] = "R U R' U R' F R F' R U2 R'"
oll_notes[11] = "Rw' R2 U R' U R U2 R' U M'"
oll_notes[12] = "F R U R' U' F' U F R U R' U' F'"
oll_notes[13] = "F U R U' R2 F' R U R U' R'"
oll_notes[14] = "Rw U R' U' Rw' F R2 U R' U' F'"
oll_notes[15] = "Rw' U' Rw R' U' R U Rw' U Rw"
oll_notes[16] = "Rw U Rw' R U R' U' Rw U' Rw'"
oll_notes[17] = "R U R' U R' F R F' U2 R' F R F'"
oll_notes[18] = "R U2 R2 F R F' U2 M' U R U' Rw'"
oll_notes[19] = "Rw' R U R U R' U' Rw R2 F R F'"
oll_notes[20] = "Rw' R U R U R' U' M2 U R U' Rw'"
oll_notes[21] = "R' U' R U' R' U R U' R' U2 R"
oll_notes[22] = "R U2 R2 U' R2 U' R2 U2 R"
oll_notes[23] = "R2 D R' U2 R D' R' U2 R'"
oll_notes[24] = "Rw U R' U' Rw' F R F'"
oll_notes[25] = "x U R' U' L U R U' Rw'"
oll_notes[26] = "L' U' L U' L' U2 L"
oll_notes[27] = "R U R' U R U2 R'"
oll_notes[28] = "Rw U R' U' Rw' R U R U' R'"
oll_notes[29] = "R' F R F' R U2 R' U' F' U' F"
oll_notes[30] = "F R' F R2 U' R' U' R U R' F2"
oll_notes[31] = "R' U' F U R U' R' F' R"
oll_notes[32] = "S R U R' U' R' F R Fw'"
oll_notes[33] = "R U R' U' R' F R F'"
oll_notes[34] = "R U R2 U' R' F R U R U' F'"
oll_notes[35] = "R U2 R2 F R F' R U2 R'"
oll_notes[36] = "R U R' U' F' U2 F U R U R'"
oll_notes[37] = "F R U' R' U' R U R' F'"
oll_notes[38] = "R U R' U R U' R' U' R' F R F'"
oll_notes[39] = "R U R' F' U' F U R U2 R'"
oll_notes[40] = "R' F R U R' U' F' U R"
oll_notes[41] = "R U R' U R U2 R' F R U R' U' F'"
oll_notes[42] = "R' U' R U' R' U2 R F R U R' U' F'"
oll_notes[43] = "R' U' F' U F R"
oll_notes[44] = "Fw R U R' U' Fw'"
oll_notes[45] = "F R U R' U' F'"
oll_notes[46] = "R' U' R' F R F' U R"
oll_notes[47] = "F' L' U' L U L' U' L U F"
oll_notes[48] = "F R U R' U' R U R' U' F'"
oll_notes[49] = "R B' R2 F R2 B R2 F' R"
oll_notes[50] = "Rw' U Rw2 U' Rw2 U' Rw2 U Rw'"
oll_notes[51] = "Fw R U R' U' R U R' U' Fw'"
oll_notes[52] = "R' F' U' F U' R U R' U R"
oll_notes[53] = "Rw' U' R U' R' U R U' R' U2 Rw"
oll_notes[54] = "Rw U R' U R U' R' U R U2 Rw'"
oll_notes[55] = "Rw U2 R2 F R F' U2 Rw' F R F'"
oll_notes[56] = "Rw' U' Rw U' R' U R U' R' U R Rw' U Rw"
oll_notes[57] = "R U R' U' M' U R U' Rw'"

for i in range(1, len(oll_notes)):
    moves["OLL-" + str(i)] = cube.apply_moves(oll_notes[i])
    moves["OLL-" + str(i) + "'"] = get_prime_move(moves["OLL-" + str(i)])
