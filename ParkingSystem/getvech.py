class Vehicle:


    def __init__(self, vehicle_type, type_count):
        self.vehicle_type = vehicle_type
        self.type_count = type_count
       
Bike = Vehicle("BIKE", 50)
Bus = Vehicle("BUS", 5)
Car = Vehicle("CAR", 10)
Van = Vehicle("VAN", 10)


class Park:


    list =[]
    def __add__(self, vehicle):
        self.list.append(vehicle)

    def display(self):
        default_values = []
        level_list =[]
        for Vehicle in range(len(self.list)):
            vehicle = self.list[Vehicle]
            default_values.append(vehicle.vehicle_type)
            default_values.append(vehicle.type_count)
            parking_limts=dict(map(None, *[iter(default_values)]*2))
            self.parking = parking_limts
        return default_values

    def getUserVehicle(self):
        vehicle_count = int(raw_input("Enter the number of vehicle's"))
        return vehicle_count

    def checkVehicle(self, vehicle_count, default_values):
        user_vehicle = []
        parking = self.parking
        for number in range(vehicle_count):
            user_vechile_type, user_vechile_count = str(raw_input("Enter your vechile type and count:")).split("-")
            user_vechile_type = user_vechile_type.upper()
            print parking[user_vechile_type]
            if user_vechile_type in default_values:
                user_vehicle.append(user_vechile_type)
                user_vehicle.append(user_vechile_count)
            else:
                print self.non_match()
        return user_vehicle

    def non_match(self):
        dismatched = "Your vehicle is not allowed to park"
        return dismatched

park = Park()
park.__add__(Bike) 
park.__add__(Bus)
park.__add__(Car)
park.__add__(Van)

limits = park.display()
count = park.getUserVehicle()
park.checkVehicle(count, limits)


## def getLevel(self):
##        level = int(input("How many Levels:"))
##        return level
##
##    def checkVehicleType(self, parking_limts, user_vechile_type, user_vechile_count):
##
##        for types,count in parking_limts.items():
##            if user_vechile_type in types:
##                if count < user_vechile_count:
##                    print "car count is higher"
##            else:
##                print "Not in list"
##                    

        
        
    
    







































##def getVechile(level, vechile_type_count):
##    vechicle_list = ['BIKE', 'CAR', 'VAN', 'BUS']
##    l = []
##
##    for i in range(level):
##        print "%r" %i
##        for j in range(vechile_type_count):
##            vechile_types, vechile_count = str(raw_input("Enter your Vechile Type and Count:")).split("-")
##            vechile_type = vechile_types.upper()
##        
##            if vechile_type in vechicle_list:
##                vechile = vechile_type
##                l.append(vechile)
##            else:
##                print "No"
##
##            if isinstance(vechile_count, str):
##               vechile_count = int(vechile_count)
##               l.append(vechile_count)
##            else:
##                vechile_count
##
##    d=dict(map(None, *[iter(l)]*2))
##    print d 
##    return vechile, vechile_count 
##
####def checkVechile():
##    
##a = getSizeOfLevel()
##b = getCountOfVechile()
##getVechile(a, b)
