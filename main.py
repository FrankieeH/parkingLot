import carClass
import parkingLotClass as PL
import random
import string

lot_squareft = 0
parkingspot_squareft = 0
num_of_cars = 0
carArray = []



def user_input_lot():
	lot_squareft = input("Please enter the desired square footage for your parking lot or enter 0 for default: (Default is 2000 sq ft)")

	if lot_squareft == '0':
		lot_squareft = 2000

	return int(lot_squareft)


def user_input_spot():
	parkingspot_squareft = input("Please entered the desired square footage for each parking spot or enter 0 for default: (Default is 8x12 = 96 sqft)")

	if parkingspot_squareft == '0':
		parkingspot_squareft = 96

	return int(parkingspot_squareft)


def user_input_cars():
	cars_to_park = input('Please enter amount of cars you wish to attempt to park: ')

	return int(cars_to_park)


def create_cars(carAmount):

	for num in range(0,carAmount):
		letters_and_digits = string.ascii_letters + string.digits
		result_str = ''.join((random.choice(letters_and_digits) for i in range(7)))

		#print('Car License Plate # for this car is: ',result_str)

	#create a Car for each License Plate created and add them to Car Array
		carArray.append(carClass.Car(result_str))
		#print('\n',carArray[num].license_plate_num)

def time_to_park():

	total = 0 

	for i in range(0,len(carArray)):

		randnum = random.randint(0,(lot1.total_parking_spots)-1)
		print("Attempting to park Car in spot #: ", randnum)

		if total < len(lot1.parking_lot_array):
			carArray[i].park(lot1.parking_lot_array,randnum)
		else:
			print("Parking Lot has reached full capacity. Unable to park Car with License Plate Number: ", carArray[i].license_plate_num, "Sorry, come again another time!\n")

		total +=1


		#print("Parking spots attempted to be  filled: ", total)
		#print("Total parking spots available: ", lot1.total_parking_spots)






print("Welcome to Frankie's Parking Lot Services\n")


print("First let's create the Parking Lot\n")

lot_squareft = user_input_lot()
parkingspot_squareft = user_input_spot()


#default parking lot square footage will be 2000 for now
#default parking spot square footage will be 96 for now

#we created a parking lot object from parkingLot Class
lot1 = PL.parkingLot(lot_squareft, parkingspot_squareft)

#print out the parking lot to make sure it exists
print('\n',lot1,'\n')


#next we need to create an array of cars with random License Plate #'s
#we can play around with the total number of cars created to be less, equal to, or more than the parking lot can fit

num_of_cars = user_input_cars()

create_cars(num_of_cars)

time_to_park()








