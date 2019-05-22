in_text = ""
text_list = []
while in_text != "done":
    in_text = raw_input("Enter a string ('done' to exit): ")
    if in_text != "done":
        text_list.append(in_text)
input_tuple = tuple(text_list)
print text_list
print input_tuple