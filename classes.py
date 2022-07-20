from functions import (
    walls_configuration,
    sort_walls,
    normal_movement
)


class Cube:
    def __init__(self, walls):
        self._walls = walls_configuration(sort_walls(walls))

    def change_walls(self, changed_walls):
        self._walls = changed_walls

    # This metod is gonna to return full algoritm to solve a cube
    def solve(self):
        pass

    def show_grid_of_cube(self):
        i = 0
        all_cube = ''
        for colour in self.walls():
            if i % 3 == 0:
                all_cube = all_cube + '\n '
                if i % 9 == 0:
                   all_cube = all_cube + '\n '
            all_cube = all_cube + colour[0] + " "
            i = i + 1
        return all_cube

    def walls(self):
        return self._walls

    # finished
    def move_u(self):
        # 12 elements changing linear
        linear_chnage = [
            36, 37, 38, 9, 10, 11, 45, 46, 47, 33, 34, 35
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            0, 3, 6, 7, 8, 5, 2, 1
        ]
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_f(self):
        # 12 elements changing linear
        linear_chnage = [
            8, 7, 6, 38, 41, 44, 18, 19, 20, 51, 48, 45
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            9, 12, 15, 16, 17, 14, 11, 10
        ]
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_d(self):
        # 12 elements changing linear
        linear_chnage = [
            53, 52, 51, 17, 16, 15, 44, 43, 42, 29, 28, 27
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            18, 21, 24, 25, 26, 23, 20, 19
        ]
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_l(self):
        # 12 elements changing linear
        linear_chnage = [
            33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            36, 39, 42, 43, 44, 41, 38, 37
        ]
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_r(self):
        # 12 elements changing linear
        linear_chnage = [
            2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            45, 48, 51, 52, 53, 50, 47, 46
        ]
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_b(self):
        # 12 elements changing linear
        linear_chnage = [
            0, 1, 2, 47, 50, 52, 26, 25, 24, 42, 39, 36
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            27, 28, 29, 32, 35, 34, 33, 30
        ]
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_m(self):
        pass

    def move_m_prim():
        pass

    def move_u_prim(self):
        # 12 elements changing linear
        linear_chnage = [
            36, 37, 38, 9, 10, 11, 45, 46, 47, 33, 34, 35
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            0, 3, 6, 7, 8, 5, 2, 1
        ]
        linear_chnage.reverse()
        rotation_change.reverse()
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_f_prim(self):
        # 12 elements changing linear
        linear_chnage = [
            8, 7, 6, 38, 41, 44, 18, 19, 20, 51, 48, 45
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            9, 12, 15, 16, 17, 14, 11, 10
        ]
        linear_chnage.reverse()
        rotation_change.reverse()
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_d_prim(self):
        # 12 elements changing linear
        linear_chnage = [
            53, 52, 51, 17, 16, 15, 44, 43, 42, 29, 28, 27
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            18, 21, 24, 25, 26, 23, 20, 19
        ]
        linear_chnage.reverse()
        rotation_change.reverse()
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_l_prim(self):
        # 12 elements changing linear
        linear_chnage = [
            33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            36, 39, 42, 43, 44, 41, 38, 37
        ]
        linear_chnage.reverse()
        rotation_change.reverse()
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_r_prim(self):
        # 12 elements changing linear
        linear_chnage = [
            2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            45, 48, 51, 52, 53, 50, 47, 46
        ]
        linear_chnage.reverse()
        rotation_change.reverse()
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_b_prim(self):
        # 12 elements changing linear
        linear_chnage = [
            0, 1, 2, 47, 50, 52, 26, 25, 24, 42, 39, 36
        ]
        # 8 elements changing on the rotation wall
        rotation_change = [
            27, 28, 29, 32, 35, 34, 33, 30
        ]
        linear_chnage.reverse()
        rotation_change.reverse()
        self._walls = normal_movement(self, linear_chnage, rotation_change)

    def move_u2():
        pass

    def move_f2():
        pass

    def move_d2():
        pass

    def move_l2():
        pass

    def move_r2():
        pass

    def move_b2():
        pass


class Wall:
    def __init__(self, colours):
        self._wall_colours = colours
        # get_type_of_wall function gives possibility to set a type of
        # wall(front(green), up(white), etc..)
        self._type_of_wall = colours[4]
    # This method give possibility to chnage at least one colour in the wall

    def change_colour_on_possition(self, new_colour, possition):
        self._colour[possition] = new_colour

    def colours(self):
        return self._wall_colours

    def type_of_wall(self):
        return self._type_of_wall
