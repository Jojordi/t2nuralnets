import random as rn
class BitSequence:

    @staticmethod
    def fitness(individual,goal_sequence):
        score = 0
        for c_i,c_gs in zip(individual,goal_sequence):
            if c_i == c_gs:
                score+=1
        return score

    @staticmethod
    def generate_gene():
        return rn.choice(["0","1"])

    @staticmethod
    def generate_individual(n):
        result = ""
        for i in range(n):
            result=result+rn.choice(["0","1"])
        return result

    @staticmethod
    def end_state(args,given_sequence,max_score,iterations):
        if iterations>args["iterations"] or given_sequence==args["goal"]:
            if given_sequence==args["goal"]:
                print("SUCCESS!")
            return True
        else:
            return False



