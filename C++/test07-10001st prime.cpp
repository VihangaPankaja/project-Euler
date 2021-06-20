/* 
  By listing the first six prime numbers: 
*   2, 3, 5, 7, 11, and 13, 
    we can see that the 6th prime is 13.

? What is the 10 001st prime number 
 */

#include <bits/stdc++.h>

using namespace std;

/* 
Primality test using 6𝑘 ± 1 optimization
https://en.wikipedia.org/wiki/Primality_test#C#_code
 */
bool IsPrime(int n)
{
    if (n==2 || n==3) { return true; }
    else if (n <= 1 || (n % 2)==0 || (n % 3)==0) { return false; }
    
    int i = 5;
    while (i*i <= n){
        if ((n % i)==0 || (n % (i + 2))==0) { return false; }
        i += 6;
    }
    
    return true;
}


/* returns given placed prime number */
int nthPrime(int prime_no){
    int primesFound = 2, k = 1;     /* ckeck for 6k ± 1 numbers. 2,3 includes in primesFound */

    while (primesFound <= prime_no){
        if (IsPrime(6*k - 1)){primesFound++;}

        if (primesFound == prime_no){return 6*k - 1;}

        if (IsPrime(6*k + 1)){primesFound++;}

        k++;
    }

    return 6*(k-1) + 1;
}


int main(){ 
    cout << nthPrime(10001);

    return 0;
}