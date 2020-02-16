#include<bits/stdc++.h>

using namespace std;

typedef  pair<int, int> iPair; 
  
struct Graph 
{ 
    int V, E; 
    vector< pair<int, iPair> > edges; 
    Graph(int V) 
    { 
        this->V = V;  
    } 
    void addEdge(int u, int v, int w) 
    { 
        edges.push_back({w,{u,v}}); 
    } 

    int kruskalMST();
}; 

struct DisjointSets 
{ 
    int *parent, *rnk; 
    int n; 
    
    DisjointSets(int n) 
    { 
        // Allocate memory 
        this->n = n; 
        parent = new int[n+1]; 
        rnk = new int[n+1]; 
  
        for (int i = 0; i <= n; i++) 
        { 
            rnk[i] = 0; 
  
            //every element is parent of itself 
            parent[i] = i; 
        } 
    } 
  
    // Find the parent of a node 'u' 
    // Path Compression 
    int find(int u) 
    { 
        /* Make the parent of the nodes in the path 
           from u--> parent[u] point to parent[u] */
        if (u != parent[u]) 
            parent[u] = find(parent[u]); 
        return parent[u]; 
    } 
  
    // Union by rank 
    void merge(int x, int y) 
    { 
        x = find(x), y = find(y); 
  
        /* Make tree with smaller height 
           a subtree of the other tree  */
        if (rnk[x] > rnk[y]) 
            parent[y] = x; 
        else // If rnk[x] <= rnk[y] 
            parent[x] = y; 
  
        if (rnk[x] == rnk[y]) 
            rnk[y]++; 
    } 
}; 
  
 /* Functions returns weight of the MST*/ 
  
int Graph::kruskalMST() 
{ 
    int mst_wt = 0; // Initialize result 
  
    // Sort edges in increasing order on basis of cost 
    sort(edges.begin(), edges.end()); 
  
    // Create disjoint sets 
    DisjointSets ds(V); 
  
    // Iterate through all sorted edges 
    vector< pair<int, iPair> >::iterator it; 
    for (it=edges.begin(); it!=edges.end(); it++) 
    { 
        int u = it->second.first; 
        int v = it->second.second; 
  
        int set_u = ds.find(u); 
        int set_v = ds.find(v); 
  
        // Check if the selected edge is creating 
        // a cycle or not (Cycle is created if u 
        // and v belong to same set) 
        if (set_u != set_v) 
        { 
            // Update MST weight 
            mst_wt += it->first; 
  
            // Merge two sets 
            ds.merge(set_u, set_v); 
        } 
    } 
  
    return mst_wt; 
} 

int findPathCost(vector<pair<int,int>> adj[], int u,int v){
    for(auto it = adj[u].begin(); it != adj[u].end(); ++it){
        if((*it).first == v){
            return (*it).second;
        }
    }
}

int isExistOpen(vector<pair<int,iPair>> open,int v){
    for(auto it = open.begin(); it != open.end(); ++it){
        if((*it).second.second == v){
            return (*it).first;
        }
    }
    return -1;
}

void findAndUpdate(vector<pair<int,iPair>> &open,int tc, int pc, int v){
    for(auto it = open.begin(); it != open.end(); ++it){
        if((*it).second.second == v){
            (*it).second.first = pc;
            (*it).first = tc;
            return;
        }
    }
}

int findMinh1(int *adj[], int v, vector<int> remainEle){
    int mini = remainEle.size() > 1 ? INT_MAX : 0;
    for(auto it = remainEle.begin(); it != remainEle.end(); ++it){
        if(adj[v][*it] < mini && *it != v){
            mini = adj[v][*it];
        }
    }
    return mini;
}

int findMinh2(int *adj[], int v, vector<int> remainEle){
    int mini = remainEle.size() > 1 ? INT_MAX : 0;
    for(auto it = remainEle.begin(); it != remainEle.end(); ++it){
        if(adj[0][*it] < mini && *it != v){
            mini = adj[0][*it];
        }
    }
    return mini;
}

int heuristicCost(int v, int *adj[], vector<int> remainEle){
    int h1, h2, h3;
    h1 = findMinh1(adj,v,remainEle);
    h2 = findMinh2(adj,v,remainEle);

    Graph graph(remainEle.size()-1);
    int i = 0, j = 0;
    for(auto it = remainEle.begin(); it != remainEle.end(); ++it){
        if(*it != v){
            j = i+1;
            for(auto jt = it+1; jt != remainEle.end(); ++jt){
                if(*jt != v){
                    graph.addEdge(i,j,adj[*it][*jt]);
                    ++j;
                }
            }
            ++i;
        }
    }
    h3 = graph.kruskalMST();
    return h1+h2+h3;
    
}

int AStar(int **adj, int V){
    vector<pair<int,iPair>> open;
    vector<int> closed;
    vector<int> remainEle;
    for(int i = 0; i < V; ++i)
        remainEle.push_back(i);
    int hc = heuristicCost(0,adj,remainEle);
    int pc = 0;
    int tc = hc + pc;
     int minPathCost = 0;
    open.push_back({tc,{pc,0}});
    while(!remainEle.empty()){
        auto mini = std::min_element(open.cbegin(), open.cend(), [](const auto& lhs, const auto& rhs) {
            return lhs.first < rhs.first; 
        });

        pair<int,iPair> storePair = *mini;
        open.erase(mini);
        int ppc = storePair.second.first;
        int city = storePair.second.second;
        closed.push_back(city);
        remainEle.erase(find(remainEle.begin(),remainEle.end(),city));
        if(remainEle.empty()){
            minPathCost = ppc + adj[0][city];
        }

        for(auto it = remainEle.begin(); it != remainEle.end(); ++it){
            hc = heuristicCost((*it),adj,remainEle);
            pc = ppc + adj[city][*it];
            tc = pc + hc;
            int existTCO = isExistOpen(open,(*it));
            
            if(existTCO != -1){
                findAndUpdate(open,tc,pc,(*it));
            }
            else{
                open.push_back({tc,{pc,(*it)}});
            }
        }
        
    }
    return minPathCost;
}

int main(){
    int u, v, w, V, E;
    cout << "Enter the no. of cities: ";
    cin >> V;
    int **adj;
    adj = new int *[V];
    for(int i = 0; i < V; i++)
        adj[i] = new int[V];
    cout << "Enter the path cost" << endl;
    for(int i = 0; i < V; ++i){
        for(int j = 0; j < V; ++j)
            cin >> adj[i][j];
    }
    int minPathCost = AStar(adj,V);
    cout << "optimal path cost: " << minPathCost << endl;
}