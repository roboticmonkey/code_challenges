
def reverse_letters(message, start_index, end_index):

    """helper function that reverses letters in a string"""

    temp_letter = " "
    

    while start_index < end_index:

        temp_letter = message[start_index]
        message[start_index] = message[end_index]
        message[end_index] = temp_letter

        start_index += 1
        end_index -= 1

      
    return message


def reverse_words(message):

    """ reverses the words of a message in place """

    message = list(message)

    message = reverse_letters(message, 0, len(message) -1)

    word_start = 0
    
    for i in xrange(len(message)):

        if (message[i] == " "):
            # print "word_start", word_start
            message = reverse_letters(message, word_start, i -1)
            word_start = i + 1
        elif  i == len(message)-1:
            
            message = reverse_letters(message, word_start, i)
            
        else:
            continue
 

    message = "".join(message)

    return message


msg = "find you will pain only go you recordings security the into if"

print "from function call: ", reverse_words(msg)
print "msg var: ", msg 