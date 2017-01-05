

def merge_sorted_lists(list1, list2):

    """ takes two sorted lists and returns one sorted list"""

    new_list = []

    index1 = 0
    index2 = 0

    while (index1 < len(list1)) and (index2 < len(list2)):

        if list1[index1] < list2[index2]:
            new_list.append(list1[index1])
            index1 += 1
        else:
            new_list.append(list2[index2])
            index2 += 1

    if index1 < len(list1):
        new_list.extend(list1[index1: ])
    else:
        new_list.extend(list2[index2: ])

    return new_list


def merge_sorted_lists_of_lists(lists):

    """merges a list of sorted lists, returns one list"""


    merged_list = []

    index = 0

    while index < len(lists):

        merged_list = merge_sorted_lists(merged_list, lists[index])
        index += 1

    return merged_list



list1 = [3,4,6,10,11,15]
list2 = [1,5,8,12,14,19]

print merge_sorted_lists(list1, list2)


list3 = [1,3,4,5,6,9]
list4 = [10,13,15,43,45]
print merge_sorted_lists(list3, list4)

list5 = [3,4,6,10,11,15]
list6 = [1,5,8,12,14,19]
list7 = [2,7,17,22,36,37,39]
list8 = [9,13,20,43,45]
list9 = [16,18,21,25,30]

print merge_sorted_lists_of_lists([list5,list6,list7,list8])
print merge_sorted_lists_of_lists([list5,list6,list7,list8, list9])