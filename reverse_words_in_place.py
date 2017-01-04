def reverse_letters(letters):

    temp_letter = " "

    for i in xrange(len(letters)/2):
        temp_letter = letters[i]
        letters[i] = letters[-(i+1)]
        letters[-(i+1)] = temp_letter

    return letters


def reverse_words(message):

    """ reverses the words of a message in place """

    # print "before split", message

    # message = message.split(" ")
    message = list(message)

    # print "after split", message

    # temp_letter = " "

    # for i in xrange(len(message)/2):
    #     temp_letter = message[i]
    #     message[i] = message[-(i+1)]
    #     message[-(i+1)] = temp_letter

    message = reverse_letters(message)

    # print "after loop", message

    # message = "".join(message)

    # print " after join", message

    word_start = 0
    word_end = 0

    for i in xrange(len(message)):
        # print i, message[i]

        if message[i] == " ":
            word_end = i-1
            # print "word_end", word_end
            
            # word_len = i - word_start
            # # print "word_len", word_len
            # count = 0
            # while count < word_len/2:
            #     # print "count", count
            #     temp_letter = message[word_start+count]
            #     # print "temp_letter", temp_letter

            #     message[word_start+count] = message[word_end-count]
            #     # print "first swap", message[word_start+count]
            #     message[word_end-count] = temp_letter
            #     # print "second swap", message[word_end-count]
            #     count += 1
            # word_start = i+1
        elif  i == len(message)-1:
            word_end = i
            word_len = len(message) - word_start
            # print "word_len", word_len
            count = 0
            while count < word_len/2:
                # print "count", count
                temp_letter = message[word_start+count]
                # print "temp_letter", temp_letter

                message[word_start+count] = message[word_end-count]
                # print "first swap", message[word_start+count]
                message[word_end-count] = temp_letter
                # print "second swap", message[word_end-count]
                count += 1
            word_start = i+1
        else:
            continue
    # return message

    

    message = "".join(message)
    # print message

    return message


msg = "find you will pain only go you recordings security the into if"

print "from function call: ", reverse_words(msg)
reverse_words(msg)
print "msg var: ", msg 