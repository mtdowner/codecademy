# Console Game

## Project Goals
In this project, you’ll write C# methods to create a game in your console. The game engine is provided for you, but it expects you to define four methods. Each one determines how some part of the game will work. You’ll run your code using `dotnet run` in the console.

## Setup Instructions
If you choose to do this project on your computer instead of Codecademy, you can download what you’ll need by clicking the “Download” button below. If you’re using Visual Studio, you’ll define the methods in Game.cs and run the code to see your game in action. If you need help setting up on your own computer, read our article about running C# with Visual Studio Community.

[Download](https://content.codecademy.com/PRO/independent-practice-projects/csharp-console-game/Console-Game-Starting.zip?_gl=1*11t3t35*_ga*MTg0NTE1MzgyNi4xNzA1OTYxNzM0*_ga_3LRZM6TM9L*MTcwNzk2NzkwNS43LjEuMTcwNzk2ODM5OC4yOC4wLjA.)

## Tasks

### Prerequisites

1. In order to complete this project, you should have completed the first 4 sections of [Learn C#](https://www.codecademy.com/learn/learn-c-sharp) (through Learn C#: Methods).

### Project Requirements

2. You’ll write four methods in `Game.cs`. The game engine is written in `Program.cs`, which will call your methods as needed. As you complete this project, make sure that all of your methods are named exactly as specified so that they can be called correctly when the game is played.

You don’t need to edit `Program.cs` to get your game working.

Check the GIF below to get a sense of what you’ll be building. Start the game with dotnet run. In the game, you control the character with the keyboard. Up moves the character up, left moves the character left, etc. Close the game by pressing `Q` or `CTRL + C`

![Console game preview](https://content.codecademy.com/PRO/independent-practice-projects/csharp-console-game/console-game-preview.gif)

---
**Hint**

If you’re curious about the other files:

- `Program.cs` contains the `Main()` method. When you type `dotnet run`, `Main()` is invoked. It uses the methods you will define in `Game.cs`
- `Game.cs` defines a Game class. Its methods define how the game works, and they are called by `Main()`
- `SuperGame.cs` defines a SuperGame class, which is the base class of Game. This allows your game to run even if you haven’t defined all of the methods in Game. Base classes and inheritance are explained in later C# lessons
- `ConsoleGame.csproj` defines configuration settings for the project, like what version of dotnet to use, where to print output, etc

---

3. Create an `UpdatePosition()` method. This method will be used to change the position of the character based on keyboard input. The method should:

- have the public new static modifiers
- return nothing
- have three arguments: a string representing the key pressed, an `int` representing the change in the x coordinate, and an `int` representing the change in the y coordinate
- have the last two parameters labeled with out

In the method, you should set the value of the two `int` arguments based on the `string` value. For example: if the `string` is "`DownArrow`", the x coordinate should change by `0` units and the y coordinate should be increased by `1` unit.

(You’ll notice that the y-axis is “flipped”. That’s because the origin, or (0,0) point, is in the top-left!)

---
**Hint**

The string can take many values, including:

```
"LeftArrow"
"RightArrow"
"UpArrow"
"DownArrow"
"Spacebar"
```

Within the method, consider using a `switch` statement.

For out parameters, remember that:

- The `out` parameter must have the `out` keyword and its expected type in the method declaration
- The `out` parameter must be set to a value before the method ends

---

4. Create an `UpdateCursor()` method. It will allow the player icon to change with each keypress. Its input will be the key pressed and it will return a symbol that represents the player. The method should:

- have the public new static modifiers
- return a char
- have one argument: a string representing the key pressed

In our example GIF we used the following mapping:

```
"LeftArrow" : '<'
"RightArrow" : '>'
"UpArrow" : '^'
"DownArrow" : 'v'
```

---
**Hint**

If you’re having trouble finding these symbols here they are by name:

- `<` — less than
- `>` — greater than
- `^` — caret
- `v` — lowercase v

Within the method, consider using a `switch` statement.

---

5. Create a `KeepInBounds()` method. Without this method, hitting the boundaries will break the game!

Every time a key is pressed, it will be called twice: once for x and once for y. The method will constrain a coordinate between 0 and its maximum value to keep the character from going off-screen.

The method should:

- have the public new static modifiers
return an `int`
- have two arguments: an `int` representing the coordinate, and an `int` representing the maximum value

Here’s how the method will be used. Imagine that the x-coordinate has a maximum of `10` (exclusive), so it should only take values from `0` through `9`:

```
// newX will be 1
newX = KeepInBounds(1, 10);
// newX will be 0
newX = KeepInBounds(-1, 10);
// newX will be 9
newX = KeepInBounds(10,10);
// newX will be 9
newX = KeepInBounds(11,10);
```

---
**Hint**

Within the method, consider using an [`if-else` statement](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/if-else).

---

6. Create a `DidScore()` method. This will allow the score to increase if the character hits the `@` object — let’s call it the "fruit".

It should:

- have the public new static modifiers
return a `bool`
- have four `int` arguments: the x and y of the character, and the x and y of the “fruit”

The method will return `true` if they overlap and ``false`` otherwise. For example, if the character and “fruit” are both at (1,5), it should return `true`:

```
// scored will be true
scored = DidScore(1, 5, 1, 5);
```

If the character is instead at (1,4), it should return `false`:

```
// scored will be false
scored = DidScore(1, 4, 1, 5);
```
---
**Hint**

You can imagine that the method will be used like so:

```
if (DidScore(characterX, characterY, fruitX, fruitY))
{
  score++;
}
```

For those curious learners, you can find the actual code towards the bottom of `Program.cs`.

---

### Extensions & Solution Code

7. Great work! If you’d like to see the solution, move to the next task. If you’d like to extend your project on your own, you could consider the following:

Customize the character and controls! Maybe your character is an emoji, maybe you use W, A, S, D instead of the arrow keys.
Make the character “loop around” the bounds of the screen. If the character moves all the way right, it should reappear on the left. If the character moves all the way down, it should reappear on the top.

8. Great work! Visit our forums to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that’s okay! There are multiple ways to solve these projects, and you’ll learn more by seeing others’ code.