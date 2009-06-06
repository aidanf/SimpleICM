import clr

print "Compiling modules"
clr.CompileModules('simpleicm.dll', mainModule = 'main.py', 'view.py', 'model.py', 'controller.py', 'utils.py', 'string.py', 'decimal.py', 'copy.py', 'types.py')

clr.AddReference('simpleicm.dll')

import model
import utils
import controller
import view
import main

print "Hello"