import random as rn
import sys
class GeneticAlgorithm:
    def __init__(self,population,
                 fitness_function,
                 gene_generation_function,
                 mutation_rate,end_state,
                 end_state_args = None,
                 individual_generation_function=None,
                 individual_generation_function_args=None,
                 fitness_function_args = None,
                 genes_in_individual = 0):

        self.original_population=population
        self.fitness_function = fitness_function
        self.gene_generation_function = gene_generation_function
        self.mutation_rate_args = mutation_rate
        self.end_state = end_state
        self.end_state_args = end_state_args
        self.individual_generation_function = individual_generation_function
        self.individual_generation_function_args = individual_generation_function_args
        self.fitness_function_args = fitness_function_args
        self.individuals = {}
        self.genes_in_individual = genes_in_individual
        self.start_population(self.original_population)
        self.chosen = []
        self.current_max = rn.choice(list(self.individuals))
        self.max_history = [0]
        self.min_history = [0]
        self.avg = [0]

    def start_population(self,initial_number):
        n = 0
        i = 0
        while n < initial_number and i < 1000000:
            i += 1
            new_individual = self.generate_random()
            if new_individual not in self.individuals:
                self.individuals[new_individual] = None
                n += 1

    def evaluate(self):
        totalSum = 0
        to_delete = []
        maximum_of_generation = -1000000
        minimum_of_generation = sys.maxsize
        for individual in self.individuals:

            if self.individuals[individual] is None:
                self.individuals[individual]=self.fitness_function(individual,self.fitness_function_args)

            if len(self.individuals)>self.original_population*3:
                if self.individuals[individual]<self.avg[-1]:
                    to_delete=to_delete+[individual]

            if self.individuals[self.current_max] is None or self.individuals[individual]>self.individuals[self.current_max]:
                self.current_max=individual

            if self.individuals[individual]>maximum_of_generation:
                maximum_of_generation = self.individuals[individual]

            if self.individuals[individual]<minimum_of_generation:
                minimum_of_generation = self.individuals[individual]

            totalSum+=self.fitness_function(individual,self.fitness_function_args)
        self.avg = self.avg + [totalSum / len(self.individuals)]
        self.max_history = self.max_history + [maximum_of_generation]
        self.min_history = self.min_history + [minimum_of_generation]
        for i in to_delete:
            del self.individuals[i]

    def tourney_select(self):
        max = -1000000
        max_key = ""
        selected = rn.choices(list(self.individuals),k=int(len(self.individuals)/5))
        for individual in selected:
            if self.individuals[individual] >= max:
                max = self.individuals[individual]
                max_key = individual
        return max_key

    def selection(self):
        selected =[]
        while len(selected) < len(self.individuals)/5:
            selection = self.tourney_select()
            selected.append(selection)
        n = 0
        iterations = 0
        while n < len(self.individuals)/10 and iterations <1000:
            sire_1 = rn.choice(selected)
            sire_2 = rn.choice(selected)
            crossover_index = rn.randint(1,len(sire_1))
            child = sire_1[0]
            if (rn.randint(0, 101) > self.mutation_rate_args * 100):
                child = self.gene_generation_function()
            for i in range(1,len(sire_1)):
                if(rn.randint(0,101) > self.mutation_rate_args * 100):
                    child = child+self.gene_generation_function()
                else:
                    if(i<=crossover_index):
                        child = child+sire_1[i]
                    else:
                       child = child+sire_2[i]
            if child not in self.individuals:
                self.individuals[child] = None
                n+=1
            iterations+=1

    def generate_random(self):
        if self.individual_generation_function is None:
            result = []
            for i in range(self.genes_in_individual):
                result = result+self.gene_generation_function()
            return result
        else:
            return self.individual_generation_function(self.individual_generation_function_args)

    def run(self):
        n=0
        self.evaluate()
        while True:
            if self.check_end_state(n):
                break
            self.selection()
            self.evaluate()
            n+=1
        return self.get_data()

    def print(self):
        print(self.individuals)

    def get_data(self):
        return [self.min_history]+[self.avg]+[self.max_history]+[self.current_max]

    def check_end_state(self,iterations):
        return self.end_state(self.end_state_args,self.current_max,self.max_history[-1],iterations)


