#include<stdio.h>
int main(){
	int number,i;
	FILE *fp1,*fp2,*fp3;
	fp1 = fopen("Numbers.txt","w");
	for(i=0;i<10;i++){
		printf("Enter integers:");
		scanf("%d",&number);
		putw(number,fp1);
	}
	fclose(fp1);
	fp1 = fopen("Numbers.txt","r");
	fp2=fopen("Even.txt","w");
	fp3 = fopen("Odd.txt","w");
	while((number=getw(fp1))!=EOF){
		if(number%2==0){
			putw(number,fp2);
		}
		else{
			putw(number,fp3);
		}
	}
	fclose(fp1);
	fclose(fp2);
	fclose(fp3);
	
	fp2 = fopen("Even.txt","r");
	fp3 = fopen("Odd.txt","r");
	printf("The content of even file:");
	while((number = getw(fp2))!=EOF){
		printf("%d\n",number);
	}
	printf("The content of odd file:");
	while((number = getw(fp3))!=EOF){
		printf("%d\n",number);
	}
	fclose(fp2);
	fclose(fp3);
	return 0;
}
