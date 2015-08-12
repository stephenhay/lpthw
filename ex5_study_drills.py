name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

weight_in_kg = weight / 2.2
height_in_cm = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "(That's %d centimeters)" % height_in_cm
print "He's %d pounds heavy." % weight
print "(That's %d kilograms)" % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# String formatting
# `s` is string, but none is the same as `s`?
# print "Can we say % is a string?" % name
# No that doesn't work: official python docs are a pain to read.
# `b` = binary
# `c` = convert integer to unicode char
# `d` = Base 10 decimal integer
# `o` = Octal format (base 8)
# `x` = Hex format (base 16, lowercase)
# `X` = Hex format (base 16, uppercase)
# `n` = number. Same as `d` but separator chars determined by locale setting
# `r` = representation of object.
