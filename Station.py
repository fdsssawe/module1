import uuid
from typing import List
from collections import defaultdict
from StuffAndPassengers import Driver, Passenger
from Route import Route


class StationInfo:
	"""Representation of Station
	   ------------------------------
	   
		Argument:
		
		routes: defaultdict(list)
			list of routes , and passengers for them
		busses: defaultdict(list)
			list of routes , and busses for them
		
		
	"""
	
	def __init__(self, routes: defaultdict(list), busses: defaultdict(list)):
		"""
			Method to create a new station
			
			Parameters:
			-----------
			
		routes: defaultdict(list)
			list of routes , and passengers for them
		busses: defaultdict(list)
			list of routes , and busses for them
			
			
			-----------
			
			"""
		self.routes = routes
		self.busses = busses


class Station(StationInfo):
	"""Representation of Station
	   ------------------------------
	   
		Argument:

		routes: defaultdict(list)
			list of routes , and passengers for them
		busses: defaultdict(list)
			list of routes , and busses for them
		
	"""
	
	def __init__(self, routes: defaultdict(list), busses: defaultdict(list)):
		"""
			Method to create a new station
			
			Parameters:
			-----------
			
		routes: defaultdict(list)
			list of routes , and passengers for them
		busses: defaultdict(list)
			list of routes , and busses for them
			
			
			-----------
			
			"""
		super(Station, self).__init__(routes, busses)
	
	def manage_transport(self, route: Route) -> bool:
		"""
			Method to manage busses
			
			Parameters:
			-----------
			
			route : Route
				Route that you want to manage
		
			-----------
			Return
			
			True/False
			"""
		if route in self.routes:
			if self.routes[route].length > 10:
				self.busses[route].start_route
				return True
			else:
				print("Not enough passengers")
				return False


class Cashier():
	"""Representation of Cashier
	   ------------------------------
	   
		Argument:
		
		driver : Driver
			Driver of the bus on route
		passenger : Passenger
			Passenger who want to buy a ticket
		station : Station
			Station where cashier is
		

		
	"""
	
	
	
	def buy_ticket(self, driver: Driver, passenger: Passenger, station: Station):
		"""
			Method to buy ticket
			
			Parameters:
			-----------
			
			Argument:
			
			driver : Driver
				Driver of the bus on route
			passenger : Passenger
				Passenger who want to buy a ticket
			station : Station
				Station where cashier is
			
			
			-----------
			
			"""
		new_ticket = uuid.uuid4()
		passenger.ticket = new_ticket
		driver.tickets.append(new_ticket)
		station.routes[Route(passenger.start_position, passenger.finish_position)].append(passenger.id)
	
	def return_ticket(self, driver: Driver, passenger: Passenger, station: Station, ticket: uuid.UUID):
		"""
			Method to return the ticket
			
			Parameters:
			-----------
			
			Argument:
			
			driver : Driver
				Driver of the bus on route
			passenger : Passenger
				Passenger who want to return a ticket
			station : Station
				Station where cashier is
			
			
			-----------
			
			"""
		passenger.ticket = None
		driver.tickets.pop(ticket)
		station.routes[Route(passenger.start_position, passenger.finish_position)].pop(passenger.id)
