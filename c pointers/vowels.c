#include<stdio.h>
#include<string.h>
int Numberofvowels(char str[]){
	int count,i,j;
	int a = strlen(str);
	char vowel[5] = {'a','e','i','o','u'};
	count =0;
	for(i=0;i<a-1;i++){
		for(j=0;j<4;j++){
			if(str[i]==vowel[j]){
				count = count + 1;
				break;
			}
		}
			
	}
	return count;
	
}
int main(){
	char name[20];
	int num;
	printf("Enter name:");
	gets(name);
	num = Numberofvowels(name);
	printf("The Number of vowels are %d",num);
}
