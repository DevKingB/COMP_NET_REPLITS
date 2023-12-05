LETTERS = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}

#############################################################
# Change everything within comment blocks
#############################################################
# Copy the whole table and paste in the graph variable below. Make sure not to change anything (like spaces or anything)
#############################################################
graph = ''' '''

iteration = 4
dist_to_node = input("Enter the node letter to get the distance vector to: ").lower()
#################################################################

def int_or_inf(i): 
  return int(i) if i.isdigit() else float("inf")
  
nodes = [
  list(map(int_or_inf, row.split('\t')[1:]))
  for row in graph.strip().split('\n')[1:]
]

def DistanceVectorNIteration(iteration, nodes):
  for _ in range(iteration):
    nodes = DistanceVectorOneIteration(nodes)
  return nodes

def DistanceVectorOneIteration(nodes):
  for i in range (len(nodes)):
    for j in range(0, len(nodes[i])):
      if i != j and nodes[i][j] != float("inf"):
        for k in range(len(nodes[i])):
          if nodes[i][k] != float("inf"):
            nodes[j][k] = min(nodes[j][k], nodes[i][j] + nodes[i][k])

  return nodes

def main(node_letter, nodes):
  nodes = DistanceVectorNIteration(iteration, nodes)
  print(",".join([str(i) for i in nodes[LETTERS[node_letter]]]))

if __name__=="__main__":  
  main(dist_to_node,nodes)



