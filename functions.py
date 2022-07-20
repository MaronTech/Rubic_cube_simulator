import copy


def sort_walls(walls):
    sorted_walls = []
    colours = ['white', 'green', 'yellow', 'blue', 'orange', 'red']
    for colour in colours:
        for wall in walls:
            if wall.type_of_wall() == colour:
                sorted_walls.append(wall)
    return sorted_walls


def normal_movement(object, linear, rotation):
    changed_cube = copy.deepcopy(object.walls())
    change_linear = linear[-3:] + linear
    change_rotation = rotation + rotation[: 2]
    for i in range(3, 15):
        changed_cube[change_linear[i - 3]] = object.walls()[change_linear[i]]
    for j in range(2, 10):
        changed_cube[change_rotation[j - 2]] = object.walls()[change_rotation[j]]
    return changed_cube


def prim_movement(object, linear, rotation):
    pass


def twice_movement(object, linear, rotation):
    pass


def get_type_of_wall(colours):
    if colours[4] == 'white':
        return 'white'

    elif colours[4] == 'green':
        return 'green'

    elif colours[4] == 'yellow':
        return 'yellow'

    elif colours[4] == 'blue':
        return 'blue'

    elif colours[4] == 'orange':
        return 'orange'

    elif colours[4] == 'red':
        return 'red'


def walls_configuration(walls):
    walls_configuration = []
    for wall in walls:
        for colour in wall.colours():
            walls_configuration.append(colour)
    return walls_configuration
