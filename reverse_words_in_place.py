
def reverse_letters(message, start_index, end_index):

    """helper function that reverses letters in a string"""

    temp_letter = " "

    for i in xrange(len(letters[start_index: end_index])/2):
        temp_letter = letters[i]
        letters[i] = letters[-(i+1)]
        letters[-(i+1)] = temp_letter

    return letters


def reverse_words(message):

    """ reverses the words of a message in place """

    message = list(message)

    message = reverse_letters(message, 0, len(message) -1)

    word_start = 0
    

    for i in xrange(len(message)):
        # print i, message[i]

        if message[i] == " ":
            
            message = reverse_letters(message, word_start, i)
            word_start = i +1
        elif  i == len(message)-1:
            
            message = reverse_letters(message, word_start, i)
            
        else:
            continue
 

    message = "".join(message)

    return message


msg = "find you will pain only go you recordings security the into if"

print "from function call: ", reverse_words(msg)
reverse_words(msg)
print "msg var: ", msg 