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
        expected = [Rover.grid_size - 1, 0, "W"]
        self.assertEqual(expected, result)

    def test_wrap_bottom(self):
        result = self.Rover.move_rover("B")
        expected = [0, Rover.grid_size - 1, "N"]
        self.assertEqual(expected, result)

    def test_move_square(self):
        result = self.Rover.move_rover("FRFRFRF")
        expected = [0, 0, "W"]
        self.assertEqual(expected, result)

    def test_move_from_instructions(self):
        result = self.Rover.move_rover("FFRFF")
        expected = [2, 2, "E"]
        self.assertEqual(expected, result)

    def test_move_square_wrap(self):
        result = self.Rover.move_rover("LFRFRFRF")
        expected = [0, 0, "S"]
        self.assertEqual(expected, result)

    def test_wrap_down_left(self):
        result = self.Rover.move_rover("BLF")
        expected = [Rover.grid_size - 1, Rover.grid_size - 1, "W"]
        self.assertEqual(expected, result)

    def test_collision(self):
        result = self.Rover.move_rover("FFFFRF")
        expected = [0, 4, "E"]
        self.assertEqual(expected, result)

    def test_wrap_collision(self):
        result = self.Rover.move_rover("BLFF")
        expected = [Rover.grid_size - 1, Rover.grid_size - 1, "W"]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
