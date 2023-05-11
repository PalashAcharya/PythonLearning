#include<stdio.h>
struct student{
	char name[25];
	int rollnum;
	int sem;
};
void Display(struct student Student){
	printf("\nStudent name:%s",Student.name);
	printf("\nStudent Roll Number:%d",Student.rollnum);
	printf("\nStudent semester:%d",Student.sem);	
}
void scan(struct student *Student){
	printf("\nEnter your Name:");
	scanf("%s",&Student->name);
	fflush(stdin);
	printf("\nEnter your Roll Number:");
	scanf("%d",&Student->rollnum);
	fflush(stdin);
	printf("\nEnter your Semester:");
	scanf("%d",&Student->sem);
	fflush(stdin);
}
int main(){
	/*struct student Student1;
	printf("Enter name:");
	scanf("%s",&Student1.name);
	printf("Enter rollnum:");
	scanf("%d",&Student1.rollnum);
	printf("Enter semester:");
	scanf("%d",&Student1.sem);
	printf("Student name:%s\nStudent roll number:%d\nStudent semester:%d\n",Student1.name,Student1.rollnum,Student1.sem);*/
	struct student Students[i];
	int i;
	for(i=0;i<5;i++){
		scan(&Students[i]);
	}
	for(i=0;i<5;i++){
		Display(Students[i]);
	}
	
}
