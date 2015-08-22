tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\n Here we try out some escape sequences:"
print "Backslash: \\"
print "Single quote: \'"
print "Double quote: \""
print "ASCII bell: \a"
print "ASCII backspace:\b"
print "ASCII formfeed: \f"
print "ASCII linefeed: \n"
print "Return: \rhere"
print "\tTab"
print u"Unicode number: \u203C"
print "Vertical\vtab"

print "And here's a study drill:"
symbol = "\N{TIRED FACE}"
print u"This is what I look like when I'm tired: %s" % symbol
print "Hmm. That didn't work."
