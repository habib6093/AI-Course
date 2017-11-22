count=0

def nqueen(at,board,dimension):


   if(at==dimension):
       print("result is: ",board[0:dimension])
       global count
       count=count+1
       return


   for i in range(dimension):

           if(at==0):
               board[at]=i
               nqueen(at+1,board,dimension)
               board[at]=-1
    
         
           for j in range(at):
               temp=abs(board[j]-i)
               temp2=abs(j-at)

               if(temp==temp2 or board[j]==i ):    
                   break
                
               if(j==(at-1)):
                   board[at]=i
                   nqueen(at+1,board,dimension)
                   board[at]=-1
                   

           

def solve_nqueen(dimension):
    board=[0]*(dimension+2)
    for i in range(dimension+1):
        board[i]=-1
        
    nqueen(0,board,dimension)




dimension=7
solve_nqueen(dimension)
print(count)



