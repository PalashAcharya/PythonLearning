#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	struct node *next;
};
void Linkedlisttraversal(struct node*ptr){
	while(ptr!=NULL){
		printf("Element :%d\n",ptr->data);
		ptr = ptr->next;	
	}
}
int main(){
	int num,i,user_input;
	struct node *head;
	struct node *current;
	struct node*ptr;
	printf("Enter the number of nodes:");
	scanf("%d",&num);
	head = (struct node*)malloc(sizeof(struct node));
	printf("Enter value of 1st node:");
	scanf("%d",&head->data);
	head->next = NULL;
	ptr = head;
	for(i=1;i<num;i++){
		printf("Enter value of %dth node:",i+1);
		scanf("%d",&user_input);
		current = (struct node*)malloc(sizeof(struct node));
		current->data = user_input;
		head->next = current;
		current->next = NULL;
		head = current;
	}
	Linkedlisttraversal(ptr);
}
