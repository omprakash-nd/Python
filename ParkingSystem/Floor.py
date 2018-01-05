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
 
