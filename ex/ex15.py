from sys import argv

# run a script with arguments
script, filename = argv

# open a file
txt = open(filename)

print "Here's your file %r" % filename
# read a file
print txt.read()

print "Type the filename again:"
# get input from the user
file_again = raw_input("> ")

# open a file
txt_again = open(file_again)

# read a file
print txt_again.read()
print txt_again.readlines()
txt.close()
txt_again.close()
