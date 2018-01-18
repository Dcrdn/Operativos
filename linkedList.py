from node import *

class SinglyLinkedList:

	def __init__(self):
		self.head = None

	def setHead(self,head):
		self.head = head
	
	def insert(self, data):
		node=Node()
		node.setData(data)
		if(self.head==None):
			self.setHead(node)
		else:
			current=self.head
			while(current.getNext()!=None):
				current=current.getNext()
			current.setNext(node)

	def iterate(self):
		current=self.head
		while(current!=None):
			print(current.getData())
			current=current.getNext()

	def getSize(self):
		current=self.head
		nodos=1
		while(current!=None):
			print(current.getData())
			current=current.getNext()
			nodos+=1
		return nodos

	def iterateBack(self):
		last=None
		current=self.head
		while(current!=None):
			next=current.getNext()
			current.setNext(last)
			last=current
			current=next

	def reverse(self):
		last=None
		current=self.head
		while(current!=None):
			next=current.getNext()
			current.setNext(last)
			last=current
			current=next
		
		current=last
		while(current!=None):
			current=current.getNext()

	def addFirst(self,data):
		if(self.head==None):
			self.head=data
		else:
			node=Node()
			node.setData(data)
			node.setNext(self.head)
			self.head=node

	def find(self, data):
		current=self.head
		while(current!=None):
			if(current.getData()==data):
				return True
			current=current.getNext()
		return False

	def remove(self, data):
		if(data==None):
			return False
		if(self.head==data):
			self.head=data.getNext()
			return True
		current=self.head
		next=current.getNext()
		while(current!=None):
			if(next.getData()==data):
				current.setNext(current.getNext().getNext())
				return True
			current=current.getNext()
		return False

	def deleteLast(self):
		if(self.head==None):
			return True
		current=self.head
		if(current.getNext==None):
			self.head=None
			return True
		current=self.head
		
		while(current.getNext()!=None):
			current=current.getNext()
		current.setData=None


lista=SinglyLinkedList()
lista.insert(23)
lista.insert(24)
lista.insert(25)
lista.insert(45)
lista.insert(26)
lista.iterate()
#lista.iterateBack()
print("---")
lista.addFirst(1)
lista.iterate()
print("---")
lista.remove(45)
lista.iterate()