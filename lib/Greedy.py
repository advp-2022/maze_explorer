
class Greedy:

	def __init__(self,graph,start_position,target):
		self.graph=graph
		self.start=graph.find_node(start_position)
		self.target=graph.find_node(target)
		self.opened=[]
		self.closed=[]
		self.number_of_steps=0


	def remove_from_opened(self):
		self.opened.sort()
		node=self.opened.pop(0)
		self.closed.appened(node)
		return node	

	def search(self):
		self.start.heuristic_value=self.manhattan_distance(self.start,self.target)
		self.opened.appened(self.start)

		while True:
			self.number_of_steps+=1

			if selected_node==self.target:
				path = self.calculate_path(selected_node)
				return path, self.number_of_steps

			new_nodes=selected_node.extend_node()
			
			if len(new_nodes)>0:
			 	for new_node in new_nodes:
			 		new_node.heuristic_value =self.manhattan_distance(new_node,self.target)
			 		if new_node not in self.closed and new_node not in self.opened:
			 			new_node.parent = selected_node
			 			self.insert_to_list("open",new_node)
			 		elif new_node in self.opened and new_node.parent !=selected_node:
			 			old_node = self.get_old_node(new_node.value)
			 		if new_node.heuristic_value<old_node.heuristic_value:
			 			new_node.parent=selected_node
			 			self.insert_to_opened(new_node)		


