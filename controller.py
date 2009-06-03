import clr
clr.AddReference('System.Windows.Forms') 
clr.AddReference('System.Drawing')
#clr.AddReference('System.ComponentModel')


import System
from System.Windows.Forms import *
from System.IO import File, Path
from model import ICM

from decimal import *
D = Decimal

class SimpleICMController:
    def __init__(self, view):
        self.view = view
        self._model = None
        
    def handle_go(self, sender, event):
        self.view.statusLabel.Text = "Status: Calculating"
        self.view.Refresh()
        stacks = [D(stack.Text) for stack in self.view.stacks]
        payouts = [D(payout.Text) for payout in self.view.payouts if D(payout.Text) > D(0)]
        print stacks
        print payouts
        self._model = ICM(stacks, payouts)
        equities = self._model.equities
        print equities
        
        for i in range(len(equities)):
            self.view.equities[i].Text = str(equities[i])
        self.view.statusLabel.Text = "Status: Ready"
        self.view.Refresh()

if __name__=='__main__':
    print "Controller"