#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;

void func1(int p); // declare functon
void myFunc(int &p);


class myclass {
public:
    int num;
    string Name;
    
    void Func() {
        cout << Name << "    " << num << endl;
    }
    void test(int k);
};


void myclass::test(int k){
    cout << "Hello World!\n" << k;
}

class constructorTest: public myclass {
    public:
        int x;
        int y;
        constructorTest(int a, int b){
            x = a;
            y = b;
        }
};


int main(){
    // swich case
    int x = 2;
    switch (x){
        case 2:
            cout << 2;
            break;

        case 3:
            cout << 3;
            break;

        default:
            cout << 4;
    }
    /* ########################## */

    // do while loop
    do {
        cout << "\nHello World!" << endl;
        x++;
    } while (x < 3);
    /* ################ */

    // array
    int i[] = {3, 4, 5};
    i[4] = 1;
    i[1] = 2;
    cout << i[4] << endl;

    string cars[5] = {"Volvo", "BMW", "Ford"};
    cars[3] = "Mazda";
    cars[4] = "Tesla";

    for(int j = 0; j < 5; j++) {
        cout << cars[j] << "\n";
    }
    /* ##################################### */

    // pointers
    int b = 9;
    int* ptr = &b; // pointer
    cout << b << "\n" << &b << "\n" << ptr << endl;
    cout << *ptr << endl;
    /* ################################# */
    
    // pointers used in function
    int p = 10;
    func1(p);
    cout << p << endl;
    myFunc(p);
    cout << p << endl;
    /* ############################### */

    // class
    myclass obj1;
    myclass obj2;

    obj1.Name = "Vihanga";
    obj1.num = 4;
    obj2.num = 6;
    obj2.Name = "Pankaja";

    cout << obj1.num << " " << obj1.Name << endl;
    cout << obj2.num << " " << obj2.Name << endl;

    obj1.Func();
    obj2.Func();

    obj1.test(25);

    constructorTest test(2, 3);
    cout << "\n" << test.x << endl;
    /* ################################ */

    // files
    ofstream testFile("testFile.txt"); // write
    for (int q = 0; q < 10; q++){
        testFile << q << "\n";
    }
    testFile.close();

    ifstream read("testfile.txt"); // read
    string text;
    while (getline(read, text)){
        cout << text << endl;
    }
    read.close();
    /* ######################### */

    // exception
    try{
        int h = 1;
        if (h == 1){
            throw 404;
        }else if (h == 2){
            throw 505;
        }
    }catch (...){
        cout << "not found!" << endl;
    }
    return 0;
}



void func1(int p){
    p += 10;
}

void myFunc(int &p){ // change variable globally
    p += 10;
}