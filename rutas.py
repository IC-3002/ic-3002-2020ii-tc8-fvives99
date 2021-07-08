import copy

def is_empty(data_structure):
    if data_structure:
        return False
    else:
        return True

def create_answer_matrix(n, y):
    answer_matrix = []
    for i in range(n):
        answer_matrix.append([])
        for j in range(y):
            answer_matrix[i].append(0)
    return answer_matrix

#Mismas funciones de la tarea 7#

def right(partial_answer, matrix, target_row, target_column):
    limt_matrix = len(matrix[0])
    if target_column == limt_matrix:
        target_column -= 1
        return False

    if (matrix[target_row][target_column] == 0 and partial_answer[target_row][target_column] == 0):
        return True

    return False

def down(partial_answer, matrix, target_row, target_column):
    limt_matrix = len(matrix)
    if target_row == limt_matrix:
        target_row -= 1
        return False

    if (matrix[target_row][target_column] == 0 and partial_answer[target_row][target_column] == 0):
        return True

    return False

def move_right(matrix, actual_row, actual_column, target_row, target_column, partial_answer, answer):
    if right(partial_answer, matrix, target_row, target_column) == True:
        partial_answer[actual_row][actual_column] = 1
        matrix_traking(answer, partial_answer, matrix, target_row, target_column)
        partial_answer[actual_row][actual_column] = 0
        return


def move_down(matrix, actual_row, actual_column, target_row, target_column, partial_answer, answer):
    if down(partial_answer, matrix, target_row, target_column) == True:
        partial_answer[actual_row][actual_column] = 1
        matrix_traking(answer, partial_answer, matrix, target_row, target_column)
        partial_answer[actual_row][actual_column] = 0
        return

def matrix_traking(answer, partial_answer, matrix, row, column):
    n = len(matrix)
    y = len(matrix[0])

    if n - 1 == row and y - 1 == column:
        if matrix[row][column] == 0:
            partial_answer[row][column] = 1
            ans = copy.deepcopy(partial_answer)
            answer.append(ans)
            partial_answer[row][column] = 0

    else:
        movimientos = [[0, 0, 1], [1, 1, 0]]
        for i in movimientos:
            target_row = row + i[1]
            target_column = column + i[2]

            moves = [move_right, move_down]
            next_move = moves[i[0]]
            next_move(matrix, row, column, target_row, target_column, partial_answer, answer)

def print_matrix(matrix):
    x = len(matrix)
    for i in range(0, x):
        print("\nSolucion #" + str(i))
        for x in range(0, len(matrix[i])):
            print(matrix[i][x])


def contar_rutas_mas_cortas(C):
    x_de_inicio = 0
    y_de_inicio = 0
    n = len(C)
    y = len(C[0])

    answer = []

    partial_answer = create_answer_matrix(n, y)

    matrix_traking(answer, partial_answer, C, y_de_inicio, x_de_inicio)
    return len(answer)

