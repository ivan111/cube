import cube
import draw

solved_cube = cube.Cube.solved()

# あるPLLに到達するPLLの番号を表示する

pattern = {}

for name in cube.pll_names:
    pattern[name] = []

for name in cube.pll_names:
    state = solved_cube.apply_moves(name)
    target_name = state.get_pll_name()
    pattern[target_name].append(name)

for name in cube.pll_names:
    print(name, pattern[name])

# PLLを繰り返したときのサイクルを表示する
print("\n\n\n")

for name in cube.pll_names:
    print(name + ":", end="")
    mv = solved_cube.apply_moves(name)
    state = mv

    t_name = state.get_pll_name()
    while t_name != name:
        print(" " + t_name, end="")

        state = state.apply_move(mv)
        t_name = state.get_pll_name()

    print()
