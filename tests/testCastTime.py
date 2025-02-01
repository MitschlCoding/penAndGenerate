import unittest
from app.classes.time.time import Time, TimeUnit

class TestTimeInstandAndX(unittest.TestCase):
    def testEqualInstantAndInstant(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(None, TimeUnit.INSTANTANEOUS)
        self.assertEqual(c1, c2)
    
    def testEqualInstantAndZeroSecond(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(0, TimeUnit.SECONDS)
        self.assertEqual(c1, c2)

    def testEqualInstantAndZeroRound(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(0, TimeUnit.ROUND)
        self.assertEqual(c1, c2)

    def testEqualInstantAndZeroMinute(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(0, TimeUnit.MINUTES)
        self.assertEqual(c1, c2)
    
    def testEqualInstantAndZeroHour(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(0, TimeUnit.HOURS)
        self.assertEqual(c1, c2)

    def testNotEqualInsantAndSecond(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(1, TimeUnit.SECONDS)
        self.assertNotEqual(c1, c2)
    
    def testNotEqualInsantAndRound(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(1, TimeUnit.ROUND)
        self.assertNotEqual(c1, c2)

    def testNotEqualInsantAndMinute(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(1, TimeUnit.MINUTES)
        self.assertNotEqual(c1, c2)
    
    def testNotEqualInsantAndHour(self):
        c1 = Time(None, TimeUnit.INSTANTANEOUS)
        c2 = Time(1, TimeUnit.HOURS)
        self.assertNotEqual(c1, c2)
    
class TestTimeSecondsAndX(unittest.TestCase):
    def testEqualSecondsAndSeconds(self):
        c1 = Time(1, TimeUnit.SECONDS)
        c2 = Time(1, TimeUnit.SECONDS)
        self.assertEqual(c1, c2)
    
    def testEqualSecondsAndRounds(self):
        c1 = Time(6, TimeUnit.SECONDS)
        c2 = Time(1, TimeUnit.ROUND)
        self.assertEqual(c1, c2)
        
    def testEqualSecondsAndMinutes(self):
        c1 = Time(60, TimeUnit.SECONDS)
        c2 = Time(1, TimeUnit.MINUTES)
        self.assertEqual(c1, c2)

    def testEqualSecondsAndHours(self):
        c1 = Time(3600, TimeUnit.SECONDS)
        c2 = Time(1, TimeUnit.HOURS)
        self.assertEqual(c1, c2)

    def testNotEqualSecondsAndSeconds(self):
        c1 = Time(1, TimeUnit.SECONDS)
        c2 = Time(2, TimeUnit.SECONDS)
        self.assertNotEqual(c1, c2)

    def testNotEqualSecondsAndRound(self):
        c1 = Time(1, TimeUnit.SECONDS)
        c2 = Time(1, TimeUnit.ROUND)
        self.assertNotEqual(c1, c2)
        
    def testNotEqualSecondsAndMinutes(self):
        c1 = Time(1, TimeUnit.SECONDS)
        c2 = Time(1, TimeUnit.MINUTES)
        self.assertNotEqual(c1, c2)
        
    def testNotEqualSecondsAndHours(self):
        c1 = Time(1, TimeUnit.SECONDS)
        c2 = Time(1, TimeUnit.HOURS)
        self.assertNotEqual(c1, c2)

class TestTimeRoundAndX(unittest.TestCase):
    def testEqualRoundAndRound(self):
        c1 = Time(1, TimeUnit.ROUND)
        c2 = Time(1, TimeUnit.ROUND)
        self.assertEqual(c1, c2)
        
    def testEqualRoundAndMinutes(self):
        c1 = Time(10, TimeUnit.ROUND)
        c2 = Time(1, TimeUnit.MINUTES)
        self.assertEqual(c1, c2)
    
    def testEqualRoundAndHours(self):
        c1 = Time(600, TimeUnit.ROUND)
        c2 = Time(1, TimeUnit.HOURS)
        self.assertEqual(c1, c2)
    
    def testNotEqualRoundAndRound(self):
        c1 = Time(1, TimeUnit.ROUND)
        c2 = Time(2, TimeUnit.ROUND)
        self.assertNotEqual(c1, c2)
    
    def testNotEqualRoundAndMinutes(self):
        c1 = Time(1, TimeUnit.ROUND)
        c2 = Time(1, TimeUnit.MINUTES)
        self.assertNotEqual(c1, c2)
    
    def testNotEqualRoundAndHours(self):
        c1 = Time(1, TimeUnit.ROUND)
        c2 = Time(1, TimeUnit.HOURS)
        self.assertNotEqual(c1, c2)
    
class TestTimeMinutesAndX(unittest.TestCase):
    def testEqualMinuteAndMinute(self):
        c1 = Time(1, TimeUnit.MINUTES)
        c2 = Time(1, TimeUnit.MINUTES)
        self.assertEqual(c1, c2)
    
    def testEqualMinuteAndHour(self):
        c1 = Time(60, TimeUnit.MINUTES)
        c2 = Time(1, TimeUnit.HOURS)
        self.assertEqual(c1, c2)
    
    def testNotEqualMinuteAndMinute(self):
        c1 = Time(1, TimeUnit.MINUTES)
        c2 = Time(2, TimeUnit.MINUTES)
        self.assertNotEqual(c1, c2)
    
    def testNotEqualMinuteAndHour(self):
        c1 = Time(1, TimeUnit.MINUTES)
        c2 = Time(1, TimeUnit.HOURS)
        self.assertNotEqual(c1, c2)
    
class TestTimeHoursAndX(unittest.TestCase):
    def testEqualHourAndHour(self):
        c1 = Time(1, TimeUnit.HOURS)
        c2 = Time(1, TimeUnit.HOURS)
        self.assertEqual(c1, c2)
        
    def testNotEqualHourAndHour(self):
        c1 = Time(1, TimeUnit.HOURS)
        c2 = Time(2, TimeUnit.HOURS)
        self.assertNotEqual(c1, c2)

class TestTimeConstructor(unittest.TestCase):
    def testInstantaneousConstructor(self):
        c = Time(None, TimeUnit.INSTANTANEOUS)
        self.assertIsInstance(c, Time)
        
    def testInstantaneousConstructorIncorrectTime(self):
        with self.assertRaises(ValueError):
            Time(1, TimeUnit.INSTANTANEOUS)
            