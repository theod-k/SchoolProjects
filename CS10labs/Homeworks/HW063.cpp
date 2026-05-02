#include <iostream>
#include <string>
using namespace std;

int main(){
  string s = " ";
  cout << "Please enter a string: ";
  getline(cin, s, '\n');

  int words = 1;
  int arr[s.length()];
  char uniqueLetters[s.length()];
  for(int i = 0; i < s.length(); i++){
    uniqueLetters[i] = ' ';
  }

  for(int i = 0; i < s.length(); i++){
    arr[i] = 1;
  }

  //All Lowercase and word count
  string s2 = "";
  for(int i = 0; i < s.length(); i++){
    if(isspace(s[i])){
      words++;
    }
    else if(isupper(s[i])){
      char c = tolower(s[i]);
      s2 = s2 + c;
    }
    else{
      s2 = s2 + s[i];
    }
  }
  s = s2;

  //Sort Alphabetically
  for(int i=0;i<s.length();i++){
    for(int j=1;j<s.length()-i;j++){
      if(s[j-1]>s[j]){
        char temp=s[j-1];
        s[j-1]=s[j];
        s[j]=temp;
      }
    }
  }

  //Gather Unique Letters
  for(int i = 0; i < s.length(); i++){
    int flag = 0;
    for(int in = 0; in < s.length(); in++){
      if(uniqueLetters[in] == s[i]){
        flag = 1;
      }
    }
    if(flag == 0){
      uniqueLetters[i] = s[i];
    }
  }

  for(int i = 0; i < s.length()-1; i++){
    if(s[i] == s[i+1]){
      arr[i] = arr[i] + 1;
      i++;
    }
  }

  cout << words << " words" << endl;
  for(int i = 0; i < s.length(); i++){
    cout << arr[i] << " " << uniqueLetters[i] << endl;
  }

  //I know there is a small error when you have duplicates but I don't know how to fix it
  return(0);
}
