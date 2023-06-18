import cube
import draw

solved_cube = cube.Cube.solved()

# あるOLLに到達するOLLの番号を表示する

pattern = [[] for i in range(58)]

for i in range(1, len(cube.oll_notes)):
    state = solved_cube.apply_moves("OLL-" + str(i))
    num = state.get_oll_number()
    pattern[num].append(i)

for i in range(1, len(cube.oll_notes)):
    print(i, pattern[i])

# OLLを繰り返したときのサイクルを表示する
print("\n\n\n")

for i in range(1, len(cube.oll_notes)):
    print(str(i) + ": ", end="")
    mv = solved_cube.apply_moves("OLL-" + str(i))
    state = mv

    p = state.get_up_pattern()
    while p != [1, 1, 1, 1, 1, 1, 1, 1]:
        num = state.get_oll_number()
        print(" " + str(num), end="")

        state = state.apply_move(mv)
        p = state.get_up_pattern()

    print()

# 組み合わせてOLLに到着するものを探す
print("\n\n\n")

base_oll = 45

mvs = []
mv0 = solved_cube.apply_moves("OLL-" + str(base_oll))
mvs.append(mv0)
mvs.append(mv0.apply_moves("U"))
mvs.append(mv0.apply_moves("U2"))
mvs.append(mv0.apply_moves("U'"))

mvs2 = []
mvs2.append(solved_cube.apply_moves("OLL-" + str(base_oll)))
mvs2.append(solved_cube.apply_moves("U OLL-" + str(base_oll)))
mvs2.append(solved_cube.apply_moves("U2 OLL-" + str(base_oll)))
mvs2.append(solved_cube.apply_moves("U' OLL-" + str(base_oll)))

u_str = ["", "U ", "U2 ", "U' "]

p2 = [[] for i in range(len(cube.oll_notes))]

for i in range(1, len(cube.oll_notes)):
    for k in range(4):
        state = mvs[k].apply_moves("OLL-" + str(i))
        num = state.get_oll_number()

        if len(pattern[num]) == 0:
            p2[num].append(str(base_oll) + " " + u_str[k] + str(i))

    cur_oll = solved_cube.apply_moves("OLL-" + str(i))
    for k in range(4):
        state = cur_oll.apply_move(mvs2[k])
        num = state.get_oll_number()

        if len(pattern[num]) == 0:
            p2[num].append(str(i) + " " + u_str[k] + str(base_oll))

for i in range(1, len(cube.oll_notes)):
    if len(p2[i]):
        print(i, p2[i])
