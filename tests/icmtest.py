import unittest
from tests.testcase import TestCase

from icm import ICM

class ICMTest(TestCase):
	
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    def testCorrectICMValues1(self):
        icm = ICM([1000, 1000, 1000, 1000, 1000, 1000], [0.5, .3, 0.2])
        equities = icm.equities
        self.assertEquals(6, len(equities), 
	                          "Equity array is the wrong length")
        
        for eq in equities:
            self.assertEquals(0.1667, eq) 
	
    def testCorrectICMValues2(self):
        icm = ICM([8000, 2000, 3000, 500], [0.5, .3, 0.2])
        equities = icm.equities
        self.assertEquals(4, len(equities), 
	                          "Equity array is the wrong length")
        self.assertEquals(0.4049, equities[0]) 
        self.assertEquals(0.2388, equities[1]) 
        self.assertEquals(0.2867, equities[2]) 
        self.assertEquals(0.0695, equities[3]) 
        