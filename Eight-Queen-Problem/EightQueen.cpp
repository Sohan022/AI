#include<iostream>
#include<bits/stdc++.h>

using namespace std;
typedef pair<int,vector<vector<int>>> p;

// checking safe position for queen
bool checkPosition(vector<vector<int>> &v,int row, int col){
    int i, j;
    // checking safe position in the  left
    for (i = 0; i < col; i++) 
        if (v[row][i]) 
            return false; 
    // checking safe postion in the left upward
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--) 
        if (v[i][j]) 
            return false; 
    // checking safe positon in the left downward
    for (i = row, j = col; j >= 0 && i < 8; i++, j--) 
        if (v[i][j]) 
            return false; 
    //if the position is safe then return true
    return true; 
}

void ucs(priority_queue<p,vector<p>,greater<p>> &open, vector<vector<int>> &v){
    // push blank chess board and cost = 0 in open
    open.push(make_pair(0,v));
    int k = 1;
    while(!open.empty()){
        for(int j = 0; j < 8; ++j){
            p storePair = open.top();
            vector<vector<int>> vec = storePair.second;
            int t = storePair.first;
            if(checkPosition(vec,j,t)){
                if(t == 7){
                     vec[j][t] = 1;
                     //print index
                     cout << k << endl;
                     ++k;
                     // print all possible solution of 8 queen
                     for(auto it : vec){
                        for(auto i : it){
                            cout << i << " ";
                        }
                        cout << endl;
                    }
                    cout << endl;
                }else{
                    vec[j][t] = 1;
                    //push new pair into open
                    open.push(make_pair(t+1,vec));
                }  
            }
        }
        open.pop();        
    }
}


int main(){
    //priority queue for storing pairs (cost and pointer to chess board)
    priority_queue<p,vector<p>,greater<p>> open;
    // create 8X8 chess board
    vector<vector<int>> v(8,vector<int>(8,0));
    ucs(open,v);
}