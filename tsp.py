from city import City
from route import Route

# INSERT AL DATA FROM TABLE INTO THE DICT()
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

Route([a, b, c, d, e, f, g, h, i, j]).print_route()
