import unittest
from app.classes.range.range import Range, DistanceUnit, DistanceType

class TestRangeTouchAndX(unittest.TestCase):
    def testEqualTouchAndTouch(self):
        r1 = Range(None, None, DistanceType.TOUCH)
        r2 = Range(None, None, DistanceType.TOUCH)
        self.assertEqual(r1, r2)
    
    def testEqualTouchAndFeet(self):
        r1 = Range(None, None, DistanceType.TOUCH)
        r2 = Range(0, DistanceUnit.FEET, DistanceType.RANGED)
        self.assertEqual(r1, r2)
    
    def testEqualTouchAndMiles(self):
        r1 = Range(None, None, DistanceType.TOUCH)
        r2 = Range(0, DistanceUnit.MILES, DistanceType.RANGED)
        self.assertEqual(r1, r2)
    
    def testNotEqualTouchAndFeet(self):
        r1 = Range(None, None, DistanceType.TOUCH)
        r2 = Range(1, DistanceUnit.FEET, DistanceType.RANGED)
        self.assertNotEqual(r1, r2)
    
    def testNotEqualTouchAndMiles(self):
        r1 = Range(None, None, DistanceType.TOUCH)
        r2 = Range(1, DistanceUnit.MILES, DistanceType.RANGED)
        self.assertNotEqual(r1, r2)
        
class TestRangeFeetAndX(unittest.TestCase):
    def testEqualFeetAndFeet(self):
        r1 = Range(1, DistanceUnit.FEET, DistanceType.RANGED)
        r2 = Range(1, DistanceUnit.FEET, DistanceType.RANGED)
        self.assertEqual(r1, r2)
    
    def testEqualFeetAndMiles(self):
        r1 = Range(1, DistanceUnit.FEET, DistanceType.RANGED)
        r2 = Range(1, DistanceUnit.MILES, DistanceType.RANGED)
        self.assertNotEqual(r1, r2)
    
    def testNotEqualFeetAndFeet(self):
        r1 = Range(1, DistanceUnit.FEET, DistanceType.RANGED)
        r2 = Range(2, DistanceUnit.FEET, DistanceType.RANGED)
        self.assertNotEqual(r1, r2)
    
    def testNotEqualFeetAndMiles(self):
        r1 = Range(1, DistanceUnit.FEET, DistanceType.RANGED)
        r2 = Range(1, DistanceUnit.MILES, DistanceType.RANGED)
        self.assertNotEqual(r1, r2)

class TestRangeSelfAndX(unittest.TestCase):
    def testEqualSelfAndSelf(self):
        r1 = Range(None, None, DistanceType.SELF)
        r2 = Range(None, None, DistanceType.SELF)
        self.assertEqual(r1, r2)
    
    def testNotEqualSelfAndFeet(self):
        r1 = Range(None, None, DistanceType.SELF)
        r2 = Range(0, DistanceUnit.FEET, DistanceType.RANGED)
        self.assertEqual(r1, r2)
    
    def testNotEqualSelfAndMiles(self):
        r1 = Range(None, None, DistanceType.SELF)
        r2 = Range(0, DistanceUnit.MILES, DistanceType.RANGED)
        self.assertNotEqual(r1, r2)
    
    def testNotEqualSelfAndFeet(self):
        r1 = Range(None, None, DistanceType.SELF)
        r2 = Range(1, DistanceUnit.FEET, DistanceType.RANGED)
        self.assertNotEqual(r1, r2)
    
    def testNotEqualSelfAndMiles(self):
        r1 = Range(None, None, DistanceType.SELF)
        r2 = Range(1, DistanceUnit.MILES, DistanceType.RANGED)
        self.assertNotEqual(r1, r2)
    
class TestRangeSelfConstructor(unittest.TestCase):
    def testSelfCorrectConstructor(self):
        r = Range(None, None, DistanceType.SELF)
        self.assertIsInstance(r, Range)
        
    def testSelfIncorrectDistance(self):
        with self.assertRaises(ValueError):
            Range(1, None, DistanceType.SELF)
    
    def testSelfIncorrectDistanceUnit(self):
        with self.assertRaises(ValueError):
            Range(None, DistanceUnit.FEET, DistanceType.SELF)

class TestRangeTouchConstructor(unittest.TestCase):
    def testTouchCorrectConstructor(self):
        r = Range(None, None, DistanceType.TOUCH)
        self.assertIsInstance(r, Range)
        
    def testTouchIncorrectDistance(self):
        with self.assertRaises(ValueError):
            Range(1, None, DistanceType.TOUCH)
    
    def testTouchIncorrectDistanceUnit(self):
        with self.assertRaises(ValueError):
            Range(None, DistanceUnit.FEET, DistanceType.TOUCH)