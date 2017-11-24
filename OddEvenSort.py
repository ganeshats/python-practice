in_numbers = raw_input("Enter some numbers with comma separated: ").strip()
even_list = []
odd_list = []
# for x in in_numbers.split(","):
#     if int(x) % 2 == 0:
#         even_list.append(x)
#     else:
#         odd_list.append(x)

even_list = filter(lambda n: int(n) % 2 == 0, in_numbers.split(","))
odd_list = filter(lambda n: int(n) % 2 != 0, in_numbers.split(","))

print even_list
print odd_list

print [x for x in in_numbers.split(",") if int(x) % 2 == 0]
print [x for x in in_numbers.split(",") if int(x) % 2 != 0]
