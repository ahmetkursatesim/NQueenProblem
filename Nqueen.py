import sys
import copy
import math
import random



class GeneticAlgorithmPart:

    def Initalize (self, boardLength, pop_size, zone_size):

        self.boardLength = boardLength
        self.pop_size = pop_size
        self.zone_size = zone_size
        self.zone_count = 0
        self.Target = int((self.boardLength * (self.boardLength - 1)) / 2)
        self.populationCreationList = []
        self.initZone()

        while True:

            if self.reached_Target() == True:
                break

            if -1 < self.zone_size <= self.zone_count:
                break

            self.next_Zone()


        if -1 < self.zone_size <= self.zone_count:
            print("not finding any result ")

        elif self.reached_Target():
            print("Answer Found  %s" % self.zone_count)
            for element in self.populationCreationList:
                if element.fitnessFunc == self.Target:

                    print(element.queens)

                    element.ShowChessBoard()


    def reached_Target(self):

        for element in self.populationCreationList:
            if element.fitnessFunc == self.Target:
                return True
        return False

    def randPopulationselect(self):

        population_nextlist = []
        for i in range(len(self.populationCreationList)):
            population_nextlist.append((i, self.populationCreationList[i].fitnessFunc))
        population_nextlist.sort(key=lambda pop_item: pop_item[1], reverse=True)
        return population_nextlist[:int(len(population_nextlist) / 3)]

    def initZone(self):

        for i in range(self.pop_size):
            self.populationCreationList.append(ChessBoard(self.boardLength,self.Target))

        self.Show_Pop()

    def next_Zone(self):

        self.zone_count += 1

        select_rand = self.randPopulationselect()

        new_population = []
        while len(new_population) < self.pop_size:
            selected_item= random.choice(select_rand)[0]
            new_population.append(copy.deepcopy(self.populationCreationList[selected_item]))
        self.populationCreationList= new_population

        for population in self.populationCreationList:
            population.createPop()

        self.Show_Pop(select_rand)

    def Show_Pop(self, beta=None):

        print("Population #%d" % self.zone_count)

        if beta == None:
            beta = []

        print(" Solution: %s" % str([select_rand[0] for select_rand in beta]))

        counter = 0
        for population in self.populationCreationList:
            print("%16d : (%d) %s" % (counter, population.fitnessFunc, str(population.queens)))
            counter += 1
class ChessBoard:


    def ChangesQueen(self, counter):

        counter = int(counter)

        for alpha in range(counter):
            beta = random.randint(0, self.boardLength - 1)
            tetha = random.randint(0, self.boardLength - 1)
            self.queens[tetha], self.queens[beta] = self.queens[beta], self.queens[tetha]


        self.fitnessApplying()



    def __init__(self, boardLength, Target):

        self.boardLength = boardLength
        self.Target = Target

        self.fitnessFunc = 0


        self.queens = list(range(self.boardLength))

        self.ChangesQueen(self.boardLength / 2)
    def createPop(self):

        self.ChangesQueen(2)
        if random.uniform(0, 1) < 0.25:
            self.ChangesQueen(1)

    def fitnessApplying(self):

        self.fitnessFunc= self.Target

        for row in range(self.boardLength):
            for coloumn in range(row + 1, self.boardLength):
                if math.fabs(self.queens[row] - self.queens[coloumn]) == coloumn - row:

                    self.fitnessFunc -= 1

    def ShowChessBoard(self):

        for x in range(self.boardLength):
            print("", end="|")

            queen = self.queens.index(x)

            for y in range(self.boardLength):
                if y == queen:
                    print("Q", end="|")
                else:
                    print("_", end="|")
            print("")


popsize = 10
zonesize = -1
a=GeneticAlgorithmPart()

boardLength=int(input("Enter Board Length=="))
a.Initalize(boardLength,popsize,zonesize)