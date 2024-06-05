# Getting Ready for Physics Class

You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.

If you get stuck during this project or would like to see an experienced developer work through it, click "**Get Unstuck**" to see a **project walkthrough video**.

### Tasks

0/13 complete

Mark the tasks as complete by checking them off

## Turn up the Temperature

1. Write a function called `f_to_c` that takes an input `f_temp`, a temperature in Fahrenheit, and converts it to `c_temp`, that temperature in Celsius.

It should then return `c_temp`.

The equation you should use is:

```py
Temp (C) = (Temp (F) - 32) * 5/9
```

Hint

To define a function with an input, use this syntax:

```py
def your_function(your_input):
... # do something with the input
return some_final_value
```

2. Let's test your function with a value of 100 Fahrenheit.

Define a variable `f100_in_celsius` and set it equal to the value of `f_to_c` with `100`as an input.

Hint

To call a function use the syntax:

```py
returned_value = your_function(your_input)
```

3. Write a function called `c_to_f` that takes an input `c_temp`, a temperature in Celsius, and converts it to `f_temp`, that temperature in Fahrenheit.

It should then return `f_temp`.

The equation you should use is:

```py
Temp (F) = Temp (C) * (9/5) + 32
```

4. Let's test your function with a value of 0 Celsius.

Define a variable `c0_in_fahrenheit` and set it equal to the value of `c_to_f` with `0`as an input.

Hint

You can `print()` the value of `c0_in_fahrenheit` to check that it equals `32.0`.

## Use the Force

5. Define a function called `get_force` that takes in `mass` and `acceleration`. It should return `mass` multiplied by `acceleration`.

6. Test `get_force` by calling it with the variables `train_mass` and `train_acceleration`.

Save the result to a variable called `train_force` and print it out.

`train_mass` and `train_acceleration` have been defined for you at the top of **script.py**. Make sure to uncomment those lines before trying to use these variables.

Hint

If you've set up `get_force()` correctly, `train_force` should equal `226800`.

7. Print the string "The GE train supplies X Newtons of force.", with `X` replaced by `train_force`.

8. Define a function called `get_energy` that takes in `mass` and `c`.

`c` is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set `c` to have a default value of `3*10**8`.

`get_energy` should return `mass` multiplied by `c` squared.

9. Test `get_energy` by using it on `bomb_mass`, with the default value of `c`. Save the result to a variable called `bomb_energy`.

`bomb_mass` has been defined for you at the top of **script.py**. Make sure to uncomment this line before trying to use `bomb_mass`.

Hint

Bombs have a lot of energy: `90000000000000000` of it.

10. Print the string `"A 1kg bomb supplies X Joules."`, with `X` replaced by `bomb_energy`.

## Do the Work

11. Define a final function called `get_work` that takes in `mass`, `acceleration`, and `distance`.

Work is defined as force multiplied by distance. First, get the `force` using `get_force`, then multiply that by `distance`. Return the result.

Hint

To call `get_force`, use `mass` and `acceleration` as inputs. Do this inside the `get_work`function.

12. Test `get_work` by using it on `train_mass`, `train_acceleration`, and `train_distance`. Save the result to a variable called `train_work`.

13. Print the string `"The GE train does X Joules of work over Y meters."`, with `X`replaced with `train_work` and `Y` replaced with `train_distance`.

Hint

Remember to cast `train_work` and `train_distance` to strings using `str()` before concatenating.

The GE train does `22680000` Joules of work over `100`, by the way.