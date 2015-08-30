# import argv from sys module
from sys import argv

# set script and filename variables to the arguments entered when run
script, filename = argv

# open the file entered as `filename`
txt = open(filename)

# print the name of file, read the contents and print them
print "Here's your file %r:" % filename
print txt.read()

# ask for the filename again
print "Type the filename again:"
file_again = raw_input("> ")

# open, read, and print the content of the file again
txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
