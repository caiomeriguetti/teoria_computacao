a = [[1, 3],
     [5, 6]]

b = [[1, 2],
     [3, 4]]


def multi(x, y):
    lines_x = len(x)
    cols_y = len(y[0])

    result = [[None for k in range(lines_x)] for t in range(cols_y)]

    for line in range(0, lines_x):
        for col in range(0, cols_y):

            sum_buffer = 0
            str_buffer = ''
            for col_y, line_elem in enumerate(x[line]):
                col_elem = y[col_y][col]
                sum_buffer += line_elem * col_elem

            result[line][col] = sum_buffer

    print result

multi(a, b)
