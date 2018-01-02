import random

class Floor:
    

    def __init__(self, floor_no):
        self.floor_no = floor_no
        self.capacity = {}
        self.parked_vehicle = {}
        
    def set_slot(self, types, count):
        self.capacity[types] = count

    def park(self, vehicle):
        self.capacity[vehicle.vehicle_type] -= 1
        self.parked_vehicle[vehicle.vehicle_number] = vehicle.vehicle_type
        return self.parked_vehicle

    def unpark(self, vehicle):
        self.capacity[vehicle.vehicle_type] += 1
        del self.parked_vehicle[vehicle.vehicle_number]
        return unparked    
        
        
        
floor1 = Floor("floor1")
floor1.set_slot("Car", 10)
floor1.set_slot("Bike", 10)
floor1.set_slot("Van", 10)
floor1.set_slot("Bus", 10)

floor2 = Floor("floor2")
floor2.set_slot("Bike", 1)
floor2.set_slot("Van", 1)
floor2.set_slot("Car", 1)

floor3 = Floor("floor3")
floor3.set_slot("Car", 10)
floor3.set_slot("Bike", 10)


class Vehicles:


    def vehicle_info(self, number, category):
        self.number = number
        self.catagory = category
        return self.number, self.category

vehicle = Vehicles()


class ParkingController():
    
    def __init__(self):
        self.list = []

    def check_floor_space(self, floor, Success):
        if self.vehicle in floor.capacity:
            if floor.capacity[self.vehicle] > 0:
                self.list.append(floor)
                Success = True
            else:
                Success = False 
        else:
            print "This type of vehicle not allowed"
        return Success

    def check_vehicle_number(self, floor, Success):
        if number in floor.parked_vehicle.keys():
            Success = True
        else:
            Success = False
        return Success

    def vehicle_info(self):
        self.vehicle = str(raw_input("Enter vehicle type:"))
        number = int(raw_input("Enter vehicle number:"))
        return self.vehicle, number

    def display(self, floor):
        print "\tFloor:",floor.floor_no
        print "\tParked vehicles:%r" %floor.parked_vehicle

build = ParkingController()
build.__add__(floor1)
build.__add__(floor2)
build.__add__(floor3)

success = True
while success:
    choice = int(raw_input(""" 1.Park\n 2.Unpark\n 3.Search Vehicles\n 4.Exit\n Enter your choice:"""))
    if choice == 1:
        v_num, v_type = build.visitor_vehicle()
        ticket, park_info = build.park(v_num, v_type)
        build.display(ticket, park_info)

    elif choice == 2:
        build.unpark()
    
    elif choice == 3:
        ticket, park_info = build.search_vehicle()
        build.display(ticket, park_info)

    elif choice == 4:
        success == False
        exit()

