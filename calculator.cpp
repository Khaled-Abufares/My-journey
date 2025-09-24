#include<iostream>
using namespace std;
int main()
{
    cout<<"Welcome to my calculator\n";
    cout<<"Number1: ";
    cin>>n1;
    cout<<endl;
    cout<<"Number2: ";
    cin>>n2;
    cout<<endl;
    cout<<"Enter an opirator (+,-,*,/): ";
    cin>>op;
    cout<<endl;
    switch (op)
    {
        case '+' :
         cout<<"Number1 + Number2 ="<<n1 + n2;
         break;
        case '-' :
         cout<<"Number1 - Number2 ="<<n1 - n2;
         break;
        case '*':
         cout<<"Number1 * Number2 ="<<n1 * n2;
         break;
        case '/':
         cout<<"Number1/Number2 ="<<n1 / n2;
         break;
        default:
         break;

    }  
return0;
}
 }       default:
         break;
