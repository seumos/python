#Maria Customer database

first_names = ["Ainsley", "Ben", "Chani", "Depak"]

# Let add customers sizes.
preferred_size = ["Small", "Large", "Medium"]

# Add append
preferred_size.append("Medium")
print(preferred_size)

# Add boolean data
customer_data = [["Ainsley", "Small", True ], ["Ben", "Large", False ], ["Chani", "Medium", True ], ["Depak", "Medium", False ]]
print(customer_data)

# Modification of preference
customer_data[2][2] = (False)

#Using .remove
customer_data[1].remove (False)

#Updated Customer data
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
