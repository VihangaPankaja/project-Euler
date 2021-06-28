/* 
  The prime factors of 13195 are 5, 7, 13 and 29.

? What is the largest prime factor of the number 600851475143
 */

function largestFactor(number) {
  let i = 2;

  while (i < number) {
    while (true) {
      if (number % i === 0 && number / i !== 1) {
        number /= i;
      } else {
        break;
      }
    }
    i++;
  }

  return number;
}

if (typeof require !== "undefined" && require.main === module) {
  console.log(largestFactor(600_851_475_143));
}
