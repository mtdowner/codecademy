# Weight of package in lbs
weight = 4.83

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight <= 10:
  cost_ground = weight * 4.00 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00

print("Ground Shipping: $", round(cost_ground, 3))

# Ground Premium is a flat rate
cost_premium = 125.00

print("Ground Shipping Premium: $", round(cost_premium, -2))

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $", round(cost_drone, 3))p