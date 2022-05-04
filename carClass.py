#Car class will create cars with a unique license plate number
#Car class will have a park method that will park car to specified parking spot number 

import random
import string

class Car:

	def __init__(self, license_plate_num):
		self.license_plate_num = license_plate_num


	def park(self, parking_lot, spot_number):

		canPark = True

		while canPark:
			if parking_lot[spot_number] == 0:
				#assign Car License Plate Num to spot
				parking_lot[spot_number] = self.license_plate_num
				print("Car with License Plate #: ", self.license_plate_num, " parked in spot number: ", spot_number, " succesfully!\n")
				break
			else:
				#breaks out of loop 
				print("Unfortunately that parking spot is already occupied, please hold while we look for an available location..")
				canPark = False
				break

		while not canPark:
			#create a new random int to try park in that spot 
			#will keep trying arbitrary spot nums until open spot is found
			randnum = random.randint(0,len(parking_lot)-1)

			if parking_lot[randnum] == 0:
				#assign Car License Plate Num to spot
				parking_lot[randnum] = self.license_plate_num
				print("We found a spot! Car with License Plate #: ", self.license_plate_num, " was parked in spot number: ", spot_number, " succesfully!\n")
				canPark = True
			else:
				canPark = False
				break

	def __str__(self):

		return f"\nThis car's license plate # is : {self.license_plate_num}.\n"
