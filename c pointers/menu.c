#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node *next;
};
void LinkedlistTraversal(struct Node*ptr){
	while(ptr!=NULL){
		printf("Elements-%d\n",ptr->data);
		ptr = ptr->next;
	}
	
}
struct Node* CreateLinkedlist(struct Node *head){
	struct Node *current;
	current = (struct Node*)malloc(sizeof(struct Node));
	printf("Enter value:");
	scanf("%d",&current->data);
	head->next = current;
	current->next = NULL;
	head = current;
	return head;
	
}
void menu(){
	printf("Enter 1 to add number.\nEnter 2 to view list\nEnter 3 to edit\nEnter 4 to delete a node\nEnter 5 to append at certain position\nEnter 6 to exit\n");
}
struct Node* createfirstnode(struct Node *head){
	printf("Enter value of node:");
	scanf("%d",&head->data);
	head->next = NULL;
	return head;
}
void EditNode(struct Node *ptr){
	int user_input,counter;
	printf("Enter position to delete a node:");
	scanf("%d",&user_input);
	counter = 1;
	while(counter!=user_input){
		ptr = ptr->next;
		counter = counter+1;
	}
	printf("Enter value of new node:");
	scanf("%d",&ptr->data);
}
void DeleteNode(struct Node *ptr,int *user_input){
	struct Node *ptr2;
	int counter,counter2;
	ptr2=ptr;
	counter=1,counter2=1;
	while(counter!=*user_input){
		ptr2 = ptr2->next;
		counter = counter+1;
	}
	while(counter2!=*user_input-1){
		ptr = ptr->next;
		counter2 = counter2+1;
	}
	ptr->next = ptr2->next;
	free(ptr2);
	printf("Node deleted!\n");
	
}
struct Node* DeletefirstNode(struct Node*ptr){
	struct Node *ptr2;
	ptr2=ptr;
	ptr=ptr->next;
	free(ptr2);
	printf("Node deleted!");
	return ptr;
}
void AppendatPosition(struct Node *ptr,int * user_input){
	struct Node *current;
	current = (struct Node*)malloc(sizeof(struct Node));
	int counter=1;
	while(counter!=*user_input-1){
		ptr = ptr->next;
		counter = counter+1;
	}
	printf("Enter value of node:");
	scanf("%d",&current->data);
	current->next = ptr->next;
	ptr->next = current;
}
struct Node* AppendfirstNode(struct Node*ptr){
	struct Node*current;
	current =(struct Node*)malloc(sizeof(struct Node));
	printf("Enter the value :");
	scanf("%d",&current->data);
	current->next = ptr;
	ptr = current;
	return ptr;
}

int main(){
	struct Node *head;
	struct Node *ptr;
	int user_input, condition_ = 0,count=0,counter=1;
	head = (struct Node*)malloc(sizeof(struct Node));
	while(condition_==0){
		menu();
		printf("\nEnter input:");
		scanf("%d",&user_input);
		if(user_input==1){
			if(count ==0){
				head = createfirstnode(head);
				ptr = head;
				count = count + 1;
			}
			else{
				head = CreateLinkedlist(head);
			}
		}
		if(user_input ==2){
			LinkedlistTraversal(ptr);
		}
		if(user_input ==3){
			EditNode(ptr);
			printf("Node has been edited!\n");
		}
		if(user_input==4){
			printf("Enter the position of the node you want to delete:");
			scanf("%d",&user_input);
			if(user_input==1){
				ptr= DeletefirstNode(ptr);
			}
			else{
				DeleteNode(ptr,&user_input);
			}
		}
		if(user_input==5){
			printf("Enter the position to append the node:");
			scanf("%d",&user_input);
			if(user_input==1){
				ptr=AppendfirstNode(ptr);
			}
			else{
				AppendatPosition(ptr,&user_input);
			}
		    
		}
		if(user_input==6){
			condition_ =1;
		}	
	}
	return 0;
	
	
}
