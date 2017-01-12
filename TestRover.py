import unittest
import Rover


class MoveTests(unittest.TestCase):
    def setUp(self):
        self.Rover = Rover.Rover()

    def test_move_north(self):
        result = self.Rover.move_rover("F")
        expected = [0, 1, "N"]
        self.assertEqual(expected, result)

    def test_move_south(self):
        self.Rover.position = [0, 1, "N"]
        result = self.Rover.move_rover("B")
        expected = [0, 0, "N"]
        self.assertEqual(expected, result)

    def test_move_left(self):
        result = self.Rover.move_rover("L")
        expected = [0, 0, "W"]
        self.assertEqual(expected, result)

    def test_move_right(self):
        result = self.Rover.move_rover("R")
        expected = [0, 0, "E"]
        self.assertEqual(expected, result)

    def test_wrap_left(self):
        self.Rover.position = [0, 0, "W"]
        result = self.Rover.move_rover("F")
        expected = [9, 0, "W"]
        self.assertEqual(expected, result)

    def test_wrap_bottom(self):
        result = self.Rover.move_rover("B")
        expected = [0, 9, "N"]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
