def find_rotation_point(words):
    # write the body of your function here

    first_word = words[0]
    
    lower_bounds = 0
    upper_bounds = len(words)-1


    if first_word < words[-1]:
        return 0

    while lower_bounds < upper_bounds:

        # if alist[index - 1] < alist[index] and alist[index] < alist[index + 1]:

        #     if alist[lower_bounds] > alist[index]:
        #         upper_bounds = index
        #     else:
        #         lower_bounds = index

        #     index = ((upper_bounds - lower_bounds) / 2) + lower_bounds

        # if alist[index - 1] < alist[index] and alist[index] > alist[index + 1]:
        #     return index + 1

        # if alist[index - 1] > alist[index] and alist[index] < alist[index + 1]:
        #     return index

        #SIMPLER VERSION
        guess_index = lower_bounds + ((upper_bounds - lower_bounds) / 2)

        #if guessed word is bigger than first word move right
        if first_word < words[guess_index]:
            lower_bounds = guess_index

        #otherwise move left
        else:
            upper_bounds = guess_index

        if lower_bounds + 1 == upper_bounds:
            return upper_bounds



list1 = ['pea', 'suash', 'zebra', 'all', 'bat', 'dog', 'horse', 'monkey']
list2 = ['mon', 'open', 'quit', 'rat', 'stop', 'tv','vice','zig', 'apple', 'ball', 'cup', 'dig', 'ear']
list3 = ['a','b', 'c', 'd','e']

print find_rotation_point(list1)

print find_rotation_point(list2)
print find_rotation_point(list3)