// #include <iostream>
// #include <vector>
// #include <unordered_map>
// #include <unordered_set>

// using namespace std;

// void dfs(int node, unordered_set<int>& visited, unordered_set<int>& component, unordered_map<int, vector<pair<int, int>>>& adj_list) {
//     visited.insert(node);
//     component.insert(node);
//     for (const auto& neighbor_weight : adj_list[node]) {
//         int neighbor = neighbor_weight.first;
//         if (visited.find(neighbor) == visited.end()) {
//             dfs(neighbor, visited, component, adj_list);
//         }
//     }
// }

// vector<int> getMinimumBitwiseAND(int g_nodes, vector<int>& g_from, vector<int>& g_to, vector<int>& g_weights, vector<vector<int>>& queries) {
    
//     unordered_map<int, vector<pair<int, int>>> adj_list;
//     for (int i = 0; i < g_from.size(); ++i) {
//         adj_list[g_from[i]].push_back({g_to[i], g_weights[i]});
//         adj_list[g_to[i]].push_back({g_from[i], g_weights[i]});
//     }
    
    
//     vector<unordered_set<int>> components;
//     unordered_set<int> visited;
//     for (int node = 1; node <= g_nodes; ++node) {
//         if (visited.find(node) == visited.end()) {
//             unordered_set<int> component;
//             dfs(node, visited, component, adj_list);
//             components.push_back(component);
//         }
//     }
    
//     vector<int> results;
//     for (const auto& query : queries) {
//         int u = query[0], v = query[1];
//         unordered_set<int> u_component, v_component;
//         for (const auto& comp : components) {
//             if (comp.find(u) != comp.end()) u_component = comp;
//             if (comp.find(v) != comp.end()) v_component = comp;
//         }
//         if (u_component.empty() || v_component.empty() || u_component != v_component) {
//             results.push_back(-1);  // If u and v are not in the same component, return -1
//         } else {
//             int min_bitwise_and = 0;
//             for (int node : u_component) {
//                 for (const auto& neighbor_weight : adj_list[node]) {
//                     int neighbor = neighbor_weight.first;
//                     int weight = neighbor_weight.second;
//                     if (u_component.find(neighbor) != u_component.end()) {
//                         min_bitwise_and &= weight;
//                     }
//                 }
//             }
//             results.push_back(min_bitwise_and);
//         }
//     }
    
//     return results;
// }

// int main() {
//     int g_nodes = 4;
//     vector<int> g_from = {1, 3, 2, 3};
//     vector<int> g_to = {3, 2, 1, 4};
//     vector<int> g_weights = {2, 10, 6, 14};
//     vector<vector<int>> queries = {{2, 3}, {1, 5}};

//     vector<int> result = getMinimumBitwiseAND(g_nodes, g_from, g_to, g_weights, queries);

//     cout<<result[0];
//     cout << endl;

//     return 0;
// }




#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <numeric>
using namespace std;

class UnionFind {
public:
    UnionFind(int size) : parent(size), rank(size, 0) {
        iota(parent.begin(), parent.end(), 0);
    }
    
    int find(int u) {
        if (parent[u] != u) {
            parent[u] = find(parent[u]);
        }
        return parent[u];
    }
    
    void unite(int u, int v) {
        int rootU = find(u);
        int rootV = find(v);
        if (rootU != rootV) {
            if (rank[rootU] > rank[rootV]) {
                parent[rootV] = rootU;
            } else if (rank[rootU] < rank[rootV]) {
                parent[rootU] = rootV;
            } else {
                parent[rootV] = rootU;
                rank[rootU]++;
            }
        }
    }

private:
    vector<int> parent;
    vector<int> rank;
};

vector<int> getMinimumBitwiseAND(int g_nodes, vector<int>& g_from, vector<int>& g_to, vector<int>& g_weight, vector<vector<int>>& queries) {
    int g_edges = g_from.size();
    UnionFind uf(g_nodes + 1);
    unordered_map<int, vector<int>> componentEdges;

    // Process each edge and union-find
    for (int i = 0; i < g_edges; ++i) {
        int u = g_from[i];
        int v = g_to[i];
        int w = g_weight[i];
        uf.unite(u, v);
    }

    // Collect edge weights for each connected component
    for (int i = 0; i < g_edges; ++i) {
        int u = g_from[i];
        int v = g_to[i];
        int w = g_weight[i];
        int root = uf.find(u);
        componentEdges[root].push_back(w);
    }

    // Compute minimum bitwise-AND for each component
    unordered_map<int, int> minBitwiseAND;
    for (auto& entry : componentEdges) {
        int root = entry.first;
        auto& weights = entry.second;
        int minAND = weights[0];
        for (int weight : weights) {
            minAND &= weight;
        }
        minBitwiseAND[root] = minAND;
    }

    // Answer the queries
    vector<int> results;
    for (const auto& query : queries) {
        int u = query[0];
        int v = query[1];
        if (uf.find(u) == uf.find(v)) {
            int root = uf.find(u);
            results.push_back(minBitwiseAND[root]);
        } else {
            results.push_back(-1);
        }
    }

    return results;
}

int main() {
    int g_nodes, g_edges;
    cin >> g_nodes >> g_edges;

    vector<int> g_from(g_edges), g_to(g_edges), g_weight(g_edges);
    for (int i = 0; i < g_edges; ++i) {
        cin >> g_from[i] >> g_to[i] >> g_weight[i];
    }

    int q;
    cin >> q;
    vector<vector<int>> queries(q, vector<int>(2));
    for (int i = 0; i < q; ++i) {
        cin >> queries[i][0] >> queries[i][1];
    }

    vector<int> results = getMinimumBitwiseAND(g_nodes, g_from, g_to, g_weight, queries);

    for (int result : results) {
        cout << result << endl;
    }

    return 0;
}