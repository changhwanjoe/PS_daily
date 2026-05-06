
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> solution(vector<int> answers)
{

  
vector<int> answer;    
int arr1[5]={1,2,3,4,5};    
int arr2[8]={2,1,2,3,2,4,2,5};    
int arr3[10]={3,3,1,1,2,2,4,4,5,5};    
int i1=0, i2=0, i3=0;    
int score[3]={0,0,0};        
int mScore=0;    
for(int i=0;i<answers.size();i++)    
{        
if(arr1[i1%5]==answers[i])            
score[0]++;        
if(arr2[i2%8]==answers[i])            
score[1]++;        
if(arr3[i3%10]==answers[i])            
score[2]++;                
if(mScore<score[0])           
 mScore=score[0];                
 if(mScore<score[1])            
 mScore=score[1];               
  if(mScore<score[2])          
    mScore=score[2];                
    i1++; i2++; i3++;    }       
     for(int i=0;i<3;i++)  
       {        if(score[i]==mScore)            
       answer.push_back(i+1);    }       
        return answer;}