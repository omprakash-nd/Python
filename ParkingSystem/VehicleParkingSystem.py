from Floor import Floor
from Vehicle import Vehicle
from ParkController import ParkingController

##Creating floor objects for Floor Class##

floor1 = Floor("floor1")
floor1.set_slot("Car", 10)
floor1.set_slot("Bike", 10)
floor1.set_slot("Van", 10)
floor1.set_slot("Bus", 10)

floor2 = Floor("floor2")
floor2.set_slot("Bike",10)
floor2.set_slot("Van", 5)
floor2.set_slot("Car", 10)

floor3 = Floor("floor3")
floor3.set_slot("Car", 5)
floor3.set_slot("Bike", 10)


##Adding each floor objects to ParkingController list##

build = ParkingController()
build.__add__(floor1)
build.__add__(floor2)
build.__add__(floor3)



success = True
while success:

    choice = int(raw_input(""" \n1.Park\n 2.Unpark\n 3.Exit\n Enter your choice:"""))    
    if choice == 1:
        vehicle_type, vehicle_number = build.vehicle_info()                   
        vehicle = Vehicle(vehicle_type, vehicle_number)                       ##Creating vehicle objects for Vehicle
        floor, space, issuccess = build.check_space(vehicle)
        if issuccess:
            floor.park(vehicle)                                 
            build.display(floor, space)
        else:
            print "No space / Vehicle not allowed"
        
    elif choice == 2:
        vehicle_type, vehicle_number = build.vehicle_info()
        vehicle = Vehicle(vehicle_type, vehicle_number)
        floor, vehicle_detail, issuccess = build.check_vehicle(vehicle)
        if issuccess:
            floor.unpark(vehicle)
            build.display(floor, vehicle_detail)
        else:
            print "Not parked"

    elif choice == 3:
        success = False


##Sample Output

        
##1.Park
## 2.Unpark
## 3.Exit
## Enter your choice:1
##Enter vehicle type:Car
##Enter vehicle number:3455
##	Floor: floor1
##	Space Available
##	Parked vehicles:[3455]
## 
##1.Park
## 2.Unpark
## 3.Exit
## Enter your choice:1
##Enter vehicle type:Van
##Enter vehicle number:5467
##	Floor: floor1
##	Space Available
##	Parked vehicles:[5467, 3455]
## 
##1.Park
## 2.Unpark
## 3.Exit
## Enter your choice:1
##Enter vehicle type:Bus
##Enter vehicle number:4566
##	Floor: floor1
##	Space Available
##	Parked vehicles:[5467, 4566, 3455]
## 
##1.Park
## 2.Unpark
## 3.Exit
## Enter your choice:2
##Enter vehicle type:Car
##Enter vehicle number:3455
##	Floor: floor1
##	Vehicle Available
##	Parked vehicles:[5467, 4566]
