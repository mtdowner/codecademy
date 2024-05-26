// The value will remain constant.
const kelvin = 293;
// Convert Kelvin to Celsius by subtracting 273 from the kelvin variable.
let celsius = kelvin - 273;
// Use the equation to calculate Fahrenheit and store in variable:
let fahrenheit = celsius * (9 / 5) + 32;
// use the built-in Math object .floor() to round down the decimal and save the result to fahrenheit variable.
fahrenheit = Math.floor(fahrenheit);

console.log(
  "When the temperature is " +
    kelvin +
    " degrees in Kelvin, it will convert to these temperatures:"
);
console.log("The temperature is " + fahrenheit + " degrees Fahrenheit.");
console.log("The temperature is " + celsius + " degrees in Celsius.");

let newton = celsius * (33 / 100);
newton = Math.floor(newton);
console.log("And it is " + newton + " degrees in Newton!");
