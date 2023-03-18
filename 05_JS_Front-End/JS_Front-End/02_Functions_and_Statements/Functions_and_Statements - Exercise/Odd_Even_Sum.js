function func(num) {
  let evenSum = 0;
  let oddSum = 0;
  let digit;

  num.toString().split('').forEach(function(digitChar) {
    digit = parseInt(digitChar);

    if (digit % 2 === 0) {
      evenSum += digit;
    } else {
      oddSum += digit;
    }
  });

  console.log(`Odd sum = ${oddSum}`);
  console.log(`Even sum = ${evenSum}`);
}
func(1000435);