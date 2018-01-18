class Node():

	def __init__(self, value): #inicializa mi nodo
		self.value=None
		self.left=None
		self.right=None

class tree():

	def __init__(self): #mi clase constructora
		self.root=None

	def create(self, value):
		if(self.root==None):
			self.root=Node(value)
		else:
			current=self.root
			while(True):
				if(value<current.value):
					if(current.left!=None):
						current=current.left
					else:
						current.left=Node(value)
						break

				elif(value>current.value):
					if(current.right!=None):
						current=current.right
					else:
						current.right=Node(value)
						break
				else:
					break

bs=tree()
bs.create(34)
bs.create(32)
