const fs = require("fs");

const lines = fs.readFileSync("input.txt", "utf8").split(/\n/);

const numberMappings = {
  one: "1",
  two: "2",
  three: "3",
  four: "4",
  five: "5",
  six: "6",
  seven: "7",
  eight: "8",
  nine: "9",
};

let sum = 0;
for (const line of lines) {
  const regexLetterToNumber = Object.keys(numberMappings).join("|");
  const numbers = line.match(new RegExp(`\\d|${regexLetterToNumber}`, "g"));

  if (!numbers) {
    continue;
  }

  let firstNumber = numbers[0];
  let lastNumber = numbers[numbers.length - 1];

  if (firstNumber in numberMappings) {
    firstNumber = numberMappings[firstNumber];
  }

  if (lastNumber in numberMappings) {
    lastNumber = numberMappings[lastNumber];
  }

  sum += +firstNumber * 10 + +lastNumber;
}

console.log(sum);
