#include<iostream>
using namespace std;
void vowelornot(char x){
    if(x=='a'||x=='A'||x=='e'||x=='E'||x=='i'||x=='I'||x=='o'||x=='O'||x=='u'||x=='U'){
        cout<<"Vowel"<<endl;
    }
    else{
        cout<<"Consonant"<<endl;
    }
}
int main(){
    char letter;
    cout<<"Enter letter:"<<endl;
    cin>>letter;
    vowelornot(letter);
    return 0;
}
