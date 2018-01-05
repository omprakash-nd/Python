
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
                    space = "Space Available"
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
        


