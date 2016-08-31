"""code to find intersecting rectangles"""

def rect_intersection(rect_1, rect_2):
    """Finds the overlapping rectangle of 2 rectangles as dictionaries

    >>> rect_1 = {'left_x':1, 'bottom_y':1, 'width': 11, 'height':13,}
    >>> rect_2 = {'left_x':6, 'bottom_y':3, 'width':11, 'height':9,}
    >>> rect_intersection(rect_1, rect_2)
    {'width': 6, 'left_x': 6, 'bottom_y': 3, 'height': 9}

    >>> rect_1 = {'left_x':1, 'bottom_y':1, 'width': 4, 'height':13,}
    >>> rect_2 = {'left_x':6, 'bottom_y':3, 'width':11, 'height':9,}
    >>> rect_intersection(rect_1, rect_2)
    {}

    >>> rect_1 = {'left_x':1, 'bottom_y':1, 'width': 5, 'height':13,}
    >>> rect_2 = {'left_x':6, 'bottom_y':3, 'width':11, 'height':9,}
    >>> rect_intersection(rect_1, rect_2)
    {}

    >>> rect_1 = {'left_x':1, 'bottom_y':1, 'width':11, 'height':13,}
    >>> rect_2 = {'left_x':6, 'bottom_y':3, 'width':5, 'height':9,}
    >>> rect_intersection(rect_1, rect_2)
    {'width': 5, 'left_x': 6, 'bottom_y': 3, 'height': 9}

    """
    
    overlap ={}

    x_overlap = find_overlap_range(rect_1['left_x'],
                                    rect_1['width'], 
                                    rect_2['left_x'], 
                                    rect_2['width']) 
    # print x_overlap
    
    y_overlap = find_overlap_range(rect_1['bottom_y'],
                                    rect_1['height'], 
                                    rect_2['bottom_y'], 
                                    rect_2['height'])
    # print y_overlap

    if x_overlap and y_overlap:
        overlap['left_x'] = x_overlap[0]
        overlap['bottom_y'] = y_overlap[0]
        overlap['width'] = x_overlap[1]
        overlap['height'] = y_overlap[1]
    
    return overlap

def find_overlap_range(x1, lenght1, x2, length2):
    """ finds the overlap range between 4 points. returns the overlap start point
            and the length of the overlap 

    >>> find_overlap_range(1, 11, 6, 15)
    (6, 6)

    >>> find_overlap_range(1, 5, 6, 10)

    >>> find_overlap_range(9, 10, 5, 15)
    (9, 10)

    """


    highest_start_point = max(x1, x2)
    lowest_end_point = min(x1 + lenght1, x2 + length2)
    
    if highest_start_point >= lowest_end_point:
        return None
    
    overlap_length = lowest_end_point - highest_start_point
        
    return (highest_start_point, overlap_length)

def overlap_list_rect(list_rects):
    """finds the single overlap of a list rectangles

    >>> rect_1 = {'left_x':1, 'bottom_y':1, 'width': 11, 'height':13,}
    >>> rect_2 = {'left_x':6, 'bottom_y':3, 'width':11, 'height':9,}
    >>> rect_3 = {'left_x':4, 'bottom_y':9, 'width': 12, 'height':12,}
    >>> rect_4 = {'left_x':9, 'bottom_y':6, 'width': 14, 'height':10,}
    >>> rect_list = [rect_1, rect_2, rect_3, rect_4]
    >>> overlap_list_rect(rect_list)
    {'width': 3, 'left_x': 9, 'bottom_y': 9, 'height': 3}

    >>> rect_1 = {'left_x':1, 'bottom_y':1, 'width': 2, 'height':13,}
    >>> rect_2 = {'left_x':6, 'bottom_y':3, 'width':11, 'height':9,}
    >>> rect_3 = {'left_x':4, 'bottom_y':9, 'width': 12, 'height':12,}
    >>> rect_4 = {'left_x':9, 'bottom_y':6, 'width': 14, 'height':10,}
    >>> rect_list = [rect_1, rect_2, rect_3, rect_4]
    >>> overlap_list_rect(rect_list)
    {}

    >>> rect_1 = {'left_x':3, 'bottom_y':1, 'width': 2, 'height':4,}
    >>> rect_2 = {'left_x':6, 'bottom_y':1, 'width':4, 'height':5,}
    >>> rect_3 = {'left_x':1, 'bottom_y':6, 'width': 5, 'height':4,}
    >>> rect_list = [rect_1, rect_2, rect_3]
    >>> overlap_list_rect(rect_list)
    {}


    """
    overlap = {}
    x_points = []
    y_points = []

    for rect in list_rects:
        x_points.append([rect['left_x'], rect['width']])
        y_points.append([rect['bottom_y'], rect['height']])

    x_overlap = find_overlap_range_list(x_points)

    y_overlap = find_overlap_range_list(y_points)

    if x_overlap and y_overlap:
        overlap['left_x'] = x_overlap[0]
        overlap['bottom_y'] = y_overlap[0]
        overlap['width'] = x_overlap[1]
        overlap['height'] = y_overlap[1]
    
    return overlap

def find_overlap_range_list(points_list):
    highest_start_point = points_list[0][0]
    lowest_end_point = points_list[0][0] + points_list[0][1]

    for point in points_list[1:]:
        highest_start_point = max(highest_start_point, point[0])
        lowest_end_point = min(lowest_end_point, point[1]+point[0])

    if lowest_end_point <= highest_start_point:
        return None

    return [highest_start_point, lowest_end_point - highest_start_point]





# rect_1 = {'left_x':1, 'bottom_y':5, 'width': 10, 'height':4,}
# rect_2 = {'left_x':7, 'bottom_y':8, 'width': 7, 'height':5,}
# print rect_intersection(rect_1, rect_2)
# rect_2 = {'left_x':1, 'bottom_y':4, 'width': 10, 'height':7,}
# rect_1 = {'left_x':7, 'bottom_y':5, 'width': 2, 'height':5,}
# print rect_intersection(rect_1, rect_2)
# rect_2 = {'left_x':1, 'bottom_y':1, 'width': 4, 'height':7,}
# rect_1 = {'left_x':7, 'bottom_y':1, 'width': 3, 'height':4,}
# print rect_intersection(rect_1, rect_2)
# rect_2 = {'left_x':1, 'bottom_y':1, 'width': 4, 'height':7,}
# rect_1 = {'left_x':5, 'bottom_y':1, 'width': 3, 'height':4,}
# print rect_intersection(rect_1, rect_2)



# rect_1 = {'left_x':1, 'bottom_y':1, 'width': 11, 'height':13,}
# rect_2 = {'left_x':17, 'bottom_y':3, 'width':9, 'height':6,}
# rect_3 = {'left_x':4, 'bottom_y':9, 'width': 12, 'height':12,}
# rect_4 = {'left_x':9, 'bottom_y':6, 'width': 14, 'height':10,}
# rect_list = [rect_1, rect_2, rect_3, rect_4]

# print overlap_list_rect(rect_list)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
