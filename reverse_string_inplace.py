def reverse_string_in_place(string):

    # first tokenize the string
    string_list = list(string)

    
    #then reverse the list in place
    for i in range((len(string)/2)):
        # swaps the values, starts at ends moves to middle
        string_list[i], string_list[-i-1] = string_list[-i-1], string_list[i]


    return ''.join(string_list)


string = "a dog came to town"
print reverse_string_in_place(string)