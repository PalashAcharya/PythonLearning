#include<stdio.h>
#include<stdlib.h>
struct linkedlist{
	int data;
	struct linkedlist *ptr;
};
int main(){
	struct linkedlist *box;
	box = (struct linkedlist*)malloc(sizeof(struct linkedlist));
	box->data = 10;
	box->ptr = NULL;
	printf("\n%d",box->data);

}
