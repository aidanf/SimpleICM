import clr
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



import sys
from System.IO import Directory, Path

if __name__ == '__main__':
    executablePath = __file__
    if executablePath is None:
        executablePath = Application.ExecutablePath
    executableDirectory = Path.GetDirectoryName(executablePath)

    import clr
    sys.path.append(Path.Combine(executableDirectory, "lib"))
    print "XXX "+executablePath
    print executableDirectory
    print sys.path
    clr.AddReference('SimpleICMInterface')
    
from SimpleICMInterface import SimpleICMInterface

