import uuid
import abc
from typing import List


class PersonalInfo:
	"""Representation of person
	   ------------------------------
	   
		Argument:
		
		first_name : str
			first name
		last_name : str
			last name
		id : uuid.UUID
			id of the stuff/passenger
		
		
	"""
	
	def __init__(self, first_name: str, last_name: str, id: uuid.UUID):
		"""
			Method to create a new personal info
			
			Parameters:
			-----------
			
			first_name : str
				first name
			last_name : str
				last name
			id : uuid.UUID
				id of the stuff/passenger
			
				
			-----------
			
			"""
		self.first_name = first_name
		self.last_name = last_name
		self.id = id
	
	def get_first_name(self):
		"""
			Method to get first name of the person
			
			Parameters:
			-----------
			
			None
			
			-----------
			
			Return
			
			first_name : str
			"""
		return self.first_name
	
	def get_second_name(self):
		"""
			Method to get second name of the person
			
			Parameters:
			-----------
			
			None
			
			-----------
			
			Return
			
			second_name : str
			"""
		return self.second_name
	
	def get_id(self):
		"""
			Method to get id of the person
			
			Parameters:
			-----------
			
			None
			
			-----------
			
			Return
			
			id : uuid.UUID
			"""
		return self.id


class Passenger(PersonalInfo):
	"""Representation of passenger
	   ------------------------------
	   
		Argument:
		
		start_position : str
			Position where route starts
		finish_position : str
			Position where route ends
		first_name : str
			first name
		last_name : str
			last name
		id : uuid.UUID
			id of the passenger
			
	"""
	
	def __init__(self, start_position: str, finish_position: str, first_name: str, last_name: str):
		"""
		Method to create a new passenger
		
		Parameters:
		-----------
		
		start_position : str
			Position where route starts
		finish_position : str
			Position where route ends
		first_name : str
			first name
		last_name : str
			last name
		id : uuid.UUID
			id of the passenger
		
			
		-----------
		
		"""
		id = uuid.uuid4()
		super().__init__(first_name, last_name, id)
		
		self.finish_position = finish_position
		self.start_position = start_position
	
	def get_ticket(self):
		"""
		Method to get passengers ticket
		
		Parameters:
		-----------
		
		None
		
		-----------
		
		Return
		
		ticket : uuid.UUID/None
		
		"""
	
		if self.ticket:
			return self.ticket
		
class Driver(PersonalInfo):
	"""Representation of driver
	   ------------------------------
	   
		Argument:
		
		start_position : str
			Position where route starts
		finish_position : str
			Position where route ends
		first_name : str
			first name
		last_name : str
			last name
		id : uuid.UUID
			id of the driver
			
	"""
	
	def __init__(self, first_name: str, last_name: str , tickets : List[uuid.UUID]=[]):
		"""
		Method to create a new driver
		
		Parameters:
		-----------
		
		first_name : str
			first name
		last_name : str
			last name
		id : uuid.UUID
			id of the driver
		tickets : List[uuid.UUID]
			list of the ticket , so
			driver can check passenger`s
			tickets
		
			
		-----------
		
		"""
		id = uuid.uuid4()
		super().__init__(first_name, last_name, id)
		self.tickets = tickets
	
	def check_ticket(self,passenger : Passenger) -> bool:
		"""
		Method to get passengers ticket
		
		Parameters:
		-----------
		
		None
		
		-----------
		
		Return
		
		ticket : uuid.UUID/None
		
		"""

		if Passenger.get_ticket() in self.tickets:
			print("You are ok to take your seat")
			return True
		else:
			print("You dont have tickets , or your ticket is not in a list")
			return  False
		

		
