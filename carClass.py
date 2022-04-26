

class Car:

	def __init__(self, license_plate_num):
		self.license_plate_num = license_plate_num


	def __str__(self):

		return f"This car's license_plate_num is : {self.license_plate_num}."

	def park(self):

		print("Im supposed to park cars, but not yet")
