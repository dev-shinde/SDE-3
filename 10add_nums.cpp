#include<iostream>
using namespace std;

class sum
{
	public:
		
		int a,b;
		
	 sum(int x,int y)
		{
			a=x;
			b=y;			
			cout<<"Sum = "<<a+b<<endl;			
		}
	
};

main()
{
	sum p(12,20);
	
}
