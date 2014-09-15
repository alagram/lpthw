from sys import argv

script, filename = argv
test = open(filename, 'r+')
test.read()
test.close()
