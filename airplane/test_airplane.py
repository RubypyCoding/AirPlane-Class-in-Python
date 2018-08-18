import unittest
from airplane import *


class AirPlaneTests(unittest.TestCase):

	def setUp(self):
		self.func = AirPlane("Comercial","Boeing")

	def test_type_is_evaluated_as_getter(self):
	    self.assertEqual(self.func.type, "Comercial")

	def test_type_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.func.type = "Militar"

	def test_model_is_evaluated_as_getter(self):
	    self.assertEqual(self.func.model, "Boeing")

	def test_model_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.func.model = "MiG-31"

	def test_speed_up_returns_message_airplane_has_accelerated_20_kph(self):
		self.assertEqual(self.func.speed_up(20), "Airplane has accelerated 20 kph.")

	def test_brake_returns_message_airplane_has_decelerated_20_kph(self):
		self.assertEqual(self.func.brake(20), "Airplane has decelerated 20 kph.")

	def test_shut_down_returns_message_lets_shut_down_to_0(self):
		self.assertEqual(self.func.shut_down(), "Let's shut down to 0!")

	def test_current_speed_returns_message_airplane_goes_40_kph_when_speed_up_increases_40(self):
		self.func.speed_up(40)
		self.assertEqual(self.func.current_speed(), "Airplane goes 40 kph.")

	def test_current_speed_returns_message_airplane_goes_60_kph_when_speed_up_increases_40_and_20(self):
		self.func.speed_up(40)
		self.func.speed_up(20)
		self.assertEqual(self.func.current_speed(), "Airplane goes 60 kph.")

	def test_current_speed_returns_message_airplane_goes_20_kph_when_brake_decreases_10(self):
		self.func.speed_up(30)
		self.func.brake(10)
		self.assertEqual(self.func.current_speed(), "Airplane goes 20 kph.")


if __name__=="__main__":
    unittest.main()