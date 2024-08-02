import math

n = 40
k = 20

routes = math.comb(n, k)

print("There are {} different paths in a 20x20 grid.".format(routes))