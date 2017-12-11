from city import City
from route import Route, random_route
from random import randint
import copy

# Data for this example
a = City("a", {'a': 'x', 'b': 5, 'c': 4, 'd': 7, 'e': 6, 'f': 5, 'g': 7, 'h': 4, 'i': 2, 'j': 9})
b = City("b", {'a': 6, 'b': 'x', 'c': 5, 'd': 6, 'e': 4, 'f': 8, 'g': 5, 'h': 4, 'i': 3, 'j': 8})
c = City("c", {'a': 3, 'b': 5, 'c': 'x', 'd': 3, 'e': 5, 'f': 6, 'g': 9, 'h': 8, 'i': 7, 'j': 6})
d = City("d", {'a': 7, 'b': 5, 'c': 4, 'd': 'x', 'e': 3, 'f': 5, 'g': 7, 'h': 9, 'i': 8, 'j': 3})
e = City("e", {'a': 5, 'b': 4, 'c': 5, 'd': 3, 'e': 'x', 'f': 4, 'g': 6, 'h': 7, 'i': 8, 'j': 7})
f = City("f", {'a': 5, 'b': 6, 'c': 5, 'd': 5, 'e': 4, 'f': 'x', 'g': 5, 'h': 4, 'i': 3, 'j': 2})
g = City("g", {'a': 6, 'b': 7, 'c': 9, 'd': 7, 'e': 6, 'f': 6, 'g': 'x', 'h': 5, 'i': 7, 'j': 9})
h = City("h", {'a': 5, 'b': 4, 'c': 8, 'd': 7, 'e': 6, 'f': 4, 'g': 4, 'h': 'x', 'i': 6, 'j': 5})
i = City("i", {'a': 2, 'b': 3, 'c': 6, 'd': 9, 'e': 8, 'f': 3, 'g': 7, 'h': 5, 'i': 'x', 'j': 7})
j = City("j", {'a': 9, 'b': 7, 'c': 5, 'd': 4, 'e': 8, 'f': 3, 'g': 9, 'h': 5, 'i': 7, 'j': 'x'})


# Create the initial random population
def initial_population(quantity):
    pop = dict()
    for _ in range(quantity):
        new_route = Route(random_route([a, b, c, d, e, f, g, h, i, j]))
        pop[new_route] = new_route.calc_fitness()
    return pop


# Evaluate the population - Givin percentages for most fitness-likely routes
def evaluate_population(pop_to_eval):
    evaluated_population = dict()
    selection_array = []
    minimum = min(pop_to_eval.values())
    for key, value in pop_to_eval.items():
        evaluated_population[key] = int(1 / (value - minimum + 1) * 10) + 1
        for _ in range(int(1 / (value - minimum + 1) * 10) + 1):
            selection_array.append(key)
    return selection_array


# Generate new population based on past and percentage of  fitness
def generate_new_population(s_times, s_rate, s_array, b_ever):
    n_population = dict()
    for _ in range(len(population)):
        new_route = copy.deepcopy(s_array[randint(0, len(sel_array) - 1)]).swap(s_times, s_rate)
        n_population[new_route] = new_route.fitness
        if new_route.fitness < b_ever.fitness:
            b_ever = new_route
    return n_population, b_ever


# MAIN PROGRAM
swap_times = 1  # Number of times cities are swapped
swap_rate = 0.5  # Rate of swapping cities
population_size = 1000  # Size of population used
num_of_iterations = 10000  # Number of max iterations

best_ever = Route([a, b, c, d, e, f, g, h, i, j])  # Default best route
population = initial_population(population_size)  # Generate initial random population

iteration = 0
for _ in range(num_of_iterations):
    sel_array = evaluate_population(population)
    population, best_ever = generate_new_population(swap_times, swap_rate, sel_array, best_ever)
    print(best_ever.fitness, iteration)
    if best_ever.fitness < 29:
        break
    iteration += 1

print("\nBEST ROUTE FOUND:")
best_ever.print_route()
print("Iterations done:", iteration)
print("\nBEST ROUTE SHOULD BE:\nRoute = c a i f j d e b h g - Fitness = 29")
