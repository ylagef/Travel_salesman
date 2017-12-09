class City:
    name = ""
    neighbors = {}

    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors

    def dist_to(self, b):
        return self.neighbors.get(b.name)
