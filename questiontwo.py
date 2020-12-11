# Question two implementation

# Find set of vertex i 
def find(i): 
	while parent[i] != i: 
		i = parent[i] 
	return i 

# Creates union of i and j. It returns 
# false if i and j are already in same 
# set. 
def union(i, j): 
	a = find(i) 
	b = find(j) 
	parent[a] = b 

# Finds minimum Spanning Tree(MST) using Kruskal's algorithm 
def MST(cost): 
	mincost = 0 # Cost of min MST 

	# Initialize sets of disjoint sets 
	for i in range(V): 
		parent[i] = i 

	# Include minimum weight edges one by one 
	edge_count = 0
	while edge_count < V - 1: 
		min = INF 
		a = -1
		b = -1
		for i in range(V): 
			for j in range(V): 
				if find(i) != find(j) and cost[i][j] < min: 
					min = cost[i][j] 
					a = i 
					b = j 
		union(a, b) 
		print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min)) 
		edge_count += 1
		mincost += min

	print("Minimum cost= {}".format(mincost)) 


# Driver code 
V =5
parent = [i for i in range(V)] 
INF = float('inf') 
cost = [[INF,10, 7, 9, 8], 
		[10,INF, 10, 5, 6], 
		[8, 10,INF, 8, 9], 
		[9, 5, 8,INF, 6], 
		[7, 6, 9, 6,INF]] 

# Print the solution 
MST(cost)
