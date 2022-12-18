# ask the client for the weight of their package
weight = float(input("Enter the weight of your package in kilograms: "))

# calculate the cost of ground shipping
if weight <= 2:
    ground_shipping_cost = 20.00 + 1.50 * weight
elif weight <= 6:
    ground_shipping_cost = 20.00 + 3.00 * weight
elif weight <= 10:
    ground_shipping_cost = 20.00 + 4.00 * weight
else:
    ground_shipping_cost = 20.00 + 4.75 * weight

# calculate the cost of drone shipping
if weight <= 2:
    drone_shipping_cost = 0.00 + 4.50 * weight
elif weight <= 6:
    drone_shipping_cost = 0.00 + 9.00 * weight
elif weight <= 10:
    drone_shipping_cost = 0.00 + 12.00 * weight
else:
    drone_shipping_cost = 0.00 + 14.25 * weight

# determine the cheapest shipping method
if ground_shipping_cost < drone_shipping_cost and ground_shipping_cost < 125.00:
    cheapest_method = "ground shipping"
    cost = ground_shipping_cost
elif drone_shipping_cost < ground_shipping_cost and drone_shipping_cost < 125.00:
    cheapest_method = "drone shipping"
    cost = drone_shipping_cost
else:
    cheapest_method = "ground shipping premium"
    cost = 125.00

# print the result
print(f"The cheapest shipping method is {cheapest_method} and it will cost ${cost:.2f} to ship your package.")
