from uuid import uuid4

class Action:
	def __init__(self, value):
		# A value may either be an atomic action
		# or a reference to another team by id.
		self.id: str = str(uuid4()) 
		self.value: str = value

	def __str__(self) -> str:
		return self.value
