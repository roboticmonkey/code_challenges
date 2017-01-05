
def which_appears_twice(list_of_nums):

    ideal_sum = 0
    for i in xrange(1, len(list_of_nums)+1):
        ideal_sum += i

    lst_sum = 0

    for n in list_of_nums:
        lst_sum += n

    off_by = ideal_sum - lst_sum

    return len(list_of_nums) - off_by

a_list = [1,2,3,4,5,6,7,8,9,9]
b_list = [1,1,2,3,4,5,6,7,8,9]
c_list = [1,2,3,4,5,6,7,8,9,10,11,12,12,13,14,15]

print which_appears_twice(a_list)
print which_appears_twice(b_list)
print which_appears_twice(c_list)