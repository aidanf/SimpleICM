import loadassemblies

import sys
from tests.testutils import MakeSuite, RunTests

from tests import (
    icmtest,
)

suite = MakeSuite(icmtest)

results = RunTests(suite, verbosity=2)

if results.failures or results.errors:
    sys.exit(1)
