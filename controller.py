import clr
clr.AddReference('System.Windows.Forms') 
clr.AddReference('System.Drawing')
#clr.AddReference('System.ComponentModel')

from utils import launch_default_browser

import System
from System.Windows.Forms import *
from System.IO import File, Path
from model import ICM

from decimal import Decimal as D

class SimpleICMController:
    def __init__(self, view):
        self.view = view
        self._model = None
        self._cachedText = {}
        
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
    
    def cache_value(self, sender, event):
        print "Caching %s" % sender.Text
        self._cachedText[sender.Name] = sender.Text   
    def validate_number(self, sender, event):
        print "LostFocus %s %s" % (sender, event)
        try:
            D(sender.Text)
        except:
            MessageBox.Show("Please enter a number!", "Input validation error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            sender.Text = self._cachedText[sender.Name]
            sender.Focus()
            
    def handle_navigate(self, sender, event):
        event.Cancel = True
        print "Navigating %s %s %s" % (event.Url, sender, event)
        launch_default_browser(event.Url)
        #System.Diagnostics.Process.Start(event.Url)
        
        
if __name__=='__main__':
    print "Controller"