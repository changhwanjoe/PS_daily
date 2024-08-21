
#include<iostream>
#include<string>//needthis
using namespace std;
int main(void)
{
    string str_i = "22";
    string str_li = "2144967290";
    string str_f = "3.4";
    string str_d = "2.11";
 
    //int i = str_i;    //error
    int i       = stoi(str_i);
    long int li = stol(str_li);
    float f     = stof(str_f);
    double d    = stod(str_d);
 
    //C++ cout
    cout << "stoi : " << i    << endl;
    cout << "stol : " << li  << endl;
    cout << "stof : " << f    << endl;
    cout << "stod : " << d    << endl;
 
    cout << endl;
    //C, C++ printf
    printf("stoi : %d\n", i);
    printf("stol : %ld\n", li);
    printf("stof : %f\n", f);
    printf("stod : %lf\n", d);
 
    cout << endl;
    system("pause");
    return 0;
}