/* 
  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
  The sum of these multiples is 23.

? Find the sum of all the multiples of 3 or 5 below 1000.
 */

#include <iostream>

using namespace std;

/* return sum of all the multiples of 3 or 5 below given number */
int divicible(int till){
    int total = 0;

    for (int i = 0; i < till; i++ ){
        if (i % 3 == 0 or i % 5 == 0){      // check if divicible by 3 and 5
                total += i;                 // add divicible numbers
        }
    }

    return total;
}


int main(){
    cout << divicible(1000);

    return 0;
}