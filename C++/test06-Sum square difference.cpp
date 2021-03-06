/* 
  The sum of the squares of the first ten natural numbers is,
* 1² + 2² + ... + 10² = 385

  The square of the sum of the first ten natural numbers is,
* (1 + 2 + ... + 10)² = 55^2 = 3025

  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
* 3025 - 385 = 2640.

? Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
 */

#include <bits/stdc++.h>

using namespace std;


int diff(int num){
    int square_sum = 0, sum = 0;

    for (int n = 1; n <= num; n++){
        square_sum += pow(n, 2);
        sum += n;
    }

    return pow(sum, 2) - square_sum;
}


int main(){
    cout << diff(100) << endl;

    return 0;
}