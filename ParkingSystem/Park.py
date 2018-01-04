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
        return vehicle.vehicle_number
    
    def unpark(self, vehicle):
        self.capacity[vehicle.vehicle_type] += 1
        del self.parked_vehicle[vehicle.vehicle_number]
        return vehicle.vehicle_number
    
        
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
                    space = "Parked"
                    issuccess = True
                    break
                else:
                    space = "No free space"
                    issuccess = False
            else:
                not_allowed = "This type of vehicle not allowed"
                issuccess = False
        return floor, space, issuccess

    def check_vehicle(self, vehicle):
        issuccess = True
        for index in range(len(self.list)):
            floor = self.list[index]
            if vehicle.vehicle_number in floor.parked_vehicle:
                issuccess = True
                vehicle_detail = "Vehicle Available"
                break
            else:
                vehicle_detail = "No vehicle"
                issuccess = False
        return floor, vehicle_detail, issuccess

    def vehicle_info(self):
        vehicle_type = str(raw_input("Enter vehicle type:"))
        vehicle_number = int(raw_input("Enter vehicle number:"))
        return vehicle_type, vehicle_number
    
    def display(self, floor, info):
        print "\tFloor:",floor.floor_no
        print "\t", info
        print "\tParked vehicles:%r" %floor.parked_vehicle.keys()
        

build = ParkingController()
build.__add__(floor1)
build.__add__(floor2)
build.__add__(floor3)

success = True
while success:

    choice = int(raw_input(""" \n1.Park\n 2.Unpark\n 3.Exit\n Enter your choice:"""))    
    if choice == 1:
        v_type, v_number = build.vehicle_info()
        vehicle = Vehicles(v_type, v_number)
        floor, space, issuccess = build.check_space(vehicle)
        if issuccess:
            floor.park(vehicle)
            build.display(floor, space)
        else:
            print "No space / Vehicle not allowed"
        
    elif choice == 2:
        vehicle_type, vehicle_number = build.vehicle_info()
        vehicle = Vehicles(vehicle_type, vehicle_number)
        floor, vehicle_detail, issuccess = build.check_vehicle(vehicle)
        if issuccess:
            floor.unpark(vehicle)
            build.display(floor, vehicle_detail)
        else:
            print "Not parked"

    elif choice == 3:
        success = False
