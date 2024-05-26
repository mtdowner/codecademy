# Pseudocode and Flowcharts
Learn about how flowcharts and pseudocode are used to design algorithms!

Software development is complex and usually involves many parties working together. Therefore, planning out a project before beginning to program is essential for success.

In this article, we will take a real-world problem and attempt to design an algorithm step by step to best solve it using pseudocode and flowcharts.

Password validator
The problem
Passwords are everywhere, and we create them all the time to access a great array of services. However, it can sometimes be helpful to guide users to make stronger passwords. This can be done by imposing some restrictions on what passwords are considered valid.

If we want to set a couple of restrictions, such as that the password must be at least 8 characters and contain a number, then the following passwords would be valid:

supers3cure
james1510
meandmy2dogs
But these would not:

password
dog
hunter2
We have all seen plenty of passwords like these, so let’s come up with a simple algorithm to validate passwords like this!

The solution
First, let’s take this problem and brainstorm some steps to validate passwords that are at least 8 characters long and also contain a number:

Input the password that we plan to validate.

To keep track of the password length, establish a pass_length variable and set it to 0.

To keep track of whether the password contains a number, establish a contains_number variable and initially set it to False.

Has the entire password been searched?

If not, continue to step 5.

If so, skip to step 8.

Iterate, or move to, to the next character in password.

Increase the value of pass_length by 1.

Is the current character a number?

If not, go straight back to step 4 and continue to iterate over the entire password.

If so, set the contains_number variable to True and then go back to step 4.

Is the pass_length greater than 8 and is contain_number equal to True?

If not, then the password is invalid.

If so, then the password is valid!

Doodling a flowchart
Now that we have a framework for the task that needs to be completed, we can get to formalizing the solution. As a picture is worth a thousand words, a nice doodle can be a helpful way to communicate a complex idea — and in software development, the professional form of doodling is the flowchart!

Common flowchart symbols
Flowcharts have some standard symbols that allow them to be read and understood by a wider group of people. These are some of the most commonly-used symbols:

Terminalterminal
The terminal is an oval that indicates the beginning and end of a program. It usually contains the words Start or End.

Flowlineflowline
The flowline is a line from one symbol pointing towards another to show the process’s order of operation. This displays the flow of execution in a program.

Input/OutputInput/Outut
Input/output is represented by a rhomboid and indicates the input or output of data. This is similar to setting a value to a variable.

ProcessProcess
A process, represented by a rectangle, is an operation that manipulates data. Think of this as changing the value of a number-based variable using an operator such as +.

DecisionDecision
Decisions are represented by a rhombus and show a conditional operation that will determine which path a program should take. This is similar to conditional statements which control the flow of execution in a program.

Converting steps into symbols
Ok! Now that we have all of the steps for the algorithm figured out, let’s pair them with the relevant flowchart symbol:

INPUT/OUTPUT: Input the password that we plan to validate.

PROCESS: To keep track of the password length, establish a pass_length variable and initially set it to 0.

PROCESS: To keep track of whether the password contains a number, establish a contains_number variable and initially set it to False.

DECISION: Has the entire password been searched?

FLOWLINE: If not, continue to step 5.

FLOWLINE: If so, skip to step 8.

PROCESS: Iterate to the next character in password.

PROCESS: Increment pass_length.

DECISION: Is the current character a number?

FLOWLINE: If not, go straight back to step 4 and continue to iterate over the entire password.

PROCESS/FLOWLINE: If so, set the contains_number variable to True and then go back to step 4.

DECISION: Is the pass_length greater than 8 and is contain_number equal to True?

TERMINAL: If not, then the password is invalid.

TERMINAL: If so, then the password is valid!

Drawing the flowchart
Whew. Now that every step is associated with a symbol, we can connect them all together to put the flow into the chart!

Luckily, most steps just happen one after another, so the final product is relatively straightforward. However, do note how the iteration of the password requires the flowlines to physically loop in the flowchart:

Flowchart Solution

Progressing with pseudocode
Now that we have the entire algorithm thought out and in visual form, we can take steps to turn it into code. Some people may be able to jump right into a development environment and start hacking away, but let’s take it slow and create some pseudocode first.

Pseudocode is a description of an algorithm using everyday wording, but molded to appear similar to a simplified programming language.

To create pseudocode from what we have so far we can use the flowchart’s flowlines to guide the structure of our code as we simplify the steps we outlined earlier:

define password
create a pass_length variable and set it to 0
create a contains_number variable and set it to False
if the entire password hasn't been searched:
  iterate to the next character of the password
  increment the pass_length variable
  if the current character of the password contains number:
    set contains_number to True
if pass_length is greater than 8 and if contain_number is equal to True:
  valid password
otherwise:
  invalid password
The final code
Now the closing moments! With pseudocode in hand, the algorithm can be programmed in any language. Here it is in Python:

# 1. Input the `password` that we plan to validate
password = "c0decademy"
# 2. To keep track of the password length, establish a `pass_length` variable and initially set it to `0`
pass_length = 0
# 3. To keep track of if the password contains a number, establish a `contains_number` variable and initially set it to `False`
contains_number = False
# 4. Has the entire `password` been searched?
while pass_length is not len(password):
  # 5. Iterate to the next character in `password`
  current_character = password[pass_length]
  # 6. Increment `pass_length`
  pass_length = pass_length + 1
  # 7. Is the current character a number?
  if current_character.isdigit():
    # If so, set the `contains_number` variable to `True` and then go back to step 4
    contains_number = True
    
# 8. Is the `pass_length` greater than `8` and is `contain_number` equal to `True`?
if pass_length > 8 and contains_number is True:
  # If so, then the `password` is valid!
  print("Valid Password!")
else:
  # If not, then the `password` is invalid
  print("Invalid Password")

Even if this code seems foreign, the power of flowcharts and pseudocode shines through. It allows people, regardless of technical expertise, to communicate algorithms and other technical solutions. These ideas can then be implemented in whatever technologies work best, and the notes can be kept around in case the algorithm needs to be reimplemented in different technologies in the future.

Wrapping up
Awesome job on making it to the end of this article! While this was mainly a practical article, here is what we learned:

Pseudocode is a description of an algorithm using everyday wording, but molded to appear similar to a simplified programming language.
In code-based flowcharts, common ANSI shapes are ovals for terminals, arrows for flowlines, rhomboids for inputs and outputs, rhombuses for decisions, and rectangles for processes.
