class Floor:
    

    def __init__(self, floor_no):
        self.floor_no = floor_no
        self.capacity = {}
        self.parked_vehicle = {}
        
    def set_slot(self, types, count):
        self.capacity[types] = count

    def park(self, vehicle):
        self.capacity[vehicle.vehicle_type] -= 1
        self.parked_vehicle[vehicle.vehicle_number] = vehicle
        return self.parked_vehicle
    
    def unpark(self, vehicle):
        self.capacity[vehicle.vehicle_type] += 1
        del self.parked_vehicle[vehicle.vehicle_number]
        return self.parked_vehicle
    
        
floor1 = Floor("floor1")
floor1.set_slot("Car", 0)
floor1.set_slot("Bike", 0)
floor1.set_slot("Van", 0)
floor1.set_slot("Bus", 0)

floor2 = Floor("floor2")
floor2.set_slot("Bike", 0)
floor2.set_slot("Van", 0)
floor2.set_slot("Car", 1)

floor3 = Floor("floor3")
floor3.set_slot("Car", 0)
floor3.set_slot("Bike", 0)


class Vehicles:


      def __init__(self, vehicle_type, vehicle_number):
        self.vehicle_type = vehicle_type
        self.vehicle_number = vehicle_number


class ParkingController():
    
    def __init__(self):
        self.list = []

    def __add__(self, floor):
        self.list.append(floor)

    def check_space(self, vehicle):
        issuccess = True
        for index in range(len(self.list)):
            floor = self.list[index]
            if vehicle.vehicle_type in floor.capacity:
                if floor.capacity[vehicle.vehicle_type] > 0:
                    issuccess = True
                    break
                else:
                    nospace = "No free space"
                    issuccess = False
            else:
                not_allowed = "This type of vehicle not allowed"
                issuccess = False
        return floor, issuccess

    def check_vehicle(self, vehicle):
        issuccess = True
        for index in range(len(self.list)):
            floor = self.list[index]
            if vehicle.vehicle_number in floor.parked_vehicle:
                issuccess = True
                break
            else:
                no_vehicle = "No vehicle"
                issuccess = False
        return floor, issuccess

    def vehicle_info(self):
        vehicle_type = str(raw_input("Enter vehicle type:"))
        vehicle_number = int(raw_input("Enter vehicle number:"))
        return vehicle_type, vehicle_number

    def display(self, floor):
        print "\tFloor:",floor.floor_no
        print "\tParked vehicles:%r" %floor.parked_vehicle.keys()
        

build = ParkingController()
build.__add__(floor1)
build.__add__(floor2)
build.__add__(floor3)

success = True
while success:

    choice = int(raw_input(""" \n1.Park\n 2.Unpark\n 3.Exit\n Enter your choice:"""))    
    if choice == 1:
        vehicle_type, vehicle_number = build.vehicle_info()
        vehicle = Vehicles(vehicle_type, vehicle_number)
        floor, issuccess = build.check_space(vehicle)
        if issuccess:
            floor.park(vehicle)
            build.display(floor)
        else:
            print "No space / Vehicle not allowed"
        
    elif choice == 2:
        vehicle_type, vehicle_number = build.vehicle_info()
        vehicle = Vehicles(vehicle_type, vehicle_number)
        floor, issuccess = build.check_vehicle(vehicle)
        if issuccess:
            floor = floor.unpark(vehicle)
            build.display(floor)
        else:
            print "Not parked"

    elif choice == 3:
        success = False
