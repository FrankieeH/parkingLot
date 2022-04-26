#parking lot class takes in square footage and parking spot square footage
#default parking spot square footage is 96
#we can calculate how many total cars can fit

class parkingLot:

	def __init__(self, square_footage, parking_spot_size =96):
		self.square_footage = square_footage
		self.parking_spot_size = parking_spot_size
		self.total_parking_spots = int(self.square_footage / self.parking_spot_size)
		self.parking_lot_array = [0] * self.total_parking_spots


	def __str__(self):
		
		return f'\nThis parking lot is {self.square_footage} square feet and can fit a total of {self.total_parking_spots} cars!'

