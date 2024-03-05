#include<stdio.h>

int main(){
	int arr[10],f=0,l=9,i,x,flag,mid;
	printf("Enter elements in ascending order:");
	for(i=0;i<10;i++){
		scanf("%d",&arr[i]);
	}
	printf("Enter element to search for:");
	scanf("%d",&x);
	while(f<=l){
		mid = f+(l-f)/2;
		if(x==arr[mid]){
			flag = 1;
			break;
		}
		else if(x>arr[mid]){
			f = mid+1;
		}
		else{
			l = mid-1;
		}
	}
	if(flag==1){
		printf("Element found at %d",mid+1);
	}
	else{
		printf("Element not found");
	}
	return 0;
}
