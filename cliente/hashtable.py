#!/usr/bin/python3
# Capacity for internal array
from keyring.backends import null

INITIAL_CAPACITY = 50

# Node data structure - essentially a LinkedList node
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	def __str__(self):
		return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
	def __repr__(self):
		return str(self)
# Hash table with separate chaining
class HashTable:
	# Initialize hash table
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None]*self.capacity
	# Generate a hash for a given key
	# Input:  key - string
	# Output: Index from 0 to self.capacity
	def hash(self, key):
		hashsum = 0
		# For each character in the key
		for idx, c in enumerate(key):
			# Add (index + length of key) ^ (current char code)
			hashsum += (idx + len(key)) ** ord(c)
			# Perform modulus to keep hashsum in range [0, self.capacity - 1]
			hashsum = hashsum % self.capacity
		return hashsum

	# Insert a key,value pair to the hashtable
	# Input:  key - string
	# 		  value - anything
	# Output: void
	def insert(self, key, value):
		# 1. Increment size
		self.size += 1
		# 2. Compute index of key
		index = self.hash(key)
		# Go to the node corresponding to the hash
		node = self.buckets[index]
		# 3. If bucket is empty:
		if node is None:
			# Create node, add it, return
			self.buckets[index] = Node(key, value)
			return "True"
		# 4. Iterate to the end of the linked list at provided index
		prev = node
		while node is not None:
			prev = node
			node = node.next
		# Add a new node at the end of the list with provided key/value
		prev.next = Node(key, value)
		return "True"

	# Find a data value based on key
	# Input:  key - string
	# Output: value stored under "key" or None if not found
	def find(self, key):
		# 1. Compute hash
		index = self.hash(key)
		# 2. Go to first node in list at bucket
		node = self.buckets[index]
		# 3. Traverse the linked list at this node
		while node is not None and node.key != key:
			node = node.next
		# 4. Now, node is the requested key/value pair or None
		if node is None:
			# Not found
			return "CLIENTE N??O ENCONTRADA"
		else:
			# Found - return the data value
			return node.value

	def validaSenha(self, key, senha):
		# 1. Compute hash
		index = self.hash(key)
		# 2. Go to first node in list at bucket
		node = self.buckets[index]
		# 3. Traverse the linked list at this node
		while node is not None and node.key != key:
			node = node.next
		# 4. Now, node is the requested key/value pair or None
		if node is None:
			# Not found
			return "ID Inv??lido"
		else:
			if node.value[1] == senha:
				return "True"
			return "Senha Incorreta"

	# Remove node stored at key
	# Input:  key - string
	# Output: removed data value or None if not found
	def remove(self, key):
		# 1. Compute hash
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		# 2. Iterate to the requested node
		while node is not None and node.key != key:
			prev = node
			node = node.next
		# Now, node is either the requested node or none
		if node is None:
			# 3. Key not found
			return "N??o Encontrado!!!"
		else:
			# 4. The key was found.
			self.size -= 1
			result = node.value
			# Delete this element in linked list
			if prev is None:
				self.buckets[index] = node.next # May be None, or the next match
			else:
				prev.next = prev.next.next # LinkedList delete by skipping over
			# Return the deleted result
			return "True"

	def setnome(self, key, nome):
		index = self.hash(key)
		node = self.buckets[index]
		while node is not None and node.key != key:
			node = node.next
		if node is None:
			return "N??O ENCONTRADO"
		else:
			node.value[0]=nome
			return node.value[0]

	def setsenha(self, key, senha):
		index = self.hash(key)
		node = self.buckets[index]
		while node is not None and node.key != key:
			node = node.next
		if node is None:
			return "N??O ENCONTRADO"
		else:
			node.value[1]=senha
			return node.value[1]

	def listaTarefas(self, key):
		index = self.hash(key)
		node = self.buckets[index]
		lista = [[]]*self.size
		aux = 0
		i = 0
		while i != INITIAL_CAPACITY and node is not None:
			if node.key == key and node.value[1] == "PENDENTE":
				lista[aux] = [node.key, node.value]
				aux+=1
			node = node.next
		if lista == [""]:
			return "LISTA DE TAREFAS N??O ENCONTRADA"
		else:
			# Found - return the data value
			return lista

	def listaConcluidas(self, key):
		index = self.hash(key)
		node = self.buckets[index]
		lista = [[]] * self.size
		aux = 0
		i = 0
		while i != INITIAL_CAPACITY and node is not None:
			if node.key == key and node.value[1] == "CONCLUIDO":
				lista[aux] = [node.key, node.value]
				aux += 1
			node = node.next
		if lista == [""]:
			return "LISTA DE TAREFAS N??O ENCONTRADA"
		else:
			# Found - return the data value
			return lista

	def removeTarefa(self, key, keyTarefa):
		# 1. Compute hash
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		# 2. Iterate to the requested node
		while node is not None:
			if(node.key == key and node.value[2] == keyTarefa):
				if prev is None:
					self.buckets[index] = node.next  # May be None, or the next match
				else:
					prev.next = prev.next.next  # LinkedList delete by skipping over
				return "True"
			prev = node
			node = node.next
		if node is None:
			# 3. Key not found
			return "TAREFA N??O ENCONTRADA"


	def findtarefa(self, key, keyTarefa):
		# 1. Compute hash
		index = self.hash(key)
		# 2. Go to first node in list at bucket
		node = self.buckets[index]
		# 3. Traverse the linked list at this node
		while node is not None:
			if (node.key == key and node.value[2] == keyTarefa):
			   return node.value
			node = node.next
		# 4. Now, node is the requested key/value pair or None
		if node is None:
			# Not found
			return "TAREFA N??O ENCONTRADA"



	def concluitarefa(self, key, keyTarefa):
		index = self.hash(key)
		node = self.buckets[index]
		while node is not None:
			if(node.key == key and node.value[2] == keyTarefa):
				node.value[1] = "CONCLUIDO"
				return "True"
			node = node.next
		if node is None:
			return "N??O ENCONTRADO"


	def setnometarefa(self, key, keyTarefa, nomeTarefa):
		index = self.hash(key)
		node = self.buckets[index]
		while node is not None:
			if (node.key == key and node.value[2] == keyTarefa):
				node.value[0] = nomeTarefa
				return "True"
			node = node.next
		if node is None:
			return "N??O ENCONTRADO"
