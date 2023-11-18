def tetris ():
    """Board inicialization

    Returns:
        [list[list[str]]]: Return a tetris board as a list of string lists
    """
    board = [
        ["-", "X", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "X", "X", "X", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ]
    
    return board
    

def print_board (board):
    """Print the board without brackets and with spaces

    Args:
        board (list[list[str]]): Board from list of string lists
    """
    for rows in board:
        print('    '.join(rows))
        
        
def mov_left (board):
    #Variable to know if the movement is possible  
    space_left = None
    #Variable to know if the loop find the first x
    found_x = False
    
    #Check for sufficient space on the left
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "X":
                if j - 0 >= 0 :
                    found_x = True
                    space_left = True
                    break
                else:
                    print("Not Space")
                    space_left = False
        if found_x:
            break
    if not found_x:
        print("Not found")
        
     #List of coordinates                 
    coord = []

    #Loop for know the coordinates of the X
    if space_left:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "X":
                    coord.append(i)
                    coord.append(j)
    print(coord)
    
    #List of coordenates plus a space to the left
    coord_moved = []
    
    for coords in range(0, len(coord)):
        # The row are kept, only moved in the column position
        if coords % 2 != 0:
            coord_moved.append(coord[coords] -1)
        else:
            coord_moved.append(coord[coords])
    print(coord_moved)

    #Clean the board before print the nex positions
    clean_board(board)
    #Ubicate the figure in the board
    for i in range(0, len(coord_moved), 2):
        row = coord_moved[i]
        column = coord_moved[i+1]
        #board[row][column] = "X"

    
    # List of coordinates plus one position to the left
    
    
    
        #for moved_coords in moved_coord:
        #row = moved_coords // 9
        #columns = moved_coords % 9
        #board[row][columns] = "X"
    
    
                    
    
               
    
                
                
            
                           
    
    

def clean_board (board):
    """Clean the board

    Args:
        board (List of String lists): Tetris board
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "X":
                board[i][j] == "-"
                 
    
    
    

        
        

if __name__  == "__main__":
    
    board = tetris()
    print_board(board)
    mov_left(board)
    clean_board(board)
    print_board(board)
