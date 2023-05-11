#include<stdio.h>
#include<stdlib.h>
int main(){
	int *ptr;
	int *ptr2;
	int n,i,num;
	printf("\nEnter size required:");
	scanf("%d",&n);
	ptr = (int*)malloc(n*sizeof(int));
	ptr2 = ptr;
	for(i=0;i<n;i++){
		//ptr2 = ptr;
		printf("\nEnter number:");
		scanf("%d",&num);
		*ptr = num;
		ptr++;
	}
	ptr = ptr2;
	for(i=0;i<n;i++){
		//ptr = ptr2;
		printf("\n%d",*ptr);
		ptr++;
	}
	free(ptr);
	return 0;

}
