#file_path = raw_input("Enter the file path: ")
file_path = "test.txt"
fil = open(file_path, "r")
ignoreList = ['a', 'an', 'is', 'was', 'the', 'if', 'of']
count_dict = {}
for line in fil:

#in_sentence = raw_input("Enter a sentence: ")
    for word in line.split():
        if word.lower() not in ignoreList:
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1
print count_dict

# To compare if the ignore list is working
count_dict = {}
fil = open(file_path, "r")
for line in fil:

#in_sentence = raw_input("Enter a sentence: ")
    for word in line.split():
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
print count_dict
