from models.genetic.algorithm.GAConfig import GAConfig
import random
class GA:
    def __init__(self, chromosome, flowerPart, poblationSize):
        self.__chromosome = chromosome
        self.__flowerPart = flowerPart
        self.__poblationSize = poblationSize
        self.__mutationRate = GAConfig.MUTATION_RATE

        self.__poblation = []
        self.__mutations = 0
        self.__generation = 0
        self.__isRunning = False
        self.__started = False

    def run(self):
        self.__isRunning = True
        self.__started = True
        while(self.__isRunning):
            print("I am running" + self.__flowerPart)
            #select
            #cross-over
            #mutate
            #evaluate

    def mutate(self, ind):
        if random.randint(1, 100) < self.__mutationRate:
            bit = random.randint(0, GAConfig.GENES_LENGTH-1)
            if ind[bit] == 0:
                ind[bit] = 1
            if ind[bit] == 1:
                ind[bit] = 0
            self.__mutations += 1

    def crossover(self, parent1, parent2):
        bitP1 = random.randint(0, GAConfig.GENES_LENGTH)
        bitP2 = random.randint(0, GAConfig.GENES_LENGTH)
        child = parent1.copy()
        if bitP1 <= bitP2:
            child[bitP1:bitP2] = parent2[bitP1:bitP2]
        else:
            child[bitP2:bitP1] = parent2[bitP2:bitP1]
        return child

    def getMutationsInfo(self):
        return self.__mutations

    def isRunning(self):
        return self.__isRunning

    def isStarted(self):
        return self.__started

    def pause(self):
        self.__isRunning = not self.__isRunning

    def getPoblation(self):
        return self.__poblation