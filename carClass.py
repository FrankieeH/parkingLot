#Car class will create cars with a unique license plate number
#Car class will have a park method that will park car to specified parking spot number 

class Car:

	def __init__(self, license_plate_num):
		self.license_plate_num = license_plate_num


	def park(self, parking_lot, spot_number):

		canPark = True

		while canPark:
			if parking_lot[spot_number] == 0:
				#assign Car License Plate Num to spot
				pass
				
			else:
				#breaks out of loop 
				canPark = False
				break

		while not canPark:
			#create a new random int to try park in this spot
			if parking_lot[spot_number] == 0:
				#assign Car License Plate Num to spot
				pass
			else:
				canPark = False
				break
				#Loop keeps trying different parking spots at random until finds a spot



	def __str__(self):

		return f"This car's license plate # is : {self.license_plate_num}."
