#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node *next;
};	
void main(){
	 struct Node*head;
	 head = (struct Node*)malloc(sizeof(struct Node));
	 head->data = 10;
	 head->next = NULL;
	 head->next = (struct Node*)malloc(sizeof(struct Node));
	 head->next->data = 20;
	 head->next->next = NULL;
	 head->next->next = (struct Node*)malloc(sizeof(struct Node));
	 head->next->next->data = 30;
	 head->next->next->next = NULL;
	 printf("%d\n",head->data);
	 printf("%d\n",head->next->data);
	 printf("%d\n",head->next->next->data);
	
}
