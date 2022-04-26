#Car class will create cars with a unique license plate number
#Car class will have a park method that will park car to specified parking spot number 

class Car:

	def __init__(self, license_plate_num):
		self.license_plate_num = license_plate_num


	def __str__(self):

		return f"This car's license plate # is : {self.license_plate_num}."

	def park(self, parking_lot, spot_number):

		print("Im supposed to park cars, but not yet")
