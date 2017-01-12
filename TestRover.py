import unittest
import Rover


class MoveTests(unittest.TestCase):
    position = [0, 0, "N"]

    def test_move_north(self):
        result = Rover.move_rover("F")
        expected = [0, 1, "N"]
        self.assertEqual(expected, result)

    def test_move_south(self):
        result = Rover.move_rover("B")
        expected = [0, -1, "N"]
        self.assertEqual(expected, result)

    def test_move_left(self):
        result = Rover.move_rover("L")
        expected = [0, 0, "W"]
        self.assertEqual(expected, result)

    def test_move_right(self):
        result = Rover.move_rover("R")
        expected = [0, 0, "E"]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
