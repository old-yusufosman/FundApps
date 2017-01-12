import unittest
import TestRover


class MoveTests(unittest.TestCase):
    position = [0, 0, "N"]

    def test_move_north(self):
        result = TestRover.move_rover("F")
        expected = [0, 1, "N"]
        self.assertEqual(expected, result)

    def test_move_south(self):
        result = TestRover.move_rover("B")
        expected = [0, -1, "N"]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
