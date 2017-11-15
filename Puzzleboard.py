import random

##puzzle=[
##         [6,1,10,2],
##         [7,11,4,14],
##         [5,0,9,15],
##         [8,12,13,3]
##       ]

def blank_tile_row():
    for i in range(dimension):
        for j in range(dimension):
            if(puzzle[i][j]==0):
                return dimension-i
    return -1;


def inversion(puzzle):
    
    temp=0

    for i in range(dimension):
        for j in range(dimension):
            temps=0
            if puzzle[i][j]!=0:
                for m in range(i,dimension):
                    for n in range(dimension):
                        
                        if puzzle[i][j]>puzzle[m][n] and puzzle[m][n]!=0:
                            
                          if(m==i and n>j):
                              temp=temp+1
                              temps=temps+1
                          elif m>i:
                              temp=temp+1
                              temps=temps+1
                              

    return temp


def is_possible():

    possible=False
    
    if(dimension%2==1 and inverse_total%2==0):
      possible=True
    if(dimension%2==0):
      if(blank_tile%2==1 and inverse_total%2==0):
         possible=True
      if(blank_tile%2==0 and inverse_total%2==1):
         possible=True
    
    return possible



def make_puzzle(dimension):
    puzzle=[]
    random_list=random.sample(range(0,dimension*dimension), dimension*dimension)

    count=0
    for i in range(dimension):
      puzzle.append(random_list[count:count+dimension])
      count=count+dimension

    return puzzle
            






  
dimension=4
possible=False

puzzle=make_puzzle(dimension)
print(puzzle)

inverse_total=inversion(puzzle)
blank_tile=blank_tile_row()

print("sum of inversion is: ",inverse_total)
print("blank tile postion from bottom is: ",blank_tile)



possible=is_possible()   
        
if(possible):
    print("solve is possible")
else:
    print("solve isn't possible")





