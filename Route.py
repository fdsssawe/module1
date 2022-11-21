from geopy.geocoders import Nominatim
import openrouteservice
import abc

client = openrouteservice.Client(key="5b3ce3597851110001cf62483fedf16304f5428caca572a7683849b3")
geolocator = Nominatim(user_agent="customer")




class Route:
	"""Representation of route search
	   ------------------------------
	   
		Argument:
		start_position : str
			Position where route starts
		start_position : str
			Position where route starts
			
		
	"""
	
	def __init__(self, start_position: str, finish_position: str):
		"""
		Method to create a new route
		
		Parameters:
		-----------
		
		start_position : str
			Position where route starts
		start_position : str
			Position where route starts
			
		-----------
			
		"""
		self.start_position = start_position
		self.finish_position = finish_position
	
	def get_calculated_coordinates(self):
		"""
		Method to calculate a longitude and latitude of both start and finish positions
		
		Parameters:
		-----------
		
		None
		
		-----------
		
		Return:
		
		coordinates for route calculation
			
		"""
		start_location = geolocator.geocode(self.start_position)
		start_lon = start_location.longitude
		start_lat = start_location.latitude
		finish_location = geolocator.geocode(self.finish_position)
		finish_lon = finish_location.longitude
		finish_lat = finish_location.latitude
		coordinates = ((start_lon, start_lat), (finish_lon, finish_lat))
		
		return coordinates
	
	def get_calculated_route(self):
		"""
		Method to calculate a route by provided coordinates
		
		Parameters:
		-----------
		
		None
		
		-----------
		
		Return:
		
		None
		
		"""
		coordinates = self.get_calculated_coordinates()
		routes = client.directions(coordinates, profile="driving-hgv")
		route = client.directions(coordinates, profile="driving-hgv",format = "geojson")
		print(f"Distance: {round(routes['routes'][0]['summary']['distance'] / 1000, 1)} km.")
		print(f"Time in hours: {round(routes['routes'][0]['summary']['duration'] / 3600, 1)}.")
		print(f"Passing : ")
		for i in (route['features'][0]['properties']['segments'][0]['steps']):
			print(i["name"] , " ; ")
