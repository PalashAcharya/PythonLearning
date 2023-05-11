#include<stdio.h>
int IsDiagonalMatrix(int m,int n,int arr[][2]){
	int i,j;
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			if(arr[i]!=arr[j]){
				if(arr[i][j]==0){
					continue;
				}
				else{
					return 0;
				}
			}
		}
	}
	return 1;
}
int IsScalarMatrix(int m,int n,int arr[][2]){
	int num,i,j,var;
	num = IsDiagonalMatrix(m,n,arr);
	if(num==1){
		var = arr[0][0];
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				if(arr[i]==arr[j]){
					if(arr[i][j]==var){
						continue;
					}
					else{
						return 2;
					}
					
				}
			}
		}
		return 3;
	}
	else{
		return 2;
	}
	
}
int IsidentityMatrix(int m,int n,int arr[][2]){
	int num,i,j;
	num = IsDiagonalMatrix(m,n,arr);
	if(num==1){
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				if(arr[i]==arr[j]){
					if(arr[i][j]==1){
						continue;
					}
					else{
						return 0;
					}
				}
			}
		}
		return 1;
	}
}
int main(){
	int num;
	int arr[2][2] = {{1,0},{0,1}};
	num = IsidentityMatrix(2,2,arr);
	if(num==1){
		printf("Its an identity matrix");
	}
	else{
		printf("Its not an Identity matrix");
	}
}
