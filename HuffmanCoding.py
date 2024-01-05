import heapq 

class node: 
	def __init__(self, freq, symbol, left = None, right = None): 
		# Tần suất(frequency) của ký tự
		self.freq = freq 

		# Ký tự
		self.symbol = symbol 

		# Node bên trái của node hiện tại 
		self.left = left 

		# Node bên phải của node hiện tại 
		self.right = right 

		# Tree direction (0/1) 
		self.huff = '' 

	def __lt__(self, nxt):                      # Hàm này trả về true nếu a < b, trong đó a, b là các đối tượng của class
		return self.freq < nxt.freq 


def printNodes(node, val = ''):                 # Giải mã, thực chất tìm con đường từ gốc đến lá

	newVal = val + str(node.huff) 

	if(node.left): 
		printNodes(node.left, newVal) 
	if(node.right): 
		printNodes(node.right, newVal) 
        
	if(not node.left and not node.right): 
		print(f"{node.symbol}: {newVal}") 


# Các ký tự của Huffman tree 
chars = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j'] 

# Tần suất của các ký tự
freq = [1, 5, 10, 15, 20, 8, 21, 2, 2, 16] 

# list containing unused nodes 
nodes = [] 

# Đẩy ký tự và tần suất vào trong Huffman tree
for x in range(len(chars)): 
	heapq.heappush(nodes, node(freq[x], chars[x]))          # nodes là 1 heap

while len(nodes) > 1: 

	left = heapq.heappop(nodes) 
	right = heapq.heappop(nodes) 

	left.huff = 0
	right.huff = 1

	# Kết hợp 2 node nhỏ nhất để tạo ra node mới là node cha
	newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right) 

	heapq.heappush(nodes, newNode) 


printNodes(nodes[0]) 
