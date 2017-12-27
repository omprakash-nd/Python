class Floor:
    

    def __init__(self, floor_no):
        self.floor_no = floor_no
        self.slot = {}
        self.space = {}
        
    def set_slot(self, types, count):
        self.slot[types] = count

    def capacity(self, floor):
        self.space[floor.floor_no] = self.slot
        return self.space

    def parked_vehicle(self, floor):
        return [floor.space]
    
floor1 = Floor("floor1")
floor1.set_slot("Car", 10)
floor1.set_slot("Bike", 10)
floor1.set_slot("Van", 10)
floor1.set_slot("Bus", 10)
floor1.capacity(floor1)

floor2 = Floor("floor2")
floor2.set_slot("Bike", 1)
floor2.set_slot("Van", 1)
floor2.set_slot("Car", 1)
floor2.capacity(floor2)

floor3 = Floor("floor3")
floor3.set_slot("Car", 10)
floor3.set_slot("Bike", 10)
floor3.capacity(floor3)


class Vehicles:


    def vehicle_info(self):
        number = int(raw_input("Enter vehicle number:"))
        category = str(raw_input("Enter vehicle type:"))
        return number, category

vehicle = Vehicles()


class ParkingController():

    def __init__(self):
        self.list = []
        self.parked_vehicle = {}
    
    def __add__(self, floor):
        self.list.append(floor)

    def system(self):
        vehicle_number, vehicle_type = vehicle.vehicle_info()
        return vehicle_number, vehicle_type

    def park(self, vehicle_number, vehicle_type):
        for i in self.list:
            for floor, values in i.items():
                if vehicle_type in values.keys():
                    space = values[vehicle_type]
                    if space >= 1:
                        assign = [floor, vehicle_number, vehicle_type]
                        self.parked_vehicle[vehicle_number] = assign
                        break
    def display(self):
        print self.list
        print self.parked_vehicle
        return self.list

               
build = ParkingController()
build.__add__(floor1.space)
build.__add__(floor2.space)
build.__add__(floor3.space)

success = True
while success:
    choice = int(raw_input())
    if choice == 1:
        v_num, v_type = build.system()
        build.park(v_num, v_type)
    elif choice == 2:
        success = False

build.display()


