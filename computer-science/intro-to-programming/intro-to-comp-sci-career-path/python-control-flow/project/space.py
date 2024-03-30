print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  weight = .91 * weight
if planet == 2:
  weight = .38 * weight
if planet == 3:
  weight = 2.34 * weight
if planet == 4:
  weight = 1.06 * weight
if planet == 5:
  weight = .92 * weight
if planet == 6:
  weight = 1.19 * weight

print("Drumroll please!")
print("...")
print("Your new weight is: ", weight)