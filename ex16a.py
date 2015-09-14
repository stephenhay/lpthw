from sys import argv

script, filename = argv


print "Opening file %r..." % filename
target = open(filename, 'r')

print "These are the contents of %r.:" % filename

contents = target.read()

print contents

print "And finally, we close it."
target.close()
