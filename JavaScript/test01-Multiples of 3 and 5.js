/* 
  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
  The sum of these multiples is 23.

? Find the sum of all the multiples of 3 or 5 below 1000.
*/


function total(num){
    let sum = 0;

    for (let i = 0; i < num; i++){
        if (i%3 === 0 || i%5 === 0){
            sum += i;
        };
    };

    return sum;
};


// this equals to __name__ == '__main__' in python. requre is undefined in browsers.
if (typeof require !== 'undefined' && require.main === module) { 
    console.log(total(1000));
};