def maze(m, n, route, pos, export):
    '''

    :param m: 迷宫数组，列表形式
    :param n: 迷宫阶数
    :param route: 可能的路线，列表
    :param pos: 当前位置，元组
    :param export: 出口，元组
    :return:
    '''
    route.append(pos)
    if pos == export:
        print(route)
    if pos[0] > 0 and m[pos[0] - 1][pos[1]] == 0 and (pos[0] - 1, pos[1]) not in route:
        maze(m, n, route[:], (pos[0] - 1, pos[1]), export)
    if pos[0] < n - 1 and m[pos[0] + 1][pos[1]] == 0 and (pos[0] + 1, pos[1]) not in route:
        maze(m, n, route[:], (pos[0] + 1, pos[1]), export)
    if pos[1] > 0 and m[pos[0]][pos[1] - 1] == 0 and (pos[0], pos[1] - 1) not in route:
        maze(m, n, route[:], (pos[0], pos[1] - 1), export)
    if pos[1] < n - 1 and m[pos[0]][pos[1] + 1] == 0 and (pos[0], pos[1] + 1) not in route:
        maze(m, n, route[:], (pos[0], pos[1] + 1), export)


m = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, ],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, ],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, ],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, ],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, ],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, ],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, ],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, ],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, ],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
]
maze(m, len(m), list(), (0, 3), (7, 9))
