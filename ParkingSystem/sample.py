glob = []

glist = ['BIKE','CAR','VAN','BUS']

def parkLimit():

    level = int(raw_input("enter level"))
    ls = []      
    for count_level in range(level):
        print "enter %r floor data" % count_level
        vehile = input("how many types of vehicle data you enter ")      
        for veh in range(vehile):
            types, count = str(raw_input("Enter your Vechile Type and Count:")).split("-")
            if types in glist: 
                samp = (types, count)
                ls.append(samp)
    
        samp = dict(ls)
        glob.append(samp)
        print glob
parkLimit()


def menu():
    print("Vehicle Parking System\n")
    menu_opition = int(input(""" 0-Restrict\n """ +
                              """1-Non Restrict\n"""))
    if menu_opition == 0:
        user = User()
        
    elif menu_opition == 1:
        park = Park()
        
    else:
        print "You have pressed the wrong key, please try again"
        menu()

def park_limits():
    
    park_dict = {
            "BIKE":30,
            "BUS":5,
            "CAR":20,
            "VAN":15,
            }
    return park_dict


class User():

    def restrict_vehicle(self, park_dict):
        
        temp_restrict = park_dict
        rest_vehicle = str(raw_input("which vehicle type you restrict:"))

        if rest_vehicle in temp_restrict.keys():
            temp_restrict[rest_vehicle] = None
            
            glop.append(temp_restrict)
            print temp_restrict
        else:
            print "This type of vehicle not in your list"
            restrict_vehicle(temp_restrict)

        return temp_restrict
    

    def unrestrict_vehicle(self, park_dict, temp_restrict, rest_vehicle):
        unrest_vehicle = str(raw_input("which vehicle type you unrestrict:"))

        if temp_restrict[unrest_vehicle] == None: 
            temp_restrict[unrest_vehicle] = park_dict[unrest_vehicle]
            glop.append(temp_restrict)
        else:
            print "This type of vehicle you cant unrestrict."
            menu()
            
        return temp_restrict

    
    
class Park(User):


    def get_vehicle_info(self):
        veh_type = str(raw_input("Enter motor type:"))
        veh_number = int(raw_input("Enter motor number:"))

        return veh_type, veh_number
    
    def park_vehicle(self, get, veh_type, veh_number, data = []):
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

    def unpark_vehicle(get, data):
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
    
    vehicle_dict = park_limits()

        restrict_option = int(input("""1- Restrict Vechicle"""))
        user = User()
        res_dict, vehicle = user.restrict_vehicle(vehicle_dict)
            
        park_opition = int(input("""
1-Park
2-Un Park
3-Back"""))
        if park_opition == 1:
            park = Park()
            v_type, v_number = park.get_vehicle_info()
            park_vehicle(v_type, v_number)
        if park_opition == 2:
            unpark_vehicle( )

    else:
        exit()
        
menu() 
