def max_duffel_bag_value(cake_tuples, weight_capacity):

    #list to hold the maximum possible value at every
    #integer capacity from 0 to wieght_capacity
    #starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    # every integer from 0 to the input weight_capacity
    
    for current_capacity in xrange(weight_capacity + 1):
        current_max_value = 0
        for cake_weight, cake_value in cake_tuples:

            # id the cake wighs as much or less than the current capacity
            # see what our max value could be if we took it!

            if cake_weight <= current_capacity:
                #find max_value_using_cake
                # num_times = current_capacity / cake_weight
                # value = num_times * cake_value

                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]

                current_max_value = max(max_value_using_cake, current_max_value)

        max_values_at_capacities[current_capacity] = current_max_value
        # print max_values_at_capacities
    #return max monetary value the bag can hold
    return max_values_at_capacities[-1]

cake_tuples = [(7, 160), (3, 90), (2,15)]
max_weight = 20

print max_duffel_bag_value(cake_tuples, max_weight)

cake_tuples = [(3, 40), (5, 70)]
max_weight = 9

print max_duffel_bag_value(cake_tuples, max_weight)

cake_tuples = [(3, 40), (5, 70)]
max_weight = 0

print max_duffel_bag_value(cake_tuples, max_weight)

cake_tuples = [(0, 0), (5, 70)]
max_weight = 10

print max_duffel_bag_value(cake_tuples, max_weight)

cake_tuples = [(0, 0), (5, 70)]
max_weight = 0

print max_duffel_bag_value(cake_tuples, max_weight)