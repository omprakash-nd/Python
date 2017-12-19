park_lot_dict = {}                              ## Dict for entire park information 
vehicle_type_list = ['BIKE', 'CAR', 'VAN', 'BUS']  ## Default vehicle list
parked_vehicle = {}                               ## Dict for store vehicle parked vehicle


class Parklot():                                ## Class for user level of creating park limits


    def get_level(self):                        ## Get count of floors
        try:
            isLevel = True
            print "***Vehicle Parking System***\n" 
            floor_level = int(raw_input("Enter count of level"))
            value = int(floor_level)
            return floor_level, isLevel
        except ValueError:
            print "Input is not an int"
            exit()
        
    def get_count_vehicle(self):                ## Get count of types of vehicles
        try:
            vehile_count = int(raw_input("how many types of vehicle ?"))
            value = int(vehile_count)
            if vehile_count <= 4:
                return vehile_count
            else:
                print "count is high."
        except ValueError:
            print "Input is not an int"
            exit()

    def get_vehicle_info(self):                  ## Get user vehicle information 
        try:            
            vehicle_types, vehicle_count = str(raw_input("Enter your Vechile Type and Count:")).split("-")
            vehicle_type = vehicle_types.upper()
            if vehicle_count >= 1:
                return vehicle_type, vehicle_count
            else:
                print "vehicle count is low."
        except ValueError:
            print "Given input is not on corret format"
            exit()
            
    def park_limit(self, floor_level):                                           ## Check park limits and correct values append to respond dict
        try:
            for floor in range(floor_level):
                user_vehicle_dict = {}
                print "**%r Floor**" % (floor + 1)
                types_count = self.get_count_vehicle()                          ##calling get_count_vehicle function
                for count in range(types_count):
                    vehicle_type, vehicle_count = self.get_vehicle_info()       ##calling get_vehicle_info function
                    if vehicle_type in vehicle_type_list: 
                        user_vehicle_dict[vehicle_type] = int(vehicle_count)
                    else:
                        print "Your %r vehicle not in list" % vehicle_type
                        types_count + 1
                park_lot_dict['Floor' +str(floor + 1)] = user_vehicle_dict         ## store user entered information to park_lot_dict
        except Exception as exception:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message

            
class Vehicle():                                                                ## Class for Vehicle


    def get_vehicle_info(self):                                                 ## Get parking vehicle inforamtion                            
        isSuccess = True
        try:
            motors_type = str(raw_input("Enter motor type:"))
            motor_type = motors_type.upper()
            motor_number = int(raw_input("Enter motor number:"))
            return motor_type, motor_number, isSuccess
        except ValueError:
            isSuccess = False
            print "Given input is not on corret format"
            return motor_type, motor_number, isSuccess

    def check_vehicle_info(self, motor_type, motor_number):                 ## Check parking vehicle information
        try:
            isSuccess = True
            user_vehicle = []
            for floor, floor_values in park_lot_dict.items():
                vehicles = floor_values.keys()
                user_vehicle.append(vehicles)
            result = [motor_type in vehicle for vehicle in user_vehicle]
            if True in result:
                return motor_type, motor_number, isSuccess
            else:
                isSuccess = False
                print "Vehicle type is wrong."    
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
            return motor_type, motor_number, isSuccess
            
    def park_vehicle(self, motor_type, motor_number):                                     ## Parking Vehicle
        try:
            isSuccess = True
            for level, level_space in park_lot_dict.items():          
                if motor_type in level_space.keys():
                    space = level_space[motor_type]
                    if space >= 1:
                        assign = [level, motor_type]
                        parked_vehicle[motor_number] = assign                            ## Assign park slot
                        level_space[motor_type] = space-1
                        print "Your %r number:%r park place:%r \n" % (motor_type, motor_number, level)
                        break
                else:
                    isSuccess = False
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
        return parked_vehicle, isSuccess

    def get_unpark_vehicle(self, parked_vehicle):                                       ## Get info for exit from park
        try:
            isSuccess = True
            vehicle_number = int(raw_input("Enter motor number:"))                      ## Parked vehicle number
            if vehicle_number in parked_vehicle.keys():
                motor_number = vehicle_number
                return motor_number, isSuccess
            else:
                print "This vehicle not in parking lot."
        except Exception as exception:
            isSuccess = False
            motor_number = None
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            return motor_number, isSuccess

    def unpark_vehicle(self, motor_number):                                           ## Function for exit from park place     
        try:
            isSuccess = True
            if motor_number in parked_vehicle.keys():
                park_lot_dict[parked_vehicle[motor_number][0]][parked_vehicle[motor_number][1]] = park_lot_dict[parked_vehicle[motor_number][0]][parked_vehicle[motor_number][1]] + 1
                del parked_vehicle[motor_number]
                print "Thanks for parking:) \n"
            else:
                print "This vehicle not in parking lot."
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return isSuccess

    def view_slots(self):
       for vehicle_number, parked_place in parked_vehicle.items():
           print """%r  %r  %r""" % (parked_place[0], vehicle_number, parked_place[1]) 
           
        

if __name__ == "__main__":
    park = Parklot()                                                    ## creation of object for parklot class
    wrong_choice = "You Entered wrong key."
    error_msg = "Your process have an error."
    isSuccess = True
    if isSuccess: 
        level, successResult = park.get_level()
        if successResult:
            park.park_limit(level)
        else:
            print error_msg
    else:
        print error_msg
    
    success = True
    while success:        
        choice = int(raw_input("""1-Park\n""" +
                            """2-Un park\n""" +
                            """3-View Slot\n""" +
                            """4-Exit\n""" +
                            """Enter your choice:"""))
        vehicle = Vehicle()                                             ## creation of object for Vehicle class
        if choice == 1:
            vehicle_type, vehicle_number, is_vehicle_info = vehicle.get_vehicle_info()
            if is_vehicle_info:
                checked_type, checked_number, is_checked = vehicle.check_vehicle_info(vehicle_type, vehicle_number)
            else:
                print error_msg
            if is_checked:
                parked_info, is_success = vehicle.park_vehicle(checked_type, checked_number)
            else:
                print error_msg
                break
        elif choice == 2:
            parked_vehicle_number, isunpark_vehicle = vehicle.get_unpark_vehicle(parked_info)
            if isunpark_vehicle:
                is_success = vehicle.unpark_vehicle(parked_vehicle_number)
            else:
                print error_msg
                break
        elif choice == 3:
            if success:
                vehicle.view_slot()
            else:
                print error_msg
        elif choice == 4:
            success = False
            exit()
            break



        
##***Vehicle Parking System***
##Enter count of level2
##**1 Floor**
##how many types of vehicle ?3
##Enter your Vechile Type and Count:car-3
##Enter your Vechile Type and Count:van-5
##Enter your Vechile Type and Count:bus-2
##**2 Floor**
##how many types of vehicle ?1
##Enter your Vechile Type and Count:bike-10
##1-Park
##2-Un park
##3-View Slot
##4-Exit
##Enter your choice:1
##Enter motor type:van
##Enter motor number:1234
##Your 'VAN' number:1234 park place:'Floor1' 
##
##1-Park
##2-Un park
##3-View Slot
##4-Exit
##Enter your choice:1
##Enter motor type:bike
##Enter motor number:1111
##Your 'BIKE' number:1111 park place:'Floor2' 
##
##1-Park
##2-Un park
##3-View Slot
##4-Exit
##Enter your choice:3
##{1234: ['Floor1', 'VAN'], 1111: ['Floor2', 'BIKE']}
##1-Park
##2-Un park
##3-View Slot
##4-Exit
##Enter your choice:1
##Enter motor type:van
##Enter motor number:1112
##Your 'VAN' number:1112 park place:'Floor1' 
##
##1-Park
##2-Un park
##3-View Slot
##4-Exit
##Enter your choice:2
##Enter motor number:1234
##Thanks for parking:) 
