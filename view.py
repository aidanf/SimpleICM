import clr
clr.AddReference('System.Windows.Forms') 
clr.AddReference('System.Drawing')
#clr.AddReference('System.ComponentModel')


import System
from System.Windows.Forms import *
from System.ComponentModel import *
from System.Drawing import *
from System.IO import File, Path
from clr import *

from controller import SimpleICMController

class SimpleICMForm(System.Windows.Forms.Form):

    #__slots__ = ['_tab_control', '_tabs[0]', '_tabs[1]', 'equities[8]', 'equities[7]', 'equities[6]', 'equities[5]', 'equities[4]', 'equities[3]', 'equities[2]', 'equities[1]', '_label_stack_header', '_label_eq_header', '_label_player_header', 'equities[0]', 'go_button', 'stacks[8]', '_player_labels[8]', 'stacks[7]', '_player_labels[7]', 'stacks[6]', '_player_labels[6]', 'stacks[5]', '_player_labels[5]', 'stacks[4]', '_player_labels[4]', 'stacks[3]', '_player_labels[3]', 'stacks[2]', '_player_labels[2]', 'stacks[1]', '_player_labels[1]', 'stacks[0]', '_player_labels[0]', '_richTextBox1', '_payouts[4]', '_payouts[3]', '_payouts[2]', '_payouts[1]', '_payouts[0]', '_payout_labels[4]', '_payout_labels[3]', '_payout_labels[2]', '_payout_labels[1]', '_payout_labels[0]', '_tabs[2]']
    def __init__(self):
        self.executablePath = __file__
        if self.executablePath is None:
            self.executablePath = Application.ExecutablePath
        self.executableDirectory = Path.GetDirectoryName(self.executablePath)
        self.InitializeComponent()
        self.controller = SimpleICMController(self)
        self.go_button.Click += self.controller.handle_go
        
    @accepts(Self(), bool)
    @returns(None)
    def Dispose(self, disposing):
        super(type(self), self).Dispose(disposing)
    
    @returns(None)
    def InitializeComponent(self):
        self.MaximumSize = self.MinimumSize = System.Drawing.Size(300, 480)
        self._tab_control = System.Windows.Forms.TabControl()
        self.statusStrip = System.Windows.Forms.StatusStrip()
        self.statusLabel = System.Windows.Forms.ToolStripStatusLabel()
        
        self._tabs = []
        self.iconPath = 'icons\\simple_icm.ico'
        self.Icon = Icon(Path.Combine(self.executableDirectory, self.iconPath))
        
        for i in range(3):
            self._tabs.append(System.Windows.Forms.TabPage())        
        self.go_button = System.Windows.Forms.Button()
        
        self.stacks = []
        self.equities = []
        self._player_labels = []
        for i in range(9):
            self.stacks.append(System.Windows.Forms.TextBox())
            self.equities.append(System.Windows.Forms.Label())
            self._player_labels.append(System.Windows.Forms.Label())
        self._label_eq_header = System.Windows.Forms.Label()
        self._label_player_header = System.Windows.Forms.Label()
        self._label_stack_header = System.Windows.Forms.Label()
        self._richTextBox1 = System.Windows.Forms.RichTextBox()

        self._payout_labels = []
        self.payouts = []
        for i in range(5):
            self._payout_labels.append(System.Windows.Forms.Label())
            self.payouts.append(System.Windows.Forms.TextBox())

        self._tab_control.SuspendLayout()
        self._tabs[0].SuspendLayout()
        self._tabs[1].SuspendLayout()
        self._tabs[2].SuspendLayout()
        self.statusStrip.SuspendLayout()
        self.SuspendLayout()
        # 
        # tab3
        # 
        for tab in self._tabs:
            self._tab_control.Controls.Add(tab)
        #self._tab_control.Location = System.Drawing.Point(13, 13)
        self._tab_control.Name = 'tab3'
        self._tab_control.SelectedIndex = 0
        #self._tab_control.Size = System.Drawing.Size(287, 447)
        self._tab_control.TabIndex = 0
        self._tab_control.Dock = System.Windows.Forms.DockStyle.Fill
        self._tab_control.Location = System.Drawing.Point(0, 0)
        
        # 
        # tab1
        # 
        for i in range(9):
            self._tabs[0].Controls.Add(self.equities[i])
            self._tabs[0].Controls.Add(self.stacks[i])
            self._tabs[0].Controls.Add(self._player_labels[i])
        self._tabs[0].Controls.Add(self._label_stack_header)
        self._tabs[0].Controls.Add(self._label_eq_header)
        self._tabs[0].Controls.Add(self._label_player_header)
        self._tabs[0].Controls.Add(self.go_button)
        self._tabs[0].Controls.Add(self.statusStrip)
        self._tabs[0].Location = System.Drawing.Point(4, 27)
        self._tabs[0].Name = 'tab1'
        self._tabs[0].Padding = System.Windows.Forms.Padding(3)
        self._tabs[0].Size = System.Drawing.Size(279, 416)
        self._tabs[0].TabIndex = 0
        self._tabs[0].Text = 'Stacks'
        self._tabs[0].UseVisualStyleBackColor = True
        # 
        # tab2
        # 
        for i in range(5):
            self._tabs[1].Controls.Add(self.payouts[i])
            self._tabs[1].Controls.Add(self._payout_labels[i])
        self._tabs[1].Location = System.Drawing.Point(4, 27)
        self._tabs[1].Name = 'tab2'
        self._tabs[1].Padding = System.Windows.Forms.Padding(3)
        self._tabs[1].Size = System.Drawing.Size(279, 416)
        self._tabs[1].TabIndex = 1
        self._tabs[1].Text = 'Payouts'
        self._tabs[1].UseVisualStyleBackColor = True
        # 
        # tabPage3
        # 
        self._tabs[2].Controls.Add(self._richTextBox1)
        self._tabs[2].Location = System.Drawing.Point(4, 27)
        self._tabs[2].Name = 'tabPage3'
        self._tabs[2].Padding = System.Windows.Forms.Padding(3)
        self._tabs[2].Size = System.Drawing.Size(279, 416)
        self._tabs[2].TabIndex = 2
        self._tabs[2].Text = 'About'
        self._tabs[2].UseVisualStyleBackColor = True
        # 
        # button_go
        # 
        self.go_button.Location = System.Drawing.Point(9, 350)
        self.go_button.Name = 'button_go'
        self.go_button.Size = System.Drawing.Size(263, 35)
        self.go_button.TabIndex = 55
        self.go_button.Text = 'Go'
        self.go_button.UseVisualStyleBackColor = True
        
        self.statusStrip.Items.AddRange(            System.Array[System.Windows.Forms.ToolStripItem]((self.statusLabel, )))
        self.statusStrip.Location = System.Drawing.Point(3, 515)
        self.statusStrip.Name = 'statusStrip'
        self.statusStrip.Size = System.Drawing.Size(178, 22)
        self.statusStrip.TabIndex = 56
        self.statusStrip.Text = 'Waiting'
        self.statusStrip.Dock = System.Windows.Forms.DockStyle.Bottom
        
        self.statusLabel.Name = 'statusLabel'
        self.statusLabel.Size = System.Drawing.Size(109, 17)
        self.statusLabel.Text = 'Status: Ready'
        #self.statusLabel.Click += self.statusLabel1_Click
        
        #def click(sender, event):
        #    print "Clicked"
        # 
        # stack9
        #
        def initialize_stack(i, location, size, tabindex):
            self.stacks[i].Location = location
            self.stacks[i].Name = "stack%s" % (i+1)
            self.stacks[i].Size = size
            self.stacks[i].TabIndex = tabindex
            self.stacks[i].Text = '1500'
        initialize_stack(8, System.Drawing.Point(93, 309), 
                        System.Drawing.Size(111, 27), 54)
        initialize_stack(7 , System.Drawing.Point(93, 276),
                        System.Drawing.Size(111, 27), 52)
        initialize_stack(6, System.Drawing.Point(93, 243),
                        System.Drawing.Size(111, 27), 50)
        initialize_stack(5, System.Drawing.Point(93, 210),
                        System.Drawing.Size(111, 27), 48)
        initialize_stack(4, System.Drawing.Point(93, 177),
                        System.Drawing.Size(111, 27), 46)
        initialize_stack(3, System.Drawing.Point(93, 144),
                        System.Drawing.Size(111, 27), 44)
        initialize_stack(2, System.Drawing.Point(93, 111),
                        System.Drawing.Size(111, 27), 42)                              
        initialize_stack(1, System.Drawing.Point(93, 78),
                        System.Drawing.Size(111, 27), 40)
        initialize_stack(0, System.Drawing.Point(93, 45),
                        System.Drawing.Size(111, 27), 38)

        def initialize_player_label(i, location, size, tabindex):
            self._player_labels[i].AutoSize = True
            self._player_labels[i].Location = location
            self._player_labels[i].Name = "label_p%s" % (i+1)
            self._player_labels[i].Size = size
            self._player_labels[i].TabIndex = tabindex
            self._player_labels[i].Text = "Player %s" % (i+1)
        initialize_player_label(8, System.Drawing.Point(6, 312),
                                System.Drawing.Size(74, 18), 53)
        initialize_player_label(7, System.Drawing.Point(6, 279), 
                                System.Drawing.Size(74, 18), 51)
        initialize_player_label(6, System.Drawing.Point(6, 246),
                                System.Drawing.Size(74, 18), 49)
        initialize_player_label(5, System.Drawing.Point(6, 213),
                                System.Drawing.Size(74, 18), 47)
        initialize_player_label(4, System.Drawing.Point(6, 180),
                                System.Drawing.Size(74, 18), 45)
        initialize_player_label(3, System.Drawing.Point(6, 147),
                                System.Drawing.Size(74, 18), 43)
        initialize_player_label(2, System.Drawing.Point(6, 114),
                                System.Drawing.Size(74, 18), 41)
        initialize_player_label(1,  System.Drawing.Point(6, 81),
                                System.Drawing.Size(74, 18), 39)
        initialize_player_label(0, System.Drawing.Point(6, 48), 
                                System.Drawing.Size(74, 18), 37)
        # 
        # eq1
        # 
        # 
        # label_eq_header
        # 
        self._label_eq_header.AutoSize = True
        self._label_eq_header.Font = System.Drawing.Font('Verdana', 12.0, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label_eq_header.Location = System.Drawing.Point(210, 9)
        self._label_eq_header.Name = 'label_eq_header'
        self._label_eq_header.Size = System.Drawing.Size(62, 18)
        self._label_eq_header.TabIndex = 59
        self._label_eq_header.Text = 'Equity'
        # 
        # label_player_header
        # 
        self._label_player_header.AutoSize = True
        self._label_player_header.Font = System.Drawing.Font('Verdana', 12.0, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label_player_header.Location = System.Drawing.Point(6, 9)
        self._label_player_header.Name = 'label_player_header'
        self._label_player_header.Size = System.Drawing.Size(63, 18)
        self._label_player_header.TabIndex = 57
        self._label_player_header.Text = 'Player'
        # 
        # label_stack_header
        # 
        self._label_stack_header.AutoSize = True
        self._label_stack_header.Font = System.Drawing.Font('Verdana', 12.0, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._label_stack_header.Location = System.Drawing.Point(90, 9)
        self._label_stack_header.Name = 'label_stack_header'
        self._label_stack_header.Size = System.Drawing.Size(56, 18)
        self._label_stack_header.TabIndex = 60
        self._label_stack_header.Text = 'Stack'


        def initialize_equity(i, location, size, tabindex):
            self.equities[i].AutoSize = True
            self.equities[i].Location = location
            self.equities[i].Name = "eq%i" % (i+1)
            self.equities[i].Size = size
            self.equities[i].TabIndex = tabindex
            self.equities[i].Text = "eq%i" % (i+1)
            
        initialize_equity(0, System.Drawing.Point(210, 48),
                        System.Drawing.Size(38, 18), 56)
        initialize_equity(1, System.Drawing.Point(210, 81),
                        System.Drawing.Size(38, 18), 61)
        initialize_equity(2, System.Drawing.Point(210, 114),
                        System.Drawing.Size(38, 18), 62)
        initialize_equity(3, System.Drawing.Point(210, 147),
                        System.Drawing.Size(38, 18), 63)
        initialize_equity(4, System.Drawing.Point(210, 180), 
                        System.Drawing.Size(38, 18), 64)
        initialize_equity(5, System.Drawing.Point(210, 213), 
                        System.Drawing.Size(38, 18), 65)
        initialize_equity(6, System.Drawing.Point(210, 246),
                        System.Drawing.Size(38, 18), 66)
        initialize_equity(7, System.Drawing.Point(210, 279), 
                        System.Drawing.Size(38, 18), 67)
        initialize_equity(8, System.Drawing.Point(210, 312), 
                        System.Drawing.Size(38, 18), 68)
        # 
        # richTextBox1
        # 
        self._richTextBox1.Location = System.Drawing.Point(7, 7)
        self._richTextBox1.Name = 'richTextBox1'
        self._richTextBox1.ReadOnly = True
        self._richTextBox1.Size = System.Drawing.Size(266, 403)
        self._richTextBox1.TabIndex = 0
        self._richTextBox1.Text = ''
        # 
        # labelpayouts[0]
        # 

        def initialize_payout_labels():
            texts = ['1st', '2nd', '3rd', '4th', '5th']
            locations = [(6, 24), (6, 59), (6, 94), (6, 131), (6, 164)]
            for i in range(5):
                self._payout_labels[i].AutoSize = True
                self._payout_labels[i].Location = System.Drawing.Point(locations[i][0], locations[i][1])
                self._payout_labels[i].Name = "label_payouts_%s" % (i+1)
                self._payout_labels[i].Size = System.Drawing.Size(34, 18)
                self._payout_labels[i].TabIndex = i
                self._payout_labels[i].Text = texts[i]
        initialize_payout_labels()
                
        def initialize_payouts():
            texts = ['0.5', '0.3', '0.2', '0.0', '0.0']
            locations = [(66, 21), (66, 56), (66, 91), (66, 128), (66, 161)]
            for i in range(5):
                self.payouts[i].Location = System.Drawing.Point(locations[i][0], locations[i][1])
                self.payouts[i].Name = "payout%s" % (i+1)
                self.payouts[i].Size = System.Drawing.Size(100, 27)
                self.payouts[i].TabIndex = 5 + i
                self.payouts[i].Text = texts[i]
        initialize_payouts()
        # 
        # SimpleICMView
        # 
        self.ClientSize = System.Drawing.Size(308, 467)
        self.Controls.Add(self._tab_control)
        self.Font = System.Drawing.Font('Verdana', 12.0, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = 'SimpleICMView'
        self.Text = 'SimpleICM'
        self._tab_control.ResumeLayout(False)
        self._tabs[0].ResumeLayout(False)
        self._tabs[0].PerformLayout()
        self.statusStrip.ResumeLayout(False)
        self.statusStrip.PerformLayout()
        self._tabs[1].ResumeLayout(False)
        self._tabs[1].PerformLayout()
        self._tabs[2].ResumeLayout(False)
        self.ResumeLayout(False)
    
    @accepts(Self(), System.Object, System.EventArgs)
    @returns(None)
    def _textBox6_TextChanged(self, sender, e):
        pass


if __name__ == '__main__':

    
    form = SimpleICMForm()
    print "XXX "+form.executableDirectory
    Application.EnableVisualStyles()
    Application.Run(form)

