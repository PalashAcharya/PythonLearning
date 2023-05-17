#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node *next;
};	
void Linkedlisttraversal(struct Node*ptr){
	while(ptr!=NULL){
		printf("Elements:%d\n",ptr->data);
		ptr = ptr->next;
	}
}
void main(){
	int i,j,var;
	 struct Node*head;
	 struct Node*ptr;
	 struct Node*ptr2;
	 head = (struct Node*)malloc(sizeof(struct Node));
	 head->data = 10;
	 head->next = NULL;
	 head->next = (struct Node*)malloc(sizeof(struct Node));
	 head->next->data = 20;
	 head->next->next = NULL;
	 head->next->next = (struct Node*)malloc(sizeof(struct Node));
	 head->next->next->data = 30;
	 head->next->next->next = NULL;
	 ptr=head;
	 ptr2= head->next;
	 printf("%d\n",head->data);
	 printf("%d\n",head->next->data);
	 printf("%d\n",head->next->next->data);
	 for(i=0;i<3;i++){
		for(j=i+1;j<3;j++){
			printf("Hello");
			if(ptr2->data > ptr->data){
				printf("Hello!");
				var=ptr->data;
				ptr->data = ptr2->data;
				ptr2->data = var;
			}
			ptr =ptr->next;
			ptr2=ptr2->next;
		}
		ptr = head;
		ptr2 = head->next;
	}
	Linkedlisttraversal(head);
	
}
