from decimal import Decimal
# Calculate and print the Dutch sales tax of EUR 51.70
print "The sales tax on EUR 51.70 is: EUR ", round(Decimal(51.70 * 0.21), 2)
print "which brings the total price to: EUR ", round(Decimal(51.70 * 0.21 + 51.70), 2)

