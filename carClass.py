#Car class will create cars with a unique license plate number
#Car class will have a park method that will park car to specified parking spot number 

import random
import string

class Car:

	def __init__(self, license_plate_num):
		self.license_plate_num = license_plate_num
		self.can_park = True


	def park(self, parking_lot):
		while self.can_park:
			spot_number = random.randint(0,len(parking_lot)-1)
			if parking_lot[spot_number] == 0:
				#assign Car License Plate Num to spot
				parking_lot[spot_number] = self.license_plate_num
				print("Car with License Plate #: ", self.license_plate_num, " parked in spot number: ", spot_number, " succesfully!\n")
				self.can_park = True
				return True
			print("Unfortunately that parking spot is already occupied, please hold while we look for an available location..")


	def __str__(self):
		return str(self.license_plate_num)

	def __repr__(self) -> str:
		return str(self)
