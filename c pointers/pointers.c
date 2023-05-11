#include<stdio.h>
int main()
{
	int a;
	int *ptr;
	a = 10;
	ptr = &a;
	printf("value of a using pointer:%d",*ptr);
	*ptr = 30;
	printf("\nvalue of a:%d",a);
}
