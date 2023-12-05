''' PLEASE ONLY USE THIS FILE FOR DIJKSTRA'S ALGORITHM ON THE NODE NETWORK TABLE '''

#TODO FIX BUGGG IN THE PRINTED RESULTS
################################################################
# Run code and input values in terminal
################################################################

LETTERS = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z",None:None}

NUMBERS = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

##############################################################################
# Change the matrix below for your question
##############################################################################
ADJACENCY_MATRIX = '''
a	b	c	d	e	f	g	h	i	j	k	l
a	0	15	11	9							18	
b	15	0		19	7	10	15			4	16	
c	11		0	7	6			6				
d	9	19	7	0	3	1	19	2				
e		7	6	3	0		14		3	10		8
f		10		1		0						
g		15		19	14		0					
h			6	2				0	19	17		7
i					3			19	0			
j		4			10			17		0		
k	18	16									0	14
l					8			7			14	0
'''
##############################################################################

NUM_ITERATIONS = int(input("Enter number of iterations: "))
START_NODE = NUMBERS[input("Enter node least path is calculated from: ")] # g

START_NODE-=1 # Change nodes to 0-based indices.
NUM_ITERATIONS+=1  # The first iteration is used to find the starting node's neighbors - their distance is initially infinite.

def int_or_inf(i): 
  return int(i) if i.isdigit() else float("inf")

adjacency_lists = [
  list(map(int_or_inf, row.split('\t')[1:]))
  for row in ADJACENCY_MATRIX.strip().split('\n')[1:]
]

cost = [float("inf") for _ in adjacency_lists[0]]
cost[START_NODE] = 0
parents = [None for _ in adjacency_lists[0]]
weights = adjacency_lists
path = []

def dijkstras(dest):
  priority_queue = [START_NODE]
  seen = set([START_NODE])
  
  for _ in range(NUM_ITERATIONS):
    render()
    curr_node = min(priority_queue, key=lambda n:cost[n])
    priority_queue.remove(curr_node)
    # print(f"new priority queue: {priority_queue} | neighboring nodes: {[[LETTERS[n], n, cost[n]] for n in priority_queue]}\n")

    # Finding the path from src node to dest node
    if (NUMBERS[dest] - 1) in priority_queue:
      path.append(dest)
    else:
      path.append(LETTERS[curr_node])

    for neighbor, weight in enumerate(adjacency_lists[curr_node]):
      if neighbor == curr_node: 
        continue
      if cost[neighbor] > cost[curr_node] + weights[curr_node][neighbor]:
        cost[neighbor] = cost[curr_node] + weights[curr_node][neighbor]
        parents[neighbor] = curr_node
        if not neighbor in seen:
          priority_queue.append(neighbor)
          seen.add(neighbor)

  print(f"Path: {path}")

def get_child(parent, parents):
  '''Used for rendering display.'''
  for child, curr_parent in enumerate(parents):
    if parent == curr_parent:
      parents[child] = -1
      return child
  else:
    return -1

def render():
  '''Displays forest of node trees with costs.'''
  parents_copy = [p for p in parents]
  stack = [None]
  while stack:
    child = get_child(stack[-1], parents_copy)
    if child == -1:
      stack.pop()
    else:
      # print('.\t\t'*(len(stack)-1), child+1, cost[child])
      stack.append(child)
  # print('...')

src = input("Enter the src node for path: ")
dest = input("Enter dest node for path: ")

dijkstras(dest)

res = []
for i in range(len(parents)):
  if cost[i] == 0:
    res.append(LETTERS[START_NODE])
  else:
    res.append(str(LETTERS[parents[i]]))
  res.append(str(cost[i]))

result = ",".join(res)

def find_ans(src, dest, path=path, res=result):
  final_path = ""
  for i in path:
    if i == src:
      final_path += i + ","
    elif i == dest:
      final_path += i
      return f"{result};{final_path}"
    else:
      final_path += i + ","

print(find_ans(src, dest))

'''
Dijkstra's:
  queue visible nodes
  each iter
    get nearest node (that's not already "locked")
    relax each of its neighbors
    add relaxed neighbors to queue if they werent already added

This is unlike BFS because
  BFS doesn't do relaxing
  BFS doesn't care which node is nearest
'''
