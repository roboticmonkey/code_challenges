
# recursive version. 
# possible stack overflow problem

class Change:

    def __init__(self):
        self.memo = {}

    def change_top_down(self, amount_left, coins, current_index=0):

        # check our memo and short-circut if we've already solved it
        memo_key = str((amount_left, current_index))

        if memo_key in self.memo:
            print "grabbing memo[%s]" % memo_key
            return self.memo[memo_key]

        #base cases:
        # we hit right on
        if amount_left == 0:
             return 1

        #we went over
        if amount_left < 0:
            return 0

        # we are out of coins
        if current_index == len(coins): return 0

        print "checking ways to make %i with %s" %(amount_left, coins[current_index:])

        # choose a current coin
        current_coin = coins[current_index]

        #see how many possibilties we can get
        # for each number of times to use current coin
        num_possiblities = 0
        while amount_left >= 0:
            num_possiblities += self.change_top_down(amount_left, coins, current_index +1)
            amount_left -= current_coin

        #save the answer in our memo so we dont compute it again
        self.memo[memo_key] = num_possiblities
        return num_possiblities

change = Change()

#print change.change_top_down(4, [1,2,3])

# iterative version, bottom up greedy algorithym

def make_change(amount, coins):

    ways_of_making_n_cents = [0] * (amount + 1)

    for coin in coins:
        
        for sub_amount in xrange(coin, amount +1):
            sub_amount_remainder = sub_amount - coin
            if sub_amount_remainder == 0:
                ways_of_making_n_cents[sub_amount] += 1
            
            ways_of_making_n_cents[sub_amount] += ways_of_making_n_cents[sub_amount_remainder]
            
    return ways_of_making_n_cents[amount]

print make_change(4, [1,2,3])
print make_change(10, [5,2,3,6])
print make_change(0, [1,2,3])
