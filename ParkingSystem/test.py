import unittest
from Park import Floor, Vehicles, ParkingController

class TestParkApplication(unittest.TestCase):


    def setUp(self):
        self.test_floor = Floor("floor1")
        self.test_floor.set_slot("Car", 1)
        self.test_floor.set_slot("Van", 0)
        self.test_floor.set_slot("Bus", 1)
        self.test_vehicle = Vehicles("Car", 1234)
        self.test_wrong_vehicle = Vehicles("Van", 8343)
        self.test_parking_controller = ParkingController()
        self.test_parking_controller.__add__(self.test_floor)

    def test_park(self):
        self.assertEqual(self.test_floor.park(self.test_vehicle), 1234)

    def test_unpark(self):
        self.assertEqual(self.test_floor.park(self.test_vehicle), 1234)

    def test_check_available_space(self):
        self.assertEqual(self.test_parking_controller.check_space(self.test_vehicle)[1], "Parked")

    def test_check_filled_space(self):
        self.assertEqual(self.test_parking_controller.check_space(self.test_wrong_vehicle)[1], "No free space")

    def test_check_vehicle(self):
        self.assertEqual(self.test_parking_controller.check_vehicle(self.test_vehicle)[1], "No vehicle")
         
    
if __name__ == '__main__':
    unittest.main()

