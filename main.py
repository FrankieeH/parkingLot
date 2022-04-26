import carClass
import parkingLotClass
import random
import string

carArray = []



print("Welcome to Frankie's Parking Lot Services\n")


print("First let's create the Parking Lot")

#default parking lot square footage will be 2000 for now
#default parking spot square footage will be 96 for now

#we created a parking lot object from parkingLot Class
lot1 = parkingLotClass.parkingLot(2000)

print('\n',lot1,'\n')

#next we need to create an array of cars with random License Plate #'s
#we can play around with the total number of cars created to be less, equal to, or more than the parking lot can fit
#default amount of cars/License plate numbers created FOR NOW is 20

for num in range(0,20):
	letters_and_digits = string.ascii_letters + string.digits
	result_str = ''.join((random.choice(letters_and_digits) for i in range(7)))

	print('Car License Plate # for this car is: ',result_str)

	#create a Car for each License Plate created and add them to Car Array
	carArray.append(carClass.Car(result_str))
	print('\n',carArray[num].license_plate_num)


