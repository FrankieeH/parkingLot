
class parkingLot:

	def __init__(self, square_footage, parking_spot_size =96):
		self.square_footage = square_footage
		self.parking_spot_size = parking_spot_size
		self.total_parking_spots = int(square_footage / parking_spot_size)


	def __str__(self):
		print("I announce a Parking lot was created")

