#include<stdio.h>
void swap(int *p,int *q)
{
	*q = *p+*q;
	*p = *q-*p;
	*q = *q-*p;
}
void main()
{
	int x = 10;
	int y = 34;
	printf("\nValue before swapping:%d %d",x,y);
	swap(&x,&y);
	printf("\nValue after swapping:%d %d",x,y);
}
