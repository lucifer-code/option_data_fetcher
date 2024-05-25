from collections import defaultdict

def getMinimumBitwiseAND(g_nodes, g_from, g_to, g_weights, queries):
    # Step 1: Create adjacency list
    adj_list = defaultdict(list)
    for i in range(len(g_from)):
        adj_list[g_from[i]].append((g_to[i], g_weights[i]))
        adj_list[g_to[i]].append((g_from[i], g_weights[i]))
    
    # Step 2: Perform DFS or BFS to find connected components
    def dfs(node, component):
        component.add(node)
        for neighbor, _ in adj_list[node]:
            if neighbor not in component:
                dfs(neighbor, component)
    
    components = []
    visited = set()
    for node in range(1, g_nodes + 1):
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(component)
            visited |= component
    
    # Step 3-5: Process queries
    results = []
    for u, v in queries:
        u_component = next((comp for comp in components if u in comp), None)
        v_component = next((comp for comp in components if v in comp), None)
        if u_component is None or v_component is None or u_component != v_component:
            results.append(-1)  # If u and v are not in the same component, return -1
        else:
            min_bitwise_and = 0
            for node in u_component:
                for neighbor, weight in adj_list[node]:
                    if neighbor in u_component:
                        min_bitwise_and &= weight
            results.append(min_bitwise_and)
    
    return results

g_nodes = 4
g_from = [1,3,2,3]
g_to = [3,2,1,4]
g_weights = [2,10,6,14]
queries = [[2,3],[1,5]]

print(getMinimumBitwiseAND(g_nodes, g_from, g_to, g_weights, queries))  
