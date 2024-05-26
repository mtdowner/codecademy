# Len's Slice

You work at Len's Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

## Tasks

### Make Some Pizzas

1. To keep track of the kinds of pizzas you sell, create a list called `toppings` that holds the following:

```py
"pepperoni"
"pineapple"
"cheese"
"sausage"
"olives"
"anchovies"
"mushrooms"
```

---
**Hint**

It should look something like:

```py
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
```

---

2. To keep track of how much each kind of pizza slice costs, create a list called `prices` that holds the following integer values:

```py
2
6
1
3
2
7
2
```

---
**Hint**

You don't need the quotes when you are dealing with integers:

```py
prices = [2, 6, 1, 3, 2, 7, 2]
```

---

3. Your boss wants you to do some research on $2 slices.

Count the number of occurrences of 2 in the `prices` list, and store the result in a variable called `num_two_dollar_slices`. Print it out.

---
**Hint**

You can use `.count` to find the number of occurrences of a value in a list:

```py
my_list = ["a", "a", "b"]

number_of_as = my_list.count("a")
# number_of_as is 2
```

---

4. Find the length of the `toppings` list and store it in a variable called `num_pizzas`.

```
**Hint**

You can use `len()` to find the `length` of a list:

```py
len(toppings)
```

---

5. Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.

---
**Hint**

To add a variable to a string, you can use the syntax:

```py
"My age is " + str(my_age)
```

> Note: You have to cast the number as a string before you add it to another string!

The output should look like:

```
We sell 7 different kinds of pizza!
```

---

6. Use the existing data about the pizza toppings and prices to create a new two-dimensional list called `pizza_and_prices`.

Each sublist in `pizza_and_prices` should have one pizza topping and an associated price.

```py
Price	Topping
2	"pepperoni"
6	"pineapple"
1	"cheese"
3	"sausage"
2	"olives"
7	"anchovies"
2	"mushrooms"
```

For this new list make sure the prices come before the topping name like so:

```py
[price, topping_name]
```

> Note: You don’t need to use your original toppings and prices lists in this exercise. Create a new two-dimensional list from scratch.

---
**Hint**

Your first sublist in the two-dimensional list would look like this:

```py
[2, "pepperoni"]
```

---

7. Print `pizza_and_prices`.

Does it look the way you expect?

---
**Hint**

The output should look like:

```py
[[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
```

---

### Sorting and Slicing Pizzas

8. Sort `pizza_and_prices` so that the pizzas are in the order of increasing price (ascending).

---
**Hint**

You can sort a list from low to high by using `.sort()`:

```py
my_list.sort()
```

When sorting a two-dimensional list using `.sort()`, the list by default will be sorted by the first element in each sublist. In this case, this will mean it is sorted by the price.

---

9. Store the first element of `pizza_and_prices` in a variable called `cheapest_pizza`.

---
**Hint**

To get an element of a list, use the syntax `list[n]`, where `n` is the index of the item you want to get. Remember that list indices start at zero!

```py
second_item = your_list[1]
```

---

10. A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”

Get the last item of the `pizza_and_prices` list and store it in a variable called `priciest_pizza`.

---
**Hint**
To get the last element of a list, use the syntax `list[-1]`

```py
last_item = your_list[-1]
```

---

11. It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our `pizza_and_prices` list since the man bought the last slice.

---
**Hint**

To remove the last element of a list, use the `.pop()` method.

---

12. Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. Here is what your new topping looks like:

```py
[2.5, "peppers"]
```

Add the new peppers pizza topping to our list pizza_and_prices.

> Note: Make sure to position it relative to the rest of the sorted data in `pizza_and_prices`, otherwise our data will not be correctly sorted anymore!

---
**Hint**

Since the new pizza has a price of 2.5, it should come after `[2, "pepperoni"]` but before `[3, "sausage"]`.

You can use the `.insert()` method to insert an element at a specific index.

---

13. Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

Slice the `pizza_and_prices` list and store the 3 lowest cost pizzas in a list called `three_cheapest`.

---
**Hint**

To get the first `n` items of a list, use `list[:n]`. For example:

```py
new_list = my_list[:2]
```

would store the first two items of `my_list` in `new_list`.

---

14. Great job! The mice are very pleased and will be leaving you a 5-star review.

Print the `three_cheapest` list.