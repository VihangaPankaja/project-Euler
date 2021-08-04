/* 
  The prime factors of 13195 are 5, 7, 13 and 29.

? What is the largest prime factor of the number 600851475143
 */

#include <iostream>

using namespace std;

/* return largest prime factor for given number */
int largest_factor(long long number_left){
    long long  i = 2;

    while (i < number_left){            // if not prime
        while (true){
            if (number_left % i == 0 && number_left / i != 1){      // if divisible by i
                number_left /= i;           // get other factor
            }else {
                break;
            };
        };
        i++;
    }

    return number_left;
}


int main(){
    cout << largest_factor(600851475143) << endl;
    
    return 0;
}