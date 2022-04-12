class Node:

	def __init__(self, value, cordinate, neighbors=None):
		self.value=value
		self.x=cordinate[0]
		self.y=cordinate[1]
		self.heuristic_value = -1
		if neighbors is None:
			self.neighbors=[]
		else:
			self.neighbors=neighbors
		self.parent=None
		return go(f,seed,[])				


	def __gt__(self,other):
		if isinstance(other,Node):
			return True
		if self.heuristic_value > other.heuristic_value:
			return False
		return self.value > other.value	
