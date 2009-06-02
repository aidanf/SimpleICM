import unittest
from types import ModuleType


def IsTestCase(test):
    if type(test) == type and issubclass(test, unittest.TestCase):
        return True
    return False
    
def AddTests(suite, test):
    if isinstance(test, ModuleType):
        for entry in test.__dict__.values():
            if IsTestCase(entry):
                suite.addTests(unittest.makeSuite(entry))
    elif IsTestCase(test):
        suite.addTests(unittest.makeSuite(test))

def MakeSuite(*tests):
    suite = unittest.TestSuite()
    for test in tests:
        AddTests(suite, test)
    return suite

def RunTests(suite, **keywargs):
    return unittest.TextTestRunner(**keywargs).run(suite)
