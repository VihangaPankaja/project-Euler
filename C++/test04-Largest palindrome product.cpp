/* 
  A palindromic number reads the same both ways. 
  The largest palindrome made from the product of two 2-digit numbers is
* 9009 = 91 × 99.

? Find the largest palindrome made from the product of two 3-digit numbers
 */

// #include <iostream>
// #include <math.h>   /* pow */ /* cmath doesn't put in namespace */
// #include <string.h> /* to_string */
#include <bits/stdc++.h>    // includes all standard library

using namespace std;

/* returns max of palindromic products */
int max_prod_digit_palindrome(int num){
    int cur_max = 0;    // holds max palindrome currently found

    for (int i = pow(10,(num-1)); i < pow(10,num); i++){
        for (int j = pow(10,(num-1)); j < pow(10,num); j++){
            string mul = to_string(i * j);      // convert multiplication to string
            string reverseMul = mul;
            reverse(reverseMul.begin(), reverseMul.end());  // reverse of string
            
            if ((mul.compare(reverseMul) == 0) && (cur_max < i*j)){   // check for palindromic and larger than previous
                cur_max = i*j;
            }
        }
    }

    return cur_max;
}


int main(){
    cout << max_prod_digit_palindrome(3);

    return 0;
}