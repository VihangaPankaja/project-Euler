#include <iostream>

using namespace std;

int main(){
    int total = 0, fib_new = 2, fib_prev_1 = 1, fib_prev_2;

    while (fib_new <= 4000000) {
        if (fib_new % 2 == 0){
            total += fib_new;
        }
        fib_prev_2 = fib_prev_1;
        fib_prev_1 = fib_new;
        fib_new = fib_prev_1 + fib_prev_2;
    }
    cout << total;
    return 0;
}