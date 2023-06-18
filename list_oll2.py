import csv
import cube

solved_cube = cube.Cube.solved()

with open('oll2.csv', 'w') as f:
    writer = csv.writer(f)

    for i in range(len(cube.oll_notes)):
        if i == 0:
            state = solved_cube
        else:
            state = solved_cube.apply_moves("OLL-" + str(i) + "'")

        for j in range(4):
            row = []

            if j == 0:
                row.append(str(i))
            elif j == 1:
                row.append(str(i) + "_U")
            elif j == 2:
                row.append(str(i) + "_U2")
            else:
                row.append(str(i) + "_U'")

            for k in range(1, len(cube.oll_notes)):
                s = state.apply_moves("OLL-" + str(k))
                name = s.get_oll_name()
                row.append(name)

            print(row)
            writer.writerow(row)
            state = state.apply_moves("U")
