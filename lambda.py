a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
b = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
c = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
poe = map(lambda x, y: x**y, a, b)
print poe
cabf = lambda x, y, z: z-(x+y)
cab = map(cabf, a, b, c)
print cab

