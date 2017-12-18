park_lot_dict = {}                              ## Dict for entire park information 
vehicle_type_list = ['BIKE','CAR','VAN','BUS']  ## Default vehicle list
parked_vehicle = {}                               ## Dict for store vehicle parked vehicle


class Parklot():                                ## Class for user level of creating park limits


    def get_level(self):                        ## Get count of floors
    
        floor_level = int(raw_input("Enter count of level"))
        if isinstance(floor_level, int):
            return floor_level
        else:
            print "Level will be integer"

    def get_count_vehicle(self):                ## Get count of types of vehicles

        vehile_count = int(raw_input("how many types of vehicle ?"))
        if vehile_count <= 4:
            return vehile_count
        else:
            print "count is high."

    def get_vehicle_info(self):                  ## Get user vehicle information 

        vehicle_types, vehicle_count = str(raw_input("Enter your Vechile Type and Count:")).split("-")
        vehicle_type = vehicle_types.upper()
        if vehicle_count >= 1:
            return vehicle_type, vehicle_count
        else:
            print "Count is not correct"

    def park_limit(self, floor_level):          ## Check park limits and correct values append to respond dict
        
        for floor in range(floor_level):
            user_vehicle_dict = {}
            print "**%r Floor**" % (floor +1)
            types_count = self.get_count_vehicle()
            
            for count in range(types_count):
                vehicle_type, vehicle_count = self.get_vehicle_info()
                if vehicle_type in vehicle_type_list: 
                    user_vehicle_dict[vehicle_type] = int(vehicle_count)
                else:
                    print "Your %r vehicle not in list" % vehicle_type
                    types_count +1
            park_lot_dict['Floor'+str(floor +1)]= user_vehicle_dict    ## store user entered information to park_lot_dict


class Vehicle():                                                    ## Class Vehicle


    def get_vehicle_info(self):                                     ## Get parking vehicle inforamtion                            
        isSuccess = True
        try:
            motors_type = str(raw_input("Enter motor type:"))
            motors_type = motors_type.upper()
            motors_number = int(raw_input("Enter motor number:"))
            if motors_type in vehicle_type_list:
               motor_type = motors_type
               motor_number = motors_number
               return motor_type, motor_number, isSuccess
            else:
                print "Vehicle type is wrong."
                isSuccess = False
                self.get_vehicle_info()
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
            return isSuccess
            
    def park_vehicle(self, motor_type, motor_number):           ## Parking Vehicle
        try:
            isSuccess = True
            for level, level_space in park_lot_dict.items():          
                if motor_type in level_space.keys():
                    print "Before Park", park_lot_dict
                    space = level_space[motor_type]
                    if space >= 1:
                        assign = [level, motor_type]
                        parked_vehicle[motor_number] = assign   ## Assign park slot
                        level_space[motor_type] = space-1
                        print "Your %r number:%r park place:%r \n" % (motor_type, motor_number, level)
                        break
                    else:
                        print "No place for park"
                else:
                    isSuccess = False
            print "After Parking", park_lot_dict
        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return parked_vehicle, isSuccess

    def get_unpark_vehicle(self, parked_vehicle):               ## Get info for exit from park
        try:
            isSuccess = True
            vehicle_number = int(raw_input("Enter motor number:")) ## Parked vehicle number
            if vehicle_number in parked_vehicle.keys():
                motor_number = vehicle_number
                return motor_number, isSuccess
            else:
                print "This vehicle not in parking lot."

        except Exception as exception:
            isSuccess = False
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
            return isSuccess

    def unpark_vehicle(self, motor_number):                    ## Function for exit from park place     
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

if __name__ == "__main__":
    park = Parklot()
    level = park.get_level()
    park.park_limit(level)

    wrong_choice = "You Entered wrong key."
    error_msg = "Your process have an error."
    success =  True
    while success:        
        choice = int(raw_input("""1-Park\n""" +
                            """2-Un park\n""" +
                            """3-Exit\n""" +
                            """Enter your choice:"""))
        vehicle = Vehicle()
        if choice == 1:
            vehicle_type, vehicle_number, is_vehicle_info = vehicle.get_vehicle_info()
            if is_vehicle_info:
                parked_info, is_success = vehicle.park_vehicle(vehicle_type, vehicle_number)
            else:
                print error_msg
                break
        elif choice == 2:
            parked_vehicle_number, isunpark_vehicle = vehicle.get_unpark_vehicle(parked_info)
            if isunpark_vehicle:
                is_success  = vehicle.unpark_vehicle(parked_vehicle_number)
            else:
                print error_msg
                break
        elif choice == 3:
            success = False
            exit()


##Output
##
##
##Enter count of level2
##**1 Floor**
##how many types of vehicle ?1
##Enter your Vechile Type and Count:van-1
##**2 Floor**
##how many types of vehicle ?1
##Enter your Vechile Type and Count:car-1
##1-Park
##2-Un park
##3-Exit
##Enter your choice:1
##Enter motor type:car
##Enter motor number:1234
##{'Floor1': {'VAN': 1}, 'Floor2': {'CAR': 1}}
##['Floor2', 'CAR']
##1
##Your 'CAR' number:1234 park place:'Floor2' 
##
##{'Floor1': {'VAN': 1}, 'Floor2': {'CAR': 0}}
##1-Park
##2-Un park
##3-Exit
##Enter your choice:2
##Enter motor number:1234
##Thanks for parking:) 
##
            
