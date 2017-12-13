def defaultVehicle():
    get = {
        "BIKE":30,
        "BUS":1,
        "CAR":20,
        "VAN":15,
        }
    return get

def addVehicle(get,data = []):
    for i in range(3):
        user = str(raw_input("Enter motor:"))
        unum = int(raw_input("Enter motor number:"))
        if user in get.keys():
            size = get[user]
            if size == 0:
                print "No place for park"
            else:
                usesss = (user, unum, size)
                data.append(usesss)
                get[user] = size-1
    print get
    return get, data

def removeVehicle(get, data):
    print "sss"

def removeVehicle():
    lsveh = [('VAN', 234, 15), ('CAR', 233, 20), ('BIKE', 235, 30)]
    vehnum = int(raw_input("Enter motor number:"))
    ss = filter(lsveh, lambda x: x[1] == vehnum)
    ##ss = [item for item in lsveh if vehnum in item]
    print ss
##    for i in range(len(lsveh)):
##        if vehnum in lsveh[i][1]:    
##            print "yes"
##        else:
##            print "NO"

removeVehicle()            
        
##
##        
##arg1 = defaultVehicle()
##arg2, arg3 = addVehicle(arg1)
##removeVehicle(arg2, arg3)


