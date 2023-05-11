#include<stdio.h>
#include<string.h>
int main(){
	int sem,rollnum;
	char name[20];
	printf("Enter name:");
	gets(name);
	printf("Enter Semester:");
	scanf("%d",&sem);
	printf("Enter Roll Number:");
	scanf("%d",&rollnum);
	printf("Name:%s\nRoll Number: %d\nSemester:%d",name,rollnum,sem);
}
