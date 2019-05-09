# Assign the value 100 to the variable cars.
cars = 100
# Assign the value 4 to the variable space_in_a _car.
space_in_a_car = 4
# Assign the value 30 to the variable drivers.
drivers = 30
# Assign the value 90 to the variable passengers.
passengers = 90
# Calculate the number of cars without drivers.
cars_not_driven = cars - drivers
# Calculate the number of cars with drivers.
cars_driven = drivers
# Calculate the number of passengers that can be transported.
carpool_capacity = cars_driven * space_in_a_car
# Calculate the average number of passengers per car.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")