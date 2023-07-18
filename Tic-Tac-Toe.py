def sum(a, b, c ):
    return a + b + c

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"\t\t{zero} | {one} | {two} ")
    print(f"\t\t--|---|---")
    print(f"\t\t{three} | {four} | {five} ")
    print(f"\t\t--|---|---")
    print(f"\t\t{six} | {seven} | {eight} ") 

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("\n\t\t\t\t*****X Won the match*****")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("\n\t\t\t\t*****O Won the match*****")
            return 0
    return -1
    
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("\n\t\t\t*****Welcome to Tic Tac Toe*****\n")
    print("\nInstructions : -\n \n\t1.Two Players needed to play game \n\n\t2. first player has X mark and another has O mark.\n\n\t3. Players take turns putting their marks in empty squares.\n\n\t 4. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n\n\t5.  When all 9 squares are full, the game is over. \n\n\t6. If no player has 3 marks in a row, the game ends in a tie. \n\n")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("\n\tX's Turns - ")
            value = int(input("\n\tPlease enter a value : "))
            xState[value] = 1
        else:
            print("\n\tO's Turns - ")
            value = int(input("\n\tPlease enter a value : "))
            zState[value] = 1
        cwin = checkWin(xState, zState)
        if(cwin != -1):
            print("\n\t\t\t\t\t----Match over----\n\n")
            break
        
        turn = 1 - turn