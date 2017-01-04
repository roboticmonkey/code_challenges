def fibonacci_helper(num):

    #edge case
    if num < 0 :
        raise Exception("index was negative")

    #base case
    elif num in [0,1]:
        return num


    prev_prev = 0
    prev = 1
    

    # shouldnt this start at 2? 
    # i = 2
    # while i <= num:
    #     print "i", i
    for _ in xrange(num-1):
        total = prev_prev + prev
        # print "total", total
        prev_prev = prev
        prev = total
        # print "prev_prev", prev_prev
        # print "prev", prev
        
        # i+=1
    
    return total
    
class Fibber:

    def __init__(self):
        self.memo = {}


    def fib(self, n):
        #edge case
        if n < 0: 
            raise Exception("index was negative.")

        #base case
        elif n in [0,1]:
            return n

        #see if we've calculated this
        if n in self.memo:
            print "grabbing memo[%i]" % n
            return self.memo[n]

        print "computing fib(%i)" % n
        result = self.fib(n-1) + self.fib(n-2)

        #memoize
        self.memo[n] = result

        return result

# print fibonacci_helper(0)
# print fibonacci_helper(1)
# print fibonacci_helper(2)
print fibonacci_helper(8)

print Fibber().fib(8)


