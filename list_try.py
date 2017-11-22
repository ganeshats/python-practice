num_list = []
for i in range(0,5,1):
    in_text = raw_input("Enter a number: ")
    num_list.append(in_text)

sums = 0
for n in num_list:
    sums += int(n)

print sums
print num_list[1]
