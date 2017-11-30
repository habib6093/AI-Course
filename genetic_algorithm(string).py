from random import randint
import copy


class Individual:
    geneLength = None
    distance = None
    gene = []

    def __init__(self, length,gene=None):

        self.geneLength = length
        self.distance=0
        self.gene = [0] * length

        if gene==None:
            for i in range(self.geneLength):
               self.gene[i] = chr(randint(97, 122))

        else:
            self.gene=gene



    def calculateFitness(self,goal):
        self.distance = 0
        for i in range(self.geneLength):
            dis=abs(ord(goal[i])-ord(self.gene[i]))
            self.distance += dis

        return self.distance






class Population:
    populationSize = None
    individuals = []
    fittest = None

    def __init__(self, size, indi=[], fit=0):
        self.populationSize = size
        self.fittest = fit
        self.individuals = indi



    def calculateFitness(self,temp,goal):
        for i in temp:
            i.calculateFitness(goal)

        temp.sort(key=lambda x: x.distance, reverse=True)

        return temp   #temp contains array of object



    def getFittestIndividual(self,goal):
        temp=self.calculateFitness(self.individuals,goal)
        self.individuals=temp

        return temp[-1]



    def getSecondFittestIndividual(self,goal):
        temp=self.calculateFitness(self.individuals,goal)
        return temp[-2]



    def getLeastFittestIndividual(self,goal):
        temp=self.calculateFitness(self.individuals,goal)
        return temp[0]



    def selection(self,goal):
        mostFittest=copy.deepcopy(self.getFittestIndividual(goal))
        secondMostFittest=copy.deepcopy(self.getSecondFittestIndividual(goal))

        temp=[mostFittest,secondMostFittest]
        return temp




    def crossOver(self,goal):
        swapPoint = randint(0, self.individuals[0].geneLength)

        temp = self.selection(goal)

        for i in range(swapPoint):
            temp[0].gene[i], temp[1].gene[i] = temp[1].gene[i], temp[0].gene[i]

        self.getFittestIndividual(goal)

        return copy.copy(temp)



    def mutation(self,goal):
        temp = self.crossOver(goal)

        randomPoint = randint(0, self.individuals[0].geneLength - 1)

        if temp[0].gene[randomPoint] < goal[randomPoint]:
            temp[0].gene[randomPoint]= chr(ord(temp[0].gene[randomPoint]) + 1)

        elif temp[0].gene[randomPoint] > goal[randomPoint]:
            temp[0].gene[randomPoint] = chr(ord(temp[0].gene[randomPoint]) - 1)


        randomPoint = randint(0, self.individuals[0].geneLength - 1)

        if temp[1].gene[randomPoint] < goal[randomPoint]:
            temp[1].gene[randomPoint] = chr(ord(temp[1].gene[randomPoint]) + 1)

        elif temp[1].gene[randomPoint] > goal[randomPoint]:
            temp[1].gene[randomPoint] = chr(ord(temp[1].gene[randomPoint]) - 1)


        #self.getFittestIndividual()

        return temp




    def getFittestOffspring(self,goal):


        temp=self.calculateFitness(self.mutation(goal),goal)
        print("idividuals")
        for i in self.individuals:
            print(i.gene,"  distance ",i.distance)

        print(" ")
        print("offsprings")
        for i in temp:
            print(i.gene, "  distance ", i.distance)


        self.individuals[0] = temp[-1]

        return self.getFittestIndividual(goal).distance





geneLength=5
gene=None
x = Individual(geneLength,gene)
y = Individual(geneLength,gene)
z = Individual(geneLength,gene)


populationSize=3
goal=['h','e','l','l','o']

a = Population(populationSize, [x, y, z])

count = 1
while (a.getFittestOffspring(goal) >0):
    print("----  generation ", count, "------")
    print(" ")
    count += 1


print(count," Generations are needed to find the fully fittest individual" )


