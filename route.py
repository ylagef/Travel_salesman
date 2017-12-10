from random import randint


class Route:
    route = []
    fitness = 0

    def __init__(self, route):
        self.route = route
        self.fitness = self.calc_fitness()

    # Used for create new random routes based in others
    def randomize_route(self):
        aux_route = self.route
        self.route = []
        for i in range(0, len(aux_route)):
            self.route.append(aux_route.pop(randint(0, len(aux_route) - 1)))
        self.calc_fitness()

    # It calculates the fitness (sum of distances) for this route
    def calc_fitness(self):
        self.fitness = 0
        for i in range(0, len(self.route)):
            actual_city = self.route[i]

            if i < len(self.route) - 1:
                next_city = self.route[i + 1]
                self.fitness += actual_city.dist_to(next_city)

        return self.fitness

    def print_route(self):
        to_print = ""
        for i in self.route:
            to_print += i.name + " "
        print("Route =", to_print + "- Fitness =", self.fitness)
