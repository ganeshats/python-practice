f = open("number_map.txt", "r")
# using lambda and map
print reduce(lambda x, y: x+y, map(int, f.readline().split()))
f = open("number_map.txt", "r")
# using lambda and list comprehension
print reduce(lambda x, y: x+y, [int(item) for lin in f for item in lin.split()])
f.close()
