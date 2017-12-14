li = [1, 2, 3, 4, 987, 6, 7, 123, 252, 2, 1234, 658]

# With bare logic
maxi = 0
for item in li:
    if item > maxi:
        maxi = item
print maxi

# with reduce


def gr(x, y):
    if x > y:
        return x
    return y

maxi_reduce = reduce(gr, li)
print maxi

# second greatest
maxi1 = 0
maxi2 = 0
for item in li:
    if item > maxi1:
        maxi2 = maxi1
        maxi1 = item

print maxi2
