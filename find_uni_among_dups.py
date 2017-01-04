def find_unique_id_among_dups(delivory_ids):

    unique_id = 0

    for delivory_id in delivory_ids:
        unique_id ^= delivory_id

    return unique_id


delivory_ids = [123, 421, 7923, 123, 321, 421, 321, 89742, 89742]
print find_unique_id_among_dups(delivory_ids)