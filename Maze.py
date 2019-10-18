import random as rn
import sys
# The maze consists of a matrix of arrays with 5 values, the first four represent wich side of a cell is blocked
# this is denoted by a 0 if its blocked a 1 if it can pass or a 2 if it reached the exit.
# The las value of the array represents wich cell it is.
# 0 = ←
# 1 = ↑
# 2 = →
# 3 = ↓


class Maze:

    @staticmethod
    def fitness(individual,maze):
        current_cell=maze['representation'][0]
        visited_cells=[0]*maze['totalcells']
        visited_cells[0]=1
        result = 0
        for i in range(len(individual)):
            if current_cell[int(individual[i])] == 0:
                return -10
            elif current_cell[int(individual[i])] == 2:
                return maze['totalcells']+1
            else:
                if individual[i]=="1":
                    current_cell=maze['representation'][current_cell[4]-maze["x"]]
                    if visited_cells[current_cell[4]]!=0:
                        visited_cells[current_cell[4]]+=1
                        result-=visited_cells[current_cell[4]]
                    else:
                        result+=1
                elif individual[i]=="3":
                    current_cell=maze['representation'][current_cell[4]+maze["x"]]
                    if visited_cells[current_cell[4]]!=0:
                        visited_cells[current_cell[4]]+=1
                        result-=visited_cells[current_cell[4]]
                    else:
                        result+=1
                elif individual[i]=="0":
                    current_cell=maze['representation'][current_cell[4]-1]
                    if visited_cells[current_cell[4]]!=0:
                        visited_cells[current_cell[4]]+=1
                        result-=visited_cells[current_cell[4]]
                    else:
                        result+=1
                else:
                    current_cell=maze['representation'][current_cell[4]+1]
                    if visited_cells[current_cell[4]]!=0:
                        visited_cells[current_cell[4]]+=1
                        result-=visited_cells[current_cell[4]]
                    else:
                        result+=1
        return result

    @staticmethod
    def generate_gene():
        return rn.choice(["0", "1", "2", "3"])

    @staticmethod
    def generate_individual(n):
        result = ""
        for i in range(n):
            result=result+rn.choice(["0", "1", "2", "3"])
        return result

    @staticmethod
    def translate(moves):
        result = ""
        for character in moves:
            if character == "0":
                result+=" ←"
            elif character == "1":
                result+=" ↑"
            elif character == "2":
                result+=" →"
            else:
                result+=" ↓"
        return result

    @staticmethod
    def end_state(args,given_sequence,max_score,iterations):
        if iterations>args['iterations'] or max_score>args['maze']['totalcells']:
            if max_score>args['maze']['totalcells']:
                print("SUCCESS!")
            return True
        else:
            return False