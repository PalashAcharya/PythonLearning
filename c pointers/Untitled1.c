#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node*next;
};
void Linkedlisttraversal(struct Node*ptr){
	while(ptr!=NULL){
		printf("Elements:%d\n",ptr->data);
		ptr=ptr->next;
	}
}
int main(){
	int i,j,var;
	struct Node*head;
	struct Node *ptr;
	struct Node*ptr2;
	ptr=head;
	ptr2=head->next;
	head=(struct Node*)malloc(sizeof(struct Node));
	head->data=1;
	head->next=(struct Node*)malloc(sizeof(struct Node));
	head->next->data=2;
	head->next->next=(struct Node*)malloc(sizeof(struct Node));
	head->next->next->data=3;
	head->next->next->next=(struct Node*)malloc(sizeof(struct Node));
	head->next->next->next->data=4;
	head->next->next->next->next = NULL;
	printf("%d\n",head->data);
	printf("%d\n",head->next->data);
	printf("%d\n",head->next->next->data);
	printf("%d\n",head->next->next->next->data);
	/*for(i=0;i<4;i++){
		for(j=i+1;j<4;j++){
			if(ptr2->data>ptr->data){
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
	Linkedlisttraversal(head);*/
	
}
