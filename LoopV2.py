ages = {"Lazaro": 37, "Monica": 36, "Romina": 1}
list(ages.items())
for age, quantity in ages.items():
	print("The age of {} {}.".format(age, quantity))
