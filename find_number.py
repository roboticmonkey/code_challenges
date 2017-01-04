def find_number(lst, num):
    # write the body of your function here
    upper_bound = len(lst)-1
    lower_bound = 0
    
    while ((upper_bound - lower_bound)/2) != 0 :
        # print "upper bound", upper_bound
        # print "lower bound", lower_bound

        check_idx = ((upper_bound - lower_bound)/2) + lower_bound
        # print "check index", check_idx
        
        if num == lst[check_idx]:
            return True
        elif num > lst[check_idx]:
            lower_bound = check_idx
        else:
            upper_bound = check_idx

        # print "upper bound", upper_bound
        # print "lower bound", lower_bound
    
    return False
        

# run your function through some test cases here
# remember: debugging is half the battle!
print find_number([1,3,5,7,8,9], 3)
print find_number([2,4,5,6,7,9,11], 12)