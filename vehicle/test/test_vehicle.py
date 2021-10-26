import unittest
from vehicle.project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_inputs(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_is_fuel_capacity_unchanged(self):
        self.assertEqual(50, self.vehicle.capacity)
        self.vehicle.fuel = 20
        self.assertEqual(50, self.vehicle.capacity)

    def test_drive_is_fuel_equal(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_drive_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(49)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_vehicle_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_is_refuel_success(self):
        self.vehicle.fuel = 20
        self.vehicle.refuel(30)
        self.assertEqual(self.vehicle.fuel, 50)

    def test_string_representation(self):
        self.assertEqual("The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption", f"The vehicle has {self.vehicle.horse_power} horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption")


if __name__ == "__main__":
    unittest.main()
