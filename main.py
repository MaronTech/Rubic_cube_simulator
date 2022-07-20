from classes import Wall, Cube

walls = []
colours = ['white', 'green', 'yellow', 'blue', 'orange', 'red']
for colour in colours:
    col = []
    for i in range(9):
        col.append(colour)
    w = Wall(col)
    walls.append(w)
c1 = Cube(walls)
# print(c1.show_grid_of_cube())
print("----------------------")
c1.move_f_prim()
c1.move_r()
c1.move_u_prim()
# c1.move_f()
# c1.move_r_prim()
print(c1.show_grid_of_cube())
