def strLength(strArg):
    length = 0
    for c in strArg:
        length = length + 1
    return length


str1 = raw_input("Enter first string")
str2 = raw_input("Enter second string")

if strLength(str1) > strLength(str2):
    print str1 + " is lengthy"
else:
    print str2 + " is lengthy"

    # code to add digits in a number
    # sums = 0
    # for c in name:
    #     sums = sums + int(c)
    # print sums
