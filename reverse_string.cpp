#include<iostream>
using namespace std;

int main(){
    string s;
    cin>>s;
    int left=0,right=s.length()-1;
    while (left < right){
       char temp=s[left];
       s[left]=s[right];
       s[right]=temp;
       left++;
       right--;    
    }
    cout<<s<<endl;  
}