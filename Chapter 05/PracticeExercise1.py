#Chess dictionary validator

chessboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessboard(board):
    letters = ['a', 'b', 'c', 'e', 'f', 'g', 'h']
    colours = ['b', 'w']
    pieces = ['pawn','knight','bishop','rook','queen','king']
    white_pieces = 0
    black_pieces = 0
    for p, s in chessboard.items():
        if int(p[0]) >= 9:
            print('Invalid space')
            return False
        if p[1] not in letters:
            print('Invalid space')
            return False
        if s[0] not in colours:
            print('Invalid piece.')
            return False
        if s[1:] not in pieces:
            print('Invalid piece')
            return False
        if s[0] == 'w':
            white_pieces += 1
        if s[0] == 'b':
            black_pieces += 1
    if white_pieces > 16:
        print('Invalid number of white pieces.')
    if black_pieces > 16:
        print('Invalid number of black pieces.')
    return print('Board is OK')

isValidChessboard(chessboard)