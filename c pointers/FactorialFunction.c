#include<stdio.h>
int Factorial(int num){
	int fact,i;
	fact =1;
	for(i=1;i<=num;i++){
		fact = fact*i;
	}
	return (fact);
}
int main(){
	int num,fact;
	printf("\nEnter Number:");
	scanf("%d",&num);
	fact = Factorial(num);
	printf("\nFactorial of the number is %d",fact);
}
