# Print function used to visualise the input and output:
def print_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print('{:>4}'.format(array[i][j]), end='')
        print()

    print()

# Helper function used to create the input based in the size of n and the index of the fan
def generate_input(size, index):
    array = []
    for i in range(size):
        r = []
        for j in range(size):
            r.append(1)
        array.append(r)

    row = index // size
    col = index % size

    array[row][col] = 0

    print("Input:")
    print_array(array)
    return array


# Places an L-Shaped tile at the 3 coordinates given
def place_l(x1, y1, x2, y2, x3, y3):
    global tile_count
    tile_count+=1
    array[x1][y1] = tile_count
    array[x2][y2] = tile_count
    array[x3][y3] = tile_count


# Recursively places L-shaped tiles until the ceiling is covered
def tile_recurse(n, row_offset, col_offset, fan_row, fan_col):
    global tile_count

    # Base case:
    if (n==2):
        tile_count+=1
        if (row_offset != fan_row or col_offset != fan_col):
            array[row_offset][col_offset] = tile_count
        if (row_offset != fan_row or col_offset + 1 != fan_col):
            array[row_offset][col_offset + 1] = tile_count
        if (row_offset + 1 != fan_row or col_offset != fan_col):
            array[row_offset + 1][col_offset] = tile_count
        if (row_offset + 1 != fan_row or col_offset + 1 != fan_col):
            array[row_offset + 1][col_offset + 1] = tile_count
        return

    # placing the tile that has one square in each quadrant:
    upper_row = row_offset + int(n/2) -1
    lower_row = row_offset + int(n/2)
    right_col = col_offset + int(n/2)
    left_col = col_offset + int(n/2) - 1

    # if fan is in q0:
    if (fan_row < row_offset + n/2 and fan_col < col_offset + n/2):
        place_l(upper_row, right_col, lower_row, left_col, lower_row, right_col)

        tile_recurse(int(n / 2), row_offset, col_offset, fan_row, fan_col)
        tile_recurse(int(n / 2), row_offset, col_offset + int(n / 2), row_offset + int(n/2) - 1, col_offset + int(n / 2))
        tile_recurse(int(n / 2), row_offset + int(n / 2), col_offset, row_offset + int(n/2), col_offset + int(n/2) -1)
        tile_recurse(int(n / 2), row_offset + int(n / 2), col_offset + int(n / 2), row_offset + int(n/2), col_offset + int(n/2))

    # if fan is in q1
    elif (fan_row < row_offset + n / 2 and fan_col >= col_offset + n / 2):
        place_l(upper_row, left_col, lower_row, left_col, lower_row, right_col)

        tile_recurse(int(n / 2), row_offset, col_offset, row_offset + int(n/2) -1, col_offset + int(n/2 - 1))
        tile_recurse(int(n / 2), row_offset, col_offset + int(n / 2), fan_row, fan_col)
        tile_recurse(int(n / 2), row_offset + int(n / 2), col_offset, row_offset + int(n / 2), col_offset + int(n / 2) - 1)
        tile_recurse(int(n / 2), row_offset + int(n / 2), col_offset + int(n / 2), row_offset + int(n / 2), col_offset + int(n / 2))

    # if fan is in q2
    elif (fan_row >= row_offset + n / 2 and fan_col < col_offset + n / 2):
        place_l(upper_row, left_col, upper_row, right_col, lower_row, right_col)

        tile_recurse(int(n / 2), row_offset, col_offset, row_offset + int(n / 2) - 1, col_offset + int(n / 2 - 1))
        tile_recurse(int(n / 2), row_offset, col_offset + int(n / 2), row_offset + int(n / 2) - 1, col_offset + int(n / 2))
        tile_recurse(int(n / 2), row_offset + int(n / 2), col_offset, fan_row, fan_col)
        tile_recurse(int(n / 2), row_offset + int(n / 2), col_offset + int(n / 2), row_offset + int(n / 2), col_offset + int(n / 2))

    # if fan is in q3
    else:
        place_l(upper_row, left_col, upper_row, right_col, lower_row, left_col)

        tile_recurse(int(n / 2), row_offset, col_offset, row_offset + int(n / 2) - 1, col_offset + int(n / 2 - 1))
        tile_recurse(int(n / 2), row_offset, col_offset + int(n / 2), row_offset + int(n / 2) - 1, col_offset + int(n / 2))
        tile_recurse(int(n / 2), row_offset + int(n / 2), col_offset, row_offset + int(n / 2), col_offset + int(n / 2) - 1)
        tile_recurse(int(n / 2), row_offset + int(n / 2), col_offset + int(n / 2), fan_row, fan_col)
    return




# main
if __name__ == '__main__':
    size = int(input())
    index = int(input())
    array = generate_input(size, index)

    tile_count = 0
    tile_recurse(len(array), 0, 0, int(index / size), index % size)

    print("Output:")
    print_array(array)



































