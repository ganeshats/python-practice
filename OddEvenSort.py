in_numbers = raw_input("Enter some numbers with comma separated: ").strip()
even_list = []
odd_list = []
for x in in_numbers.split(","):
    if int(x) % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

print even_list
print odd_list