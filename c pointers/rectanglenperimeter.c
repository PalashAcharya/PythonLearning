#include<stdio.h>
void RectangleandPerimeter(int *a,int*p,int x,int y)
{
	int *q = &x;
	int *i = &y;
	*a = *q**i;
	*p = *q + *i;
	*p = 2**p;
}
void main()
{
	int area;
	int perimeter;
	int x = 10;
	int y =34;
	RectangleandPerimeter(&area,&perimeter,10,34);
	printf("\nArea is %d",area);
	printf("\nPerimeter is %d",perimeter);
}
