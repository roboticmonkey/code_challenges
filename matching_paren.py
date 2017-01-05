

def find_match_paren(string, position):

    """ when given the position of the first parenthisis 
        returns the position of the matching parenthisis. """

    num_of_paren = 0

    for i in xrange(position +1, len(string)):
        
        if string[i] == "(":
            num_of_paren += 1

        if string[i] == ")":
            if num_of_paren == 0:
                return i
            else:
                num_of_paren -= 1


    return "No Match"

str1 = "this (is (one way) of ( driving) me crazy) blah"

str2 = "((())())"

print find_match_paren(str1, 5)
print find_match_paren(str2, 2)