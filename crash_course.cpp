#include <iostream>
using namespace std;
int main()
{
    /*~~~~~print~~~~*/
    cout << "Hello world\nHi\n";
    /*~~~~~variable~~~*/
    // 	int x = 5;
    // 	cout<<"X is equal:"<<x;
    // 	cout<<endl;

    // 	string name = "khaled";
    // 	cout<<name;
    // 	cout<<endl;

    // 	double y = 2.5;
    // 	cout<<y;
    // 	cout<<endl;

    // 	float b = 5.5;
    // 	cout<<b;
    //     cout<<endl;

    //     char v = 'c';
    //     cout<<v;
    //     cout<<endl;

    //     bool s = true;
    //     cout<<s;
    //     cout<<endl;

    // int age = 20;
    // string name = "khaled";
    // char grade = 'B';
    // float gpa = 3.8;
    // bool success = true;
    // age = 18;

    // cout<<"Your name is:"<<name<<endl;
    // cout<<"Your age is:"<<age<<endl;
    // cout<<"Your gpa is:"<<gpa<<endl;
    // cout<<"Are you success?"<<success<<endl;

    /*~~~~Input~~~~*/
    // int x;
    // cout<<"what's your age?";
    // cin>>x;
    // cout<<"your age is:"<<x;
    // cout<<endl;

    // string name;
    // cout<<"What's your name?";
    // cin>>name;
    // cout<<"your name is:"<<name;
    // cout<<endl;

    //~~~~~Calculator~~~~//
    // cout<<"Welcome to my calculator\n";
    // int x;
    // int y;
    // cout<<"What's the first number?";
    // cin>>x;
    // cout<<endl;
    // cout<<"What's the second number?";
    // cin>>y;
    // cout<<endl;
    // cout<<"What do you want to do?\n";
    // cout<<("1. Add");
    // cout<<("2. Subtract");
    // cout<<("3. Multiply");
    // cout<<("4. Divide");
    // cout<<endl;
    // int choice;
    // cout<<"Enter your choice(1/2/3/4)";
    // cin>>choice;
    // cout<<endl;
    // if (choice == 1)
    // {
    //   cout<<"The sum is:"<<x + y<<endl;
    // }
    // else if (choice == 2)
    // {
    //     cout<<"The difference is:"<<x - y<<endl;
    // }
    // else if (choice == 3)
    // {
    //     cout<<"The product is:"<<x * y<<endl;
    // }
    // else if (choice == 4)
    // {
    //     cout<<"The quotient is:"<<x / y<<endl;
    // }
    // else
    // {
    //     cout<<"تصاحبني؟";
    // }

    //~~~~~Arithmetic operations~~~~~//
    // cout<<5 + 5<<endl;
    // cout<<5 * 5<<endl;
    // float x = 2;
    // float y = 5;
    // cout<< x / y<<endl;
    // float z = x / y;
    // cout<<  z <<endl;
    // z++;
    // cout<< z <<endl;
    // z += 6;
    // cout<< z <<endl;

    //~~~~~Comparison~~~~//
    /*True = 1 , False = 0*/
    // int x = 7;
    // int y = 20;
    // cout<<(x > y)<<endl;
    // cout<<(x == 1)<<endl;

    //~~~logical operator~~//
    // int x = 1;
    // int y = 6;
    // int z = 10;
    // cout<<(x > y && z > y)<<endl; //&&--> and
    // cout<<(x > y || z > y)<<endl; //||--> or
    // cout<<(x != y)<<endl; //! --> not
    // cout<<(!(x > y && z > y))<<endl;

    //~~~~IF~~~~~//
    // int a;
    // cout<<"Enter your result ";
    // cin>>a;
    // cout<<endl;
    // if (100>=a && a >= 97)
    // {
    //     cout<<"A+";
    // }
    // else if (96 >= a && a>= 93)
    // {
    //   cout<<"A";
    // }
    // else if (92 >=a && a>= 90)
    // {
    //     cout<<"A-";
    // }
    // else if (89 >=a && a>= 87)
    // {
    //     cout<<"B+";
    // }
    // else if (86 >=a && a >= 83)
    // {
    //     cout<<"B";
    // }
    // else
    // {
    //     cout<<"I'm bored!";
    // }

    //~~~~If else shortcut~~~~//
    // int a;
    // cout<"Number?";
    // cin>>a
    // (a > 0)?cout<<"Thank you!":cout<<"We need a postive umber"

    //~~~~~~~~switch~~~~~~~//
    // float n1;
    // float n2;
    // char op;
    // cout<<"Welcome to my calculator\n";
    // cout<<"Number1: ";
    // cin>>n1;
    // cout<<endl;
    // cout<<"Number2: ";
    // cin>>n2;
    // cout<<endl;
    // cout<<"Enter an opirator (+,-,*,/): ";
    // cin>>op;
    // cout<<endl;
    // switch (op)
    // {
    //     case '+' :
    //      cout<<"Number1 + Number2 ="<<n1 + n2;
    //      break;
    //     case '-' :
    //      cout<<"Number1 - Number2 ="<<n1 - n2;
    //      break;
    //     case '*':
    //      cout<<"Number1 * Number2 ="<<n1 * n2;
    //      break;
    //     case '/':
    //      cout<<"Number1/Number2 ="<<n1 / n2;
    //      break;
    //     default:
    //      break;

    // }
    //~~~loops~~~//
    // for(int i=1;i<=100;)
    // {
    //     cout<<"Hello!\n";
    //     i++;
    //     cout<<i;
    // }
    // nested for
    // int week = 3;
    // int day = 7;
    // for(int i=1;i<= week;)
    // {
    //     cout<<"Week:"<<i<<endl;
    //     i++;
    //     for(int j = 1; j <= day;)
    //     {
    //       cout<<"      Day:"<<j<<endl;
    //       j++;
    //     }

    // }
    // while
    //     int i = 1;
    //  while (i <= 100)
    //     {
    //         cout << "HI\n";
    //         i++;
    //     }
    // loop project
    //  int n=0;
    //  int sum = 0;
    //  cout<<"Enter the number";
    //  cin>>n;
    //  while(n >= 0)
    //  {
    //      sum+=n;
    //      cout<<"Enter the number";
    //      cin>>n;
    //      cout<<endl;
    //  }
    //  cout<<"Sum="<<sum;
    // do while
    //  int x = 1;
    //  do
    //  {
    //      cout<<x<<endl;
    //       x++;
    //  }while(x<100);
    /*~~~~finish~~~~*/
    return 0;
}
