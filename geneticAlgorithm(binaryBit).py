from random import randint
import copy


class Individual:
    geneLength = None
    fitness = None
    gene = []

    def __init__(self, length, fit=0):

        self.geneLength = length
        self.fitness = fit
        self.gene = [0] * length

        for i in range(self.geneLength):
            self.gene[i] = randint(0, 1)

    def calculateFitness(self):
        self.fitness = 0
        for i in range(self.geneLength):
            if (self.gene[i] == 1):
                self.fitness += 1

        return self.fitness


class Population:
    populationSize = None
    individuals = []
    fittest = None

    def __init__(self, size, indi=[], fit=0):
        self.populationSize = size
        self.fittest = fit
        self.individuals = indi



    def calculateFitness(self,temp):
        for i in temp:
            i.calculateFitness()
            print(i.gene,"  fitness  ",i.fitness)

        temp.sort(key=lambda x: x.fitness, reverse=False)

        return temp   #temp contains array of objects



    def getFittestIndividual(self):
        temp=self.calculateFitness(self.individuals)
        self.individuals=temp

        return temp[-1]



    def getSecondFittestIndividual(self):
        temp=self.individuals[-2]#self.calculateFitness(self.individuals)
        return temp



    def getLeastFittestIndividual(self):
        temp=self.calculateFitness(self.individuals)
        return temp[0]



    def selection(self):
        
        mostFittest=copy.deepcopy(self.getFittestIndividual())
        secondMostFittest=copy.deepcopy(self.getSecondFittestIndividual())

        temp=[mostFittest,secondMostFittest]
        return temp




    def crossOver(self):
        swapPoint = randint(0, self.individuals[0].geneLength)

        temp = self.selection()

        for i in range(swapPoint):
            temp[0].gene[i], temp[1].gene[i] = temp[1].gene[i], temp[0].gene[i]

        #self.getFittestIndividual()

        return copy.copy(temp)



    def mutation(self):
        temp = self.crossOver()

        randomPoint = randint(0, self.individuals[0].geneLength - 1)
        temp[0].gene[randomPoint] = 1

        randomPoint = randint(0, self.individuals[0].geneLength - 1)
        temp[1].gene[randomPoint] = 1
        
        print("Offsprings are..............")
    
        	

        return temp




    def getFittestOffspring(self):
        
        temp=self.calculateFitness(self.mutation())
        
        
        if temp[-1].fitness > self.individuals[0].fitness:
          self.individuals[0] = temp[-1]
        
        print("after changing least fittest population with fittest offspring............")
        return self.getFittestIndividual().fitness





geneLength=5

x = Individual(geneLength)
y = Individual(geneLength)
z = Individual(geneLength)


populationSize=3

a = Population(populationSize, [x, y, z])

count = 1
while (a.getFittestOffspring() < geneLength):
    print("End of generation.....................",count)
    print(" ")
    count += 1

print(count," Generations are needed to find the fully fittest individual" )





