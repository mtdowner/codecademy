import random

# enter your name
name = "Missy"
# ask your question
question = "Will I become a German Shepherd farmer when I grow up?"
answer = ""

random_number = random.randint(1, 10)
# print(random_number)	

if random_number == 1:
  answer = "Yes - definitely. Maybe."
elif random_number == 2:
  answer = "It is decidedly so, probably."
elif random_number == 3:
  answer = "Without a doubt, most likely."
elif random_number == 4:
  answer = "Reply hazy, try again when I'm not so tired."
elif random_number == 5:
  answer = "Ask again when I wake up."
elif random_number == 6:
  answer = "Better not tell you now..."
elif random_number == 7:
  answer = "My sources say that's a big fat nope."
elif random_number == 8:
  answer = "Outlook not so good..."
elif random_number == 9:
  answer = "Very doubtful, but who knows?"
elif random_number == 10:
  answer = "You betcha!"
else:
  answer = "Uh oh, spaghetti-os! My psychic powers are broken. Please try again."

if name == "":
  print("Oh beautiful ball, with your magical wisdom, riddle me this: " + question)
if question == "":
  print("You broke my powers! Feed me a question to unbreak them.")
else:
  print(name + " asks: " + question)
  print("Magic 8 Ball's answer: " + answer)
