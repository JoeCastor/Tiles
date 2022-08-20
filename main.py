def print_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print('{:>4}'.format(array[i][j]), end='')
        print()

    print()

def gen_input(size, index):
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
def place_tile(x1,y1,x2,y2,x3,y3):
    global tile_count
    tile_count+=1
    array[x1][y1] = tile_count
    array[x2][y2] = tile_count
    array[x3][y3] = tile_count

def tile(n, row_offset, col_offset):
    global tile_count
    row_of_fan = -1
    col_of_fan = -1

    # Base case:
    if (n==2):
        tile_count+=1
        for i in range(n):
            for j in range(n):
                if (array[row_offset+i][col_offset + j]==1):
                    array[row_offset + i][col_offset + j] = tile_count
        return

    for i in range(row_offset, row_offset + n):
        for j in range(col_offset, col_offset + n):
            if array[i][j]!=1:
                row_of_fan = i
                col_of_fan = j

    # placing the tile that has one square in each quadrant:
    upper_row = row_offset + int(n/2) -1
    lower_row = row_offset + int(n/2)
    right_col = col_offset + int(n/2)
    left_col = col_offset + int(n/2) - 1
    # q0
    if (row_of_fan < row_offset + n/2 and col_of_fan < col_offset + n/2):
        place_tile(upper_row, right_col, lower_row, left_col, lower_row, right_col)

    elif (row_of_fan < row_offset + n/2 and col_of_fan >= col_offset + n/2):
        place_tile(upper_row, left_col, lower_row, left_col, lower_row, right_col)

    elif (row_of_fan >= row_offset + n/2 and col_of_fan < col_offset + n/2):
        place_tile(upper_row, left_col, upper_row, right_col, lower_row, right_col)

    else:
        place_tile(upper_row, left_col, upper_row, right_col, lower_row, left_col)

    #Recursive calls to tile each quadrant:
    tile(int(n/2), row_offset, col_offset)
    tile(int(n/2), row_offset, col_offset + int(n/2))
    tile(int(n/2), row_offset + int(n/2), col_offset)
    tile(int(n/2), row_offset + int(n/2), col_offset + int(n/2))

    return

def  fix_first():
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j]==tile_count:
                array[i][j] = 1


if __name__ == '__main__':
    tile_count = 1
    for i in range(64):
        array =  gen_input(8, i)
        tile_count = 1
        tile(len(array), 0, 0)
        fix_first()
        print_array(array)



































