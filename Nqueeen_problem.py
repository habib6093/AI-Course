def show(board):
    for i in board:
        print(i)
        

def initialize_board(dimension):
    temp_list=[]
    for i in range(dimension):
        temp_list.append([0]*dimension)
        
    return temp_list


def initialize(dimension):
    return [0]*(dimension+dimension+2) #extra position added




def solve_nqueen(column,left,right,at,board,counter):
    if(at>=dimension):
      show(board)
      print("counter is: ",counter)
      print("\n")
      return

    for i in range(dimension):
        if column[i]==0 and right[at-i+dimension]==0 and left[at+i]==0:
            column[i]=1
            right[at-i+dimension]= 1
            left[at+i]= 1
            board[at][i]=1
            
            solve_nqueen(column,left,right,at+1,board)

            column[i]=0
            right[at-i+dimension]= 0
            left[at+i]= 0
            board[at][i]=0
           
    return



def nqueen(dimension):
    column=initialize(dimension)
    left=initialize(dimension)
    right=initialize(dimension)
    board=initialize_board(dimension)
    solve_nqueen(column,left,right,0,board,0)
   


dimension=5
nqueen(dimension)




