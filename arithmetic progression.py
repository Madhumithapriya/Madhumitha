#include <bits/stdc++.h> 
using namespace std; 
void printAP(int a, int d, int n) 
{ 
int curr_term; 
curr_term=a; 
for (int i = 1; i <= n; i++) 
{   cout << curr_term << " "; 
    curr_term =curr_term + d; 
    } 
} 
int main()  
{   
    int a = 2;  
    int d = 1;
    int n = 5;  
   printAP(a, d, n); 
  return 0; 
} 
