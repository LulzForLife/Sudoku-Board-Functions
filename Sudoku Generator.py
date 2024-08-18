def board_to_matrix(board):
    matrix = []
    for l in range(3):
        for i in range(3):
            temp = dict()
            for j in range(3):
                for k in range(3):
                    temp[(k + (j * 9)) + (i * 3) + (l * 18)] = board[(k + (j * 9)) + (i * 3) + (l * 18)]
            matrix.append(temp)
    return matrix

def board_to_rows(board):
    rows = []
    for i in range(9):
        temp = dict()
        for j in range(9):
            temp[j + (i * 9)] = board[j + (i * 9)]
        rows.append(temp)
    return rows

def board_to_columns(board):
    columns = []
    for i in range(9):
        temp = dict()
        for j in range(9):
            temp[i + (j * 9)] = board[i + (j * 9)]
        columns.append(temp)
    return columns

def get_possible_values(board, cell_id):
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    matrix = board_to_matrix(board)
    for dic in matrix:
        if cell_id in dic.keys():
            for key in dic:
                if dic[key] in values:
                    values.remove(dic[key])
        else:
            continue
    
    rows = board_to_rows(board)
    for dic in rows:
        if cell_id in dic.keys():
            for key in dic:
                if dic[key] in values:
                    values.remove(dic[key])
        else:
            continue
    
    columns = board_to_columns(board)
    for dic in columns:
        if cell_id in dic.keys():
            for key in dic:
                if dic[key] in values:
                    values.remove(dic[key])
        else:
            continue
    
    return values

board = []

board = [0 for _ in range(81)]

board[1] = 3
board[3] = 7
board[27] = 5
'''
for _ in range(9):
    for i in range(9):
        board.append(i + 1)
'''
print(board)
print(get_possible_values(board, 0))