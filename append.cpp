#include<iostream>
using namespace std;
int main(){
    string s,t;
    cin>>s;
    cin>>t;
    int first=0,prefix=0;
    while (first < s.length() && prefix < t.length()){
        if (s[first]==t[prefix]){
            prefix++;
        }
        first++;
    }
    cout<<t.length() - prefix<<endl;
}