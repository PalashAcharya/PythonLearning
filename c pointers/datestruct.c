#include<stdio.h>
#include<string.h>
struct date{
	int day;
	char month[10];
	int year;
};
int main(){
	struct date dob;
	printf("Enter your Birth year:");
	scanf("%d",&dob.year);
	fflush(stdin);
	printf("\nEnter your Birth month:");
	gets(dob.month);
	printf("\nEnter your Birth day:");
	scanf("%d",&dob.day);
	printf("\nYour Birthday is %d %s %d",dob.day,dob.month,dob.year);
	struct date dog;
	printf("\nEnter the year you graduated:");
	scanf("%d",&dog.year);
	printf("\nEnter the month you graduated:");
	scanf("%s",&dog.month);
	printf("\nEnter the day you graduated:");
	scanf("%d",&dog.day);
	printf("\nYour date of graduation is %d %s %d",dog.day,dog.month,dog.year);
	return 0;
	
}
