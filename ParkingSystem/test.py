import unittest
from Floor import Floor
from Vehicle import Vehicle
from ParkController import ParkingController

class TestParkApplication(unittest.TestCase):

    def test_floor(self):
        self.test_floor = Floor("floor2")
        self.assertEqual((self.test_floor.floor_no), "floor1")
   
    def test_park(self):
        self.test_floor = Floor("floor1")
        self.test_floor.set_slot("Car", 1)
        self.test_vehicle = Vehicles("Car", 1234)
        self.assertEqual(self.test_floor.park(self.test_vehicle), 1234)

    def test_unpark(self):
        self.test_floor = Floor("floor1")
        self.test_floor.set_slot("Car", 1)
        self.test_vehicle = Vehicles("Car", 1234)
        self.assertEqual(self.test_floor.park(self.test_vehicle), 1234)

    def test_unpark(self):
        self.test_floor = Floor("floor1")
        self.test_floor.set_slot("Car", 1)
        self.test_vehicle = Vehicles("Car", 3555)   
        self.assertEqual(self.test_floor.park(self.test_vehicle), 1234)
        
    def test_check_available_space(self):
        self.test_floor = Floor("floor1")
        self.test_floor.set_slot("Car", 1)
        self.test_vehicle = Vehicles("Car", 1234)
        self.test_parking_controller = ParkingController()
        self.test_parking_controller.__add__(self.test_floor)
        self.assertEqual(self.test_parking_controller.check_space(self.test_vehicle)[1], "Space Available")

    def test_check_filled_space(self):
        self.test_floor = Floor("floor1")
        self.test_floor.set_slot("Car", 0)
        self.test_vehicle = Vehicles("Car", 1234)
        self.test_parking_controller = ParkingController()
        self.test_parking_controller.__add__(self.test_floor)
        self.assertEqual(self.test_parking_controller.check_space(self.test_vehicle)[1], "No free space")

    def test_check_vehicle(self):
        self.test_floor = Floor("floor1")
        self.test_floor.set_slot("Car", 1)
        self.test_vehicle = Vehicles("Van", 1234)
        self.test_parking_controller = ParkingController()
        self.test_parking_controller.__add__(self.test_floor)
        self.assertEqual(self.test_parking_controller.check_vehicle(self.test_vehicle)[1], "No vehicle")

         
if __name__ == '__main__':
    unittest.main()

