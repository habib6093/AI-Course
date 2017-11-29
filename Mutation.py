from random import randint 
import math
import copy

class Individual:
    geneLength= None
    fitness=None
    gene=[]
    
    def __init__ (self,length=5,fit=0):

            self.geneLength=length
            self.fitness=fit
            self.gene=[0]*length
            
            for i in range(self.geneLength):
               self.gene[i]=randint(0,1)


    def calculateFitness(self):
            self.fitness=0
            for i in range(self.geneLength):
                if(self.gene[i]==1):
                    self.fitness+=1

            return self.fitness
    

    

class Population:
    populationSize=None
    individuals=[]
    fittest=None
    
    def __init__ (self,size=5,indi=[],fit=0):
        self.populationSize=size
        self.fittest=fit 
        self.individuals=indi
        


    def calculateFitness(self):
            
            for i in self.individuals:
                i.calculateFitness()

            self.individuals.sort(key=lambda x: x.fitness, reverse=False)
                

    def getFittestIndividual(self):
            self.calculateFitness()
            return self.individuals[-1]
    

    

    def getSecondFittestIndividual(self):
        return self.individuals[-2]
            


    def getLeastFittestIndividual(self):
        return self.individuals[0]


    def selection(self):
        self.getFittestIndividual()
   
        


    def crossOver(self):
        self.selection()
        
        swapPoint=randint(0,self.individuals[0].geneLength)
        
        temp=copy.copy(self.individuals[-2:])

        for i in range(swapPoint):
           temp[0].gene[i],temp[1].gene[i] = temp[1].gene[i],temp[0].gene[i]

        
       
     
        return temp
            
            
    def mutation(self):
        temp=self.crossOver()
        
        randomPoint=randint(0,self.individuals[0].geneLength-1)
      #  print("random is: ", randomPoint)
        temp[0].gene[randomPoint]=1

        randomPoint=randint(0,self.individuals[0].geneLength-1)
       # print("random is: ", randomPoint)
        temp[1].gene[randomPoint]=1

        self.selection()

        return temp

    

    def getFittestOffspring(self):

        temp=self.mutation()

        temp[0].fitness=0
        temp[1].fitness=0
        
        for i in range(2):
            for j in range(temp[0].geneLength):
                if(j==1):
                     temp[i].fitness+=1
        
        temp.sort(key=lambda x: x.fitness, reverse=False)

        self.individuals[0]=temp[-1]

        self.calculateFitness()

        return self.individuals[-1].fitness
        

        


x=Individual(5,0)
y=Individual(5,0)
z=Individual(5,0)

a=Population(3,[x,y,z],-1)

count=0
while(a.getFittestOffspring()<5):

  count+=1


print("generation is: ",count)






##            
##    --get fittest individual--
##        -calculate and compare fitness of each individuals
##        -get the index of fittest individual
##        -fittest=fitness value of the highest individual
##    -return fittest individual
##    
##    --get second most fittest individual--
##    --get index of least fittest individual--
##
##--Selection--
##    --select the most fittest individual--
##    --seelect the second most fittest individual--
##
##--crossover--
##    -select a random crossover point
##    -swap values among parents-
##
##--mutation--
##    -select a random mutation point
##    -flip values at the muation point
##
##--get fittest offspring--
##
##--add fittest offspring-- [replacce least fittest individual from most fittest offspring]
##    -update fitness value of offspring
##    -get index of least fit individual
##    -replace least fittest individual with most fittest offspring
##
##--main--
##    - Population population=
##    - Individual fittest=
##    - Individual secondFittest=
##    - generationCount=
##
##    --initialize population--
##    --calculate fitness of each individual--
##    --loop--
##        -while population gets an individual with maximum fitness-
##            - do selection
##            - do crossover
##            - do mudation 
##            - add fittest offspring to population
##            - calculate new fitness value
##    
##    
##
##        
##        
##    
##    
