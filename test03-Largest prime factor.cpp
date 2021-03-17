#include <iostream>

using namespace std;

int main(){
    long long number_left = 600851475143, i = 2;
    bool stop = true;
    while (i < number_left){
        if (number_left % i == 0){
            cout << number_left << " % " << i << " = " << number_left % i << endl;
            number_left /= i;
        }
        i++;
    }
    cout << number_left;
    return 0;
}