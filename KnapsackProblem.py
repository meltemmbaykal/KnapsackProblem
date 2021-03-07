from __future__ import print_function
from simpleai.search.local import genetic, hill_climbing, hill_climbing_random_restarts
from simpleai.search.models import SearchProblem
import random

items = int(input("Enter the number of item: "))
capacity = int(input("Enter the knapsack capacity: "))
weights = input("Enter the weight of the items separated by spaces: ")
values = input("Enter the values of the items separated by spaces: ")



def string_to_list(a_string):
    a_list = a_string.split()
    map_object = map(int, a_list)

    return list(map_object)


def list_to_string(a_list):
    string_ints = [str(int) for int in a_list]

    return " ".join(string_ints)



class KnapsackProblem(SearchProblem):
    numV = 0
    numW = 0

    def __init__(self):
        super(KnapsackProblem, self).__init__(initial_state=self.generate_random_state())


    def actions(self, state):
        return list(range(0, items))

    def result(self, state, action):

        l_state = list_to_string(state)
        s_state = string_to_list(l_state)

        if s_state[action] == 1:
            s_state[action] = 0
        else:
            s_state[action] = 1

        return s_state

    def value(self, state):
        sumWeight = 0
        sumValue = 0
        l_state = list_to_string(state)
        s_state = string_to_list(l_state)
        s_w = string_to_list(weights)
        s_v = string_to_list(values)


        for i in range(0, items):
            sumWeight += s_state[i] * s_w[i]

        if sumWeight <= capacity:
            for i in range(0, items):
                sumValue += s_state[i] * s_v[i]
        else:
            sumValue = 0

        if self.numV < sumValue:
            self.numV = sumValue
            if self.numW < sumWeight:
                self.numW = sumWeight

        return sumValue

    def generate_random_state(self):
        list = []
        letters = '01'
        for i in range(0,items):
         harf = random.choice(letters)
         list.append(harf)
        return list

    def crossover(self, state1, state2):

        cut_point = random.randint(0, items)
        child = state1[:cut_point] + state2[cut_point:]

        return child

    def mutate(self, state):
        mutation = random.choice('01')
        mutation_point = random.randint(0, items)
        mutated = ''.join([state[i] if i != mutation_point else mutation
                           for i in range(len(state))])

        l_state = list_to_string(mutated)
        s_state = string_to_list(l_state)

        return s_state


problem = KnapsackProblem()

result = genetic(problem)


print(result.state)
print("Weight: ", problem.numW)
print("Value: ", problem.numV)
