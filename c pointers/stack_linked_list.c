#include<stdio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node*next;
};

struct Node * top = NULL;

void push(int data){
	struct Node*newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = data;
	newNode->next = top;
	top = newNode;
}

int pop(){
	if(top==NULL){
		printf("Stack is empty");
		return -1;
	}
	else{
		struct Node*temp = top;
		int data = temp->data;
		top = top->next;
		free(temp);
		return data;
	}
}

int peek(){
	return top->data;
}

int main(){
	push(10);
	push(20);
	pop();
	printf("%d",peek());
	return 0;
	
}
