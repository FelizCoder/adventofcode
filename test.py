import unittest
from typing import Callable
from aoc01 import aoc01
from aoc02 import aoc02
from aoc03 import aoc03
from aoc04 import aoc04
from aoc05 import aoc05
from aoc06 import aoc06
from aoc08 import aoc08

class TestAoc(unittest.TestCase):
    def run_test(self, day: int, expected: int, test_func: Callable[[str], int]):
        """Generic test constructor for AoC Puzzles

        Args:
            day (int): day of the puzzle
            expected (int): expected solution
            test_func (Callable[[str], int]): function under test
        """        
        filepath = f"{day:02d}/test.txt"  # Assuming your file structure is like "01/test.txt"
        result = test_func(filepath)
        self.assertEqual(
            result, 
            expected, 
            f"Incorrect result for day {day:02d},\n got {result} but expected {expected}"
        )
    
    def test_aoc01(self):
        self.run_test(1,281,aoc01)
        
    def test_aoc02(self):
        self.run_test(2,2286,aoc02)
        
    def test_aoc03(self):
        self.run_test(3,467835, aoc03)
        
    def test_aoc04(self):
        self.run_test(4,30,aoc04)
        
    def test_aoc05(self):
        self.run_test(5,46,aoc05)
    
    def test_aoc06(self):
            self.run_test(6,71503,aoc06)
            
    def test_aoc08(self):
        self.run_test(8,6,aoc08)

if __name__ == '__main__':
    unittest.main()
