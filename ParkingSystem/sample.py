class Vehicle:


    def park_limits(self):

        park_dict = {
                "BIKE":30,
                "BUS":5,
                "CAR":20,
                "VAN":15,
                }
        return park_dict


class User(Vehicle):


    def restrict_vehicle(self, park_dict):
        
        rest_vehicle = str(raw_input("which vehicle type you restrict:"))
        if rest_vehicle in park_dict.keys():
            park_dict[rest_vehicle] = None
        else:
            print "This type of vehicle not in your list"
        return park_dict, rest_vehicle

    def unrestrict_vehicle(self, default_dict, park_dict, rest_vehicle):
        
        park_dict[rest_vehicle] = default_dict[rest_vehicle]
        unrestrict = park_dict
        return unrestrict
    


class Park(User):


    def getVehicleInfo(self):
        user = str(raw_input("Enter motor type:"))
        unum = int(raw_input("Enter motor number:"))
        return user,unum
    
    def addVehicle(self, get, user, unum, data = []):
        if user in get.keys():
            size = get[user]
            if size == 0:
                print "No place for park"
            else:
                usesss = (user, unum, size)
                data.append(usesss)
                get[user] = size-1
        else:
            print "This type of vehicle not allowed."
        return get, data

    def removeVehicle(get, data):
        vehnum = int(raw_input("Enter motor number:"))
        for i in data:
            if i[1] == vehnum:
                veh = i[0]
                get[veh] +=1
                data.remove(i)
            else:
                print "No Vehicle"
        return data

if __name__ == "__main__":
    
    vehicle = Vehicle
    vehicle_dict = vehicle.park_limits()

    user = User()
    park_limit = user.park_limits()
    res_dict, vehicle = user.restrict_vehicle(park_limit)
    unres_dict = user.unrestrict_vehicle(vehicle_dict, res_dict, vehicle)

    park = Park():
