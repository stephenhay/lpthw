# We havee 100 cars
cars = 100
# We can fit 4 people in a car
space_in_a_car = 4.0 # floating point number
# We have 30 drivers
drivers = 30
# We have 90 passengers
passengers = 90
# Cars without drivers are not driven
cars_not_driven = cars - drivers
# Number of drivers is the same as number of cars driven
cars_driven = drivers
# We can carpool space in a car times the cars driven
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers is total passengers divided by cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

