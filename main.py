import clr
import System
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import Bitmap, Color, Size
from System.IO import Directory, Path, StreamWriter
from System.Windows.Forms import (
    Application, DialogResult, DockStyle, Form,
    Keys, MenuStrip, MessageBox, MessageBoxButtons, 
    MessageBoxIcon,
    ScrollBars, SaveFileDialog, TabAlignment, 
    TabControl, TabPage, TextBox, 
    ToolStripItemDisplayStyle, ToolStrip,
    ToolStripButton, ToolStripGripStyle,
    ToolStripMenuItem
)
#

from controller import SimpleICMController
from view import SimpleICMForm


import sys
from System.IO import Directory, Path

form = SimpleICMForm()
Application.EnableVisualStyles()
Application.Run(form)
