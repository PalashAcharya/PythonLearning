#include<stdio.h>
int main(){
	int i,j,var,k;
	int arr[] = {1,2,3,4,5};
	for(i=0;i<5;i++){
		for(j=i+1;j<5;j++){
			if(arr[j]>arr[i]){
				var = arr[i];
				arr[i]=arr[j];
				arr[j]=var;
			}
		}
	}
	for(k=0;k<5;k++){
		printf("\nArray in Descending order is:%d\n",arr[k]);
	}
}  
