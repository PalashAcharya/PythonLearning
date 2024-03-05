#include<stdio.h>
#define size 6
int queue[size];
int front =-1,rear=-1;

void insert(int data){
	if(rear==size-1){
		printf("Queue overflow");
		return -1;
	}
	if(rear==-1){
		front = rear =0;
	}
	else{
		rear = rear+1;
	}
	queue[rear]=data;
}

void delete(){
	int deletevalue;
	if(front==-1){
		printf("Queue underflow");
		return -1;
	}
	deletevalue = queue[front];
	if(front==rear){
		front=rear=-1;
	}
	else{
		front++;
	}
	printf("%d deleted",deletevalue);
}


int main(){
	insert(10);
	insert(15);
	insert(20);
	delete();
	for(int i=0;i<rear;i++){
		printf("%d\n",queue[i]);
	}
	return 0;
}
