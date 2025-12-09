no_of_nodes=8 #TC=O(n)+O(2E)
result=[]
adj=[[],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]
visited=[0]*(no_of_nodes+1)

def dfs(node,adj,result,visited):
    visited[node]=1
    result.append(node)
    for n in adj[node]:
        if visited[n] ==0:
            dfs(n,adj,result,visited)
dfs(1,adj,result,visited)
print(result)


