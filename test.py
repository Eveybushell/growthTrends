from trends import squareTrends
import unittest

class TestSquares(unittest.TestCase):
    
    def testStandard1 (self):
        self.assertEqual(squareTrends([1,2,3,4,5]),[1,4,9,16,25])
    
    def testStandard2 (self):
        self.assertEqual(squareTrends([-1,-2,-3,-4,-5]),[1,4,9,16,25])
    
    def testStandard3 (self):
        self.assertEqual(squareTrends([1,-2,3,-4,5]),[1,4,9,16,25])
    
    def testEdge1 (self):
        self.assertEqual(squareTrends([]),[])
    
    def testEdge2 (self):
        self.assertEqual(squareTrends(['rabbits', 'dogs', 'cats', 'fish', 'turtles']),"growthPercentages must be an array of ints.")

    def testEdge3 (self):
        self.assertEqual(squareTrends('pets'),"growthPercentages must be an array of ints.")

if __name__ == "__main__":
    unittest.main()