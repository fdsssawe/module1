from abc import ABC, abstractmethod
from Route import Route


class Transport(ABC):
	"""Representation of transport
	   ------------------------------
	   
		Argument:
		
		routes: defaultdict(list)
			route that transport follow
		
		
	"""
	
	def __init__(self, route: Route):
		"""Method to create transport
		 
			Parameters:
			-----------
			
			routes: defaultdict(list)
				route that transport follow
				
			-----------
			
			
		"""
		self.route = route
	
	@abstractmethod
	def change_route(self, route: Route) -> Route:
		pass
	
	@abstractmethod
	def start_route(self) -> None:
		pass


class Buss(Transport):
	"""Representation of buss
	   ------------------------------
	   
		Argument:
		
		routes: defaultdict(list)
			route that buss follow
		
	"""
	
	def __init__(self, route: Route):
		"""Method to create bus
		   
			Parameters:
			-----------
			
			routes: defaultdict(list)
				route that bus follow
				
			-----------
			
			
		"""
		self.route = route
		
	def change_route(self, route: Route) -> Route:
		"""Method to change route of bus
		   
			Parameters:
			-----------
			
			routes: defaultdict(list)
				route that bus follow now
				
				
			-----------
			Return
			
			New route : Route
			
		"""
		self.route = route
		return self.route
	
	def start_route(self) -> None:
		"""Method to start the route
		   
			Parameters:
			-----------

			None
			
			-----------
			Return
			
			None
			
		"""
		pass
