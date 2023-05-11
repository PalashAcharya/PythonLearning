#include<stdio.h>
void calc(int a,int b,int *add,int *mul,int *sub,int *div){
	int *ptr1 = &a;
	int *ptr2 = &b;
	*add = *ptr1+*ptr2;
	*mul = *ptr1**ptr2;
	*sub = *ptr1-*ptr2;
	*div = *ptr1/ *ptr2;
}
void main(){
	int addition;
	int multiplication;
	int subtraction;
	int division;
	int a=30,b = 10;
	calc(a,b,&addition,&multiplication,&subtraction,&division);
	printf("\nAddition is %d\nSubtraction is %d\nMultiplication is %d\nDivision is %d",addition,subtraction,multiplication,division);
}
