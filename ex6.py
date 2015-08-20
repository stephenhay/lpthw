# replace %d with 10 and assign to x
x = "There are %d types of people." % 10
# assign the string to the variable binary
binary = "binary"
# assign "don't" to the variable do_not
do_not = "don't"
# replace the two %s's with the strings between parens,
# and assign the resulting string to variable y
y = "Those who know %s and those who %s." % (binary, do_not)

# print x and y
print x
print y

# replace %r with the raw data from x, then print
print "I said: %r." % x
# replace %s with the string y, then print
print "I also said: '%s'." % y

# assign False to hilarious
hilarious = False
# assign string (which contains a format variable) to joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# pass raw data of hilarious into joke_evaluation and then print
print joke_evaluation % hilarious

# assign strings to w and e
w = "This is the left side of..."
e = "a string with a right side."

# combine w and e, then print
print w + e
