# > Окруженные острова
# Вам дан массив board размера m x n, содержащий 'X' (вода) и 'O' (остров).
# Ваша задача — затопить все острова, окруженные с четырех сторон водой (т.е. все 'O', окруженные с четырех сторон 'X').
# Все буквы X и O английские. Чтобы затопить остров, нужно все его 'O' превратить в 'X'.
# Во втором примере затопления не произошло потому, что 'O' в центре соединены с 'O' с краю — и следовательно, не окружены водой.
# Напишите функцию drown(board), принимающую на вход поле и возвращающее поле после затопления.

def drown(board):
    if not board:
        return board

    m, n = len(board), len(board[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = 'D' # Помечайем остров как затопленный
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    # Обрабатываем края поля
    for i in range(m):
        dfs(i, 0)
        dfs(i, n-1)

    for j in range(n):
        dfs(0, j)
        dfs(m-1, j)

    # Заменяем "О" на "Х" и "D" на "О"
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'D':
                board[i][j] = 'O'

    return board

if __name__ == '__main__':

    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    result_board = drown(board)
    for row in result_board:
        print(row)