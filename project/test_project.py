from project import create_game_map, isFull, insert_in_column

def test_create_game_map():
    assert create_game_map(3)==[[".",".","."],[".",".","."],[".",".","."]]
    assert create_game_map(4)==[[".",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]

def test_isFull():
    assert isFull([[".", ".", "."], [".", ".", "."], [".", ".", "."]]) == False
    assert isFull([["X", "O", "."], [".", ".", "."], [".", ".", "."]]) == False
    assert isFull([["X", "O", "X"], [".", ".", "."], [".", ".", "."]]) == True

def test_insert_in_column():
    assert insert_in_column([[".", ".", "."], [".", ".", "."], [".", ".", "."]],0,"X") == True
    assert insert_in_column([["X", ".", "."], ["X", ".", "."], [
                            "0", ".", "."]], 0, "X") == False
    assert insert_in_column([[".", ".", "."], ["X", ".", "."], [
                            "0", ".", "."]], 0, "X") == True

