/* 
  2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

? What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
 */

#include <bits/stdc++.h>

using namespace std;


/* returns smallest positive number that is evenly divisible by all of the numbers from 1 to num */
int smallest_divisible(int num){
    int cur_num = num;

    for (int i = 1; i <= num; i++){
        if (cur_num % i == 0){      // curruntly found number can be divicible by curruntly checking number
            continue;
        }

        for (int j = 2; j <= num; j++){     // check multiples of curruntly found number can be divisible
            if ((cur_num * j) % i == 0){
                cur_num *= j;
                break;
            }
        }
    }

    return cur_num;
}


int main(){
    cout << smallest_divisible(20);
    
    return 0;
}