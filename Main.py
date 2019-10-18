import GeneticAlgorithm as GA
import BitSequence as bitseq
import WordSequence as wordseq
import Maze as mz
import random as rn
import matplotlib.pyplot as plt

BITSEQUENCE_GOAL = bitseq.BitSequence.generate_individual(300)
BITSEQUENCE_INITIAL_POPULATION = 50
BITSEQUENCE_MUTATION_RATE = 0.8
BITSEQUENCE_ARGS = {'goal':BITSEQUENCE_GOAL,'iterations':1000}
BITSEQUENCE_GENES_IN_INDIVIDUAL = len(BITSEQUENCE_ARGS['goal'])
BITSEQUENCE = GA.GeneticAlgorithm(BITSEQUENCE_INITIAL_POPULATION,
                                  bitseq.BitSequence.fitness,
                                  bitseq.BitSequence.generate_gene,
                                  BITSEQUENCE_MUTATION_RATE,
                                  bitseq.BitSequence.end_state,
                                  BITSEQUENCE_ARGS,
                                  bitseq.BitSequence.generate_individual,
                                  BITSEQUENCE_GENES_IN_INDIVIDUAL,
                                  BITSEQUENCE_ARGS['goal'])
results = BITSEQUENCE.run()
f1 = plt.figure(1)
ax1 = f1.add_subplot(111)
ax1.set_title("Fitness Evolution of BitSequence")
ax1.set_xlabel('Generations')
ax1.set_ylabel('Number of Accurate Characters')
ax1.plot(results[0], c='r')
ax1.plot(results[1], c='b')
ax1.plot(results[2], c='g')
f1.show()
print("BITSEQUENCE")
print("Goal sequence: " + BITSEQUENCE_GOAL)
print("Obtained Sequence: "+ results[3]+"\n")

WORDSEQUENCE_GOAL = "thequickscribejumpedoverthelazypaladin" #wordseq.WordSequence.generate_individual(300)
WORDSEQUENCE_INITIAL_POPULATION = 50
WORDSEQUENCE_MUTATION_RATE = 0.8
WORDSEQUENCE_ARGS = {'goal':WORDSEQUENCE_GOAL, 'iterations':1000}
WORDSEQUENCE_GENES_IN_INDIVIDUAL = len(WORDSEQUENCE_ARGS['goal'])
WORDSEQUENCE = GA.GeneticAlgorithm(WORDSEQUENCE_INITIAL_POPULATION,
                                  wordseq.WordSequence.fitness,
                                  wordseq.WordSequence.generate_gene,
                                  WORDSEQUENCE_MUTATION_RATE,
                                  wordseq.WordSequence.end_state,
                                  WORDSEQUENCE_ARGS,
                                  wordseq.WordSequence.generate_individual,
                                  WORDSEQUENCE_GENES_IN_INDIVIDUAL,
                                  WORDSEQUENCE_ARGS['goal'])
results_w = WORDSEQUENCE.run()
f1 = plt.figure(1)
ax1 = f1.add_subplot(111)
ax1.set_title("Fitness Evolution of WordSequence")
ax1.set_xlabel('Generations')
ax1.set_ylabel('Number of Accurate Characters')
ax1.plot(results_w[0], c='r')
ax1.plot(results_w[1], c='b')
ax1.plot(results_w[2], c='g')
f1.show()
print("WORDSEQUENCE")
print("Goal sequence: " + WORDSEQUENCE_GOAL)
print("Obtained Sequence: "+ results_w[3]+"\n")


MAZE_GOAL = {'representation':[[0,0,1,0,0],[1,0,1,1,1],[1,0,1,1,2],[1,0,0,1,3],
                               [0,0,1,1,4],[1,1,0,0,5],[0,1,0,0,6],[0,1,0,1,7],
                               [0,1,0,1,8],[0,0,1,0,9],[1,0,1,0,10],[1,1,0,1,11],
                               [0,1,1,0,12],[1,0,1,0,13],[1,0,0,0,14],[0,1,0,2,15]],
        'x':3,
        'totalcells':16}
MAZE_INITIAL_POPULATION = 50
MAZE_MUTATION_RATE = 0.8
MAZE_ARGS = {'maze':MAZE_GOAL, 'iterations':30}
MAZE_GENES_IN_INDIVIDUAL = MAZE_ARGS['maze']['totalcells']
MAZE = GA.GeneticAlgorithm(MAZE_INITIAL_POPULATION,
                                   mz.Maze.fitness,
                                   mz.Maze.generate_gene,
                                   MAZE_MUTATION_RATE,
                                   mz.Maze.end_state,
                                   MAZE_ARGS,
                                   mz.Maze.generate_individual,
                                   MAZE_GENES_IN_INDIVIDUAL,
                                   MAZE_ARGS['maze'])
results_w = MAZE.run()
f1 = plt.figure(1)
ax1 = f1.add_subplot(111)
ax1.set_title("Fitness Evolution")
ax1.set_xlabel('Generations')
ax1.set_ylabel('Progress along the laberinth')
ax1.plot(results_w[0], c='r')
ax1.plot(results_w[1], c='b')
ax1.plot(results_w[2], c='g')
f1.show()
print("Obtained Sequence: "+ mz.Maze.translate(results_w[3]))
