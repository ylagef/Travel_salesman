from random import randint


# Used for create new random routes
def random_route(def_route):
    r_route = []
    for i in range(len(def_route)):
        r_route.append(def_route.pop(randint(0, len(def_route) - 1)))
    return r_route


class Route:
    route = []
    fitness = 0

    def __init__(self, route):
        self.route = route
        self.calc_fitness()

    # It calculates the fitness (sum of distances) for this route
    def calc_fitness(self):
        self.fitness = 0
        for i in range(len(self.route)):
            actual_city = self.route[i]
            if i < len(self.route) - 1:
                next_city = self.route[i + 1]
                self.fitness += actual_city.dist_to(next_city)
        self.fitness += actual_city.dist_to(self.route[0])  # Return to first city
        return self.fitness

    def swap(self, times, rate):
        if randint(0, 100) < (rate * 100):
            for i in range(times):
                index_a = randint(0, len(self.route) - 1)
                index_b = randint(0, len(self.route) - 1)
                city_a = self.route[index_a]
                city_b = self.route[index_b]
                self.route[index_a] = city_b
                self.route[index_b] = city_a
            self.calc_fitness()
        return self

    def print_route(self):
        to_print = ""
        for i in self.route:
            to_print += i.name + " "
        print("Route =", to_print + "- Fitness =", self.fitness)
