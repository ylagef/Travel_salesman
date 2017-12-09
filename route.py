class Route:
    route = []
    fitness = 0

    def __init__(self, route):
        self.route = route
        self.fitness = self.calc_fitness()
        # self.print_route()

    def calc_fitness(self):
        fitness = 0

        for i in range(0, len(self.route)):
            actual_city = self.route[i]

            if i < len(self.route) - 1:
                next_city = self.route[i + 1]
                fitness += actual_city.dist_to(next_city)

        return fitness

    def print_route(self):
        to_print = ""
        for i in self.route:
            to_print += i.name + " "
        print("Route =", to_print + "- Fitness =", self.fitness)
