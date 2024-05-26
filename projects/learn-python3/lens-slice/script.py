toppings = ["pepperoni",
"pineapple",
"cheese",
"sausage",
"olives",
"anchovies",
"mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [[2,"pepperoni"],
[6, "pineapple"],
[1, "cheese"],
[3, "sausage"],
[2, "olives"],
[7, "anchovies"],
[2, "mushrooms"]]

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

# 12 Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:
# [2.5, "peppers"]
# Add the new peppers pizza topping to our list pizza_and_prices.

pizza_and_prices.insert(3,[2.5, "celery"]) 
print(pizza_and_prices)

# 13 Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas. Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.

three_cheapest = pizza_and_prices[:3]

# 14 Great job! The mice are very pleased and will be leaving you a 5-star review. Print the three_cheapest list.
print(three_cheapest)

