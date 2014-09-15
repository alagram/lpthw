def loooop(n, inc):
    i = 0
    numbers = []

    for i in range(0, n):
        print "At the top i is %d" % i
        numbers.append(i)

        # i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num

loooop(6, 2)
