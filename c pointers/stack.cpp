#include<stdio.h>
void push(int *Top,int stack[]){
	printf("\npush:Before:Top:%d\n",*Top);
	int i;
	if(*Top>6){
		printf("Stack Overflow");
	}
	else{
		*Top = *Top + 1;
		printf("Enter the value to enter in stack:");
		scanf("%d",&i);
		stack[*Top]=i;
		printf("%d\n",stack[*Top]);
	}
	printf("\npush:after:Top:%d\n",*Top);
}
void Display(int *Top,int stack[]){
	printf("\nDisplay:Before:Top:%d\n",*Top);
	int top = *Top;
	for(int i=top;i>=0;i--){
		printf("%d\n",stack[i]);
	}
	printf("\nDisplay:After:Top:%d\n",*Top);
}
int main(){
	int con =1;
	int num;
	int Top = -1;
	int stack[7];
	
	while(con!=0){
		printf("Enter 1 to push\nEnter 2 to display\nEnter3 to exit");
		scanf("%d",&num);
		
		switch(num){
			case 1:
				push(&Top,&stack[7]);
				break;
			case 2:
				Display(&Top,&stack[7]);
				break;
			case 3:
				con=0;
				break;
			default:
				printf("You entered invalid choice");
		
		}
	}
	return 0;
}
