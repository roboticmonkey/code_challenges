
def river_cross(stones, jump):

    time = 0
    river = [None] * len(stones)
    monkey_pos = -1
    
    while time < max(stones):
        # print "river before looking for new stones", river
        # print "time", time
        #check for new rocks
        for idx, stone in enumerate(stones):
            # print "stone", stone
            # print "idx", idx
            
            if stone == time:
                river[idx] = True
        print "river after new stones", river
        #move forward
        i = monkey_pos+1
        # print "monkey", monkey_pos
        # print "i", i

        while i <= monkey_pos+jump and i < len(river):
            # print i
            # print "monkey", monkey_pos
            if river[i] == True:
                monkey_pos = i
                print "monkey", monkey_pos

            i +=1

        #check if monkey can cross
        print "monkey", monkey_pos
        print "time", time
        if monkey_pos + jump >= len(river):
            return time

        #increase time
        time += 1

    # if monkey cant cross
    return -1
    
def river_cross2(stones, jump):
  #doesnt work....infinete loop
    max_time = -1
    river = [None] * len(stones)
    monkey_pos = -1
    
    
    while monkey_pos+jump <= len(stones):

        min_time = None
        temp_idx = 0

        for idx, stone in enumerate(stones[monkey_pos+1:monkey_pos+jump+1]):
            print stone
            if stone > -1:
                if min_time:
                    if stone < min_time:
                        min_time = stone
                        temp_idx = idx
                    
                else:
                    min_time = stone
                    temp_idx = idx
                    
        max_time = max(max_time, min_time)
        monkey_pos = temp_idx

    print "min time", min_time
    print "max_time", max_time
    

    # if monkey cant cross
    # return max_time    

# print river_cross([1, -1, 0, 2, 3, 5], 3)
# print river_cross([-1,-1, -1, -1, -1], 2)
# print river_cross([7,0,-1, 8, 2, 4, 5, 3, -1], 4)
# print river_cross([7,-1,-1, 8, 2, 4, 5, 3, -1], 4)

# print river_cross2([1, -1, 0, 2, 3, 5], 3)

