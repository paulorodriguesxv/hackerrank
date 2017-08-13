from collections import OrderedDict

array = [5, 3, 7, 0, 1, 4, 2]
t = 3

pairs = OrderedDict()

for value in array:

    number = pairs.get(value)
    if number or number == 0:
        print "pair %d, %d has sum T=%d" % (pairs[value], value, t)
    else:
        pairs[t-value] = value

