import csv
import cube

solved_cube = cube.Cube.solved()

with open('oll.csv', 'w') as f:
    writer = csv.writer(f)

    for i in range(len(cube.oll_notes)):
        if i == 0:
            state = solved_cube
        else:
            state = solved_cube.apply_moves("OLL-" + str(i) + "'")

        for j in range(4):
            row = [i, j]

            for k in range(1, len(cube.oll_notes)):
                s = state.apply_moves("OLL-" + str(k))
                num = s.get_oll_number()
                row.append(num)

            print(row)
            writer.writerow(row)
            state = state.apply_moves("U")
