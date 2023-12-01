const fs = require("fs");

const lines = fs.readFileSync("input.txt", "utf8").split(/\n/);

let sum = 0;
for (const line of lines) {
  const numbers = line.match(/\d/g);

  if (!numbers) {
    continue;
  }

  let firstNumber = numbers[0];
  let lastNumber = numbers[numbers.length - 1];

  sum += +firstNumber * 10 + +lastNumber;
}

console.log(sum);
