from sys import argv

# script, first, second, third = argv

# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third

script, one, two = argv
print "What is the name of this script?", script
print "First parameter is:", one
print "2nd parameter is:", two
print "Thank you %s" % one
z = raw_input("What's your name: ")
print z,
