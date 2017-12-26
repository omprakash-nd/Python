class Floor:
    

    def __init__(self, floor_no):
        self.floor_no = floor_no
        self.park = {}
        self.dict = {}
        
    def set_slot(self, types, count):
        self.dict[types] = count

    def capacity(self, floor):
        self.park[floor.floor_no] = self.dict

    def display(self):
        list = []
        list.append(self.park)
        return list


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


    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number 
        self.vehicle_type = vehicle_type

    def display(self):
        return self.vehicle_number + " " + self.vehicle_type
        

vehicle = Vehicles(int(raw_input("Enter vehicle number:")), str(raw_input("Enter vehicle type:")))
user_num, user_type = vehicle.display()
    
class Parker(Vehicles):


    def add_parklot(self, floor):
        for key, values in floor.park.items():
            for key,val in values.items():
                
           
           
park = Parker()
park.add_parklot(floor1)
park.vehicle(user_num, user_type)
