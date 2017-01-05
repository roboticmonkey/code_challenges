
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

    

    # convert string to list
    message = list(message)

    #reverse list
    message = reverse_letters(message, 0, len(message) -1)

    # keep track of where the words start
    word_start = 0
    
    for i in xrange(len(message) +1):


        # find each word and reverse it again
        if (i == len(message)) or (message[i] == " ") :
            message = reverse_letters(message, word_start, i -1)
            word_start = i + 1
        
    # convert the list back into a string
    message = "".join(message)

    # return the message
    return message


msg = "find you will pain only go you recordings security the into if"

print  reverse_words(msg)

msg2 = "tea for time!"

print reverse_words(msg2)

