import clr
clr.AddReference('System.Windows.Forms') 
clr.AddReference('System.Drawing')
#clr.AddReference('System.ComponentModel')


import System
from System.Windows.Forms import *
from System.ComponentModel import *
from System.Drawing import *
from clr import *

class SimpleICMForm(System.Windows.Forms.Form):

    #__slots__ = ['_tab_control', '_tabs[0]', '_tabs[1]', '_equities[8]', '_equities[7]', '_equities[6]', '_equities[5]', '_equities[4]', '_equities[3]', '_equities[2]', '_equities[1]', '_label_stack_header', '_label_eq_header', '_label_player_header', '_equities[0]', '_button_go', '_stacks[8]', '_player_labels[8]', '_stacks[7]', '_player_labels[7]', '_stacks[6]', '_player_labels[6]', '_stacks[5]', '_player_labels[5]', '_stacks[4]', '_player_labels[4]', '_stacks[3]', '_player_labels[3]', '_stacks[2]', '_player_labels[2]', '_stacks[1]', '_player_labels[1]', '_stacks[0]', '_player_labels[0]', '_richTextBox1', '_payouts[4]', '_payouts[3]', '_payouts[2]', '_payouts[1]', '_payouts[0]', '_payout_labels[4]', '_payout_labels[3]', '_payout_labels[2]', '_payout_labels[1]', '_payout_labels[0]', '_tabs[2]']
    def __init__(self):
        self.InitializeComponent()
    
    @accepts(Self(), bool)
    @returns(None)
    def Dispose(self, disposing):
        
        
        
        super(type(self), self).Dispose(disposing)
    
    @returns(None)
    def InitializeComponent(self):
        self.MaximumSize = self.MinimumSize = System.Drawing.Size(300, 480)
        self._tab_control = System.Windows.Forms.TabControl()
        self._tabs = []
        
        for i in range(3):
            self._tabs.append(System.Windows.Forms.TabPage())        
        self._button_go = System.Windows.Forms.Button()
        
        self._stacks = []
        self._equities = []
        self._player_labels = []
        for i in range(9):
            self._stacks.append(System.Windows.Forms.TextBox())
            self._equities.append(System.Windows.Forms.Label())
            self._player_labels.append(System.Windows.Forms.Label())
        self._label_eq_header = System.Windows.Forms.Label()
        self._label_player_header = System.Windows.Forms.Label()
        self._label_stack_header = System.Windows.Forms.Label()
        self._richTextBox1 = System.Windows.Forms.RichTextBox()

        self._payout_labels = []
        self._payouts = []
        for i in range(5):
            self._payout_labels.append(System.Windows.Forms.Label())
            self._payouts.append(System.Windows.Forms.TextBox())

        self._tab_control.SuspendLayout()
        self._tabs[0].SuspendLayout()
        self._tabs[1].SuspendLayout()
        self._tabs[2].SuspendLayout()
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
            self._tabs[0].Controls.Add(self._equities[i])
            self._tabs[0].Controls.Add(self._stacks[i])
            self._tabs[0].Controls.Add(self._player_labels[i])
        self._tabs[0].Controls.Add(self._label_stack_header)
        self._tabs[0].Controls.Add(self._label_eq_header)
        self._tabs[0].Controls.Add(self._label_player_header)
        self._tabs[0].Controls.Add(self._button_go)
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
            self._tabs[1].Controls.Add(self._payouts[i])
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
        self._button_go.Location = System.Drawing.Point(9, 372)
        self._button_go.Name = 'button_go'
        self._button_go.Size = System.Drawing.Size(263, 35)
        self._button_go.TabIndex = 55
        self._button_go.Text = 'Go'
        self._button_go.UseVisualStyleBackColor = True
        # 
        # stack9
        # 
        self._stacks[8].Location = System.Drawing.Point(93, 309)
        self._stacks[8].Name = 'stack9'
        self._stacks[8].Size = System.Drawing.Size(111, 27)
        self._stacks[8].TabIndex = 54
        self._stacks[8].Text = '1500'
        # 
        # label_p9
        # 
        self._player_labels[8].AutoSize = True
        self._player_labels[8].Location = System.Drawing.Point(6, 312)
        self._player_labels[8].Name = 'label_p9'
        self._player_labels[8].Size = System.Drawing.Size(74, 18)
        self._player_labels[8].TabIndex = 53
        self._player_labels[8].Text = 'Player 9'
        # 
        # stack8
        # 
        self._stacks[7].Location = System.Drawing.Point(93, 276)
        self._stacks[7].Name = 'stack8'
        self._stacks[7].Size = System.Drawing.Size(111, 27)
        self._stacks[7].TabIndex = 52
        self._stacks[7].Text = '1500'
        # 
        # label_p8
        # 
        self._player_labels[7].AutoSize = True
        self._player_labels[7].Location = System.Drawing.Point(6, 279)
        self._player_labels[7].Name = 'label_p8'
        self._player_labels[7].Size = System.Drawing.Size(74, 18)
        self._player_labels[7].TabIndex = 51
        self._player_labels[7].Text = 'Player 8'
        # 
        # stack7
        # 
        self._stacks[6].Location = System.Drawing.Point(93, 243)
        self._stacks[6].Name = 'stack7'
        self._stacks[6].Size = System.Drawing.Size(111, 27)
        self._stacks[6].TabIndex = 50
        self._stacks[6].Text = '1500'
        # 
        # label_p7
        # 
        self._player_labels[6].AutoSize = True
        self._player_labels[6].Location = System.Drawing.Point(6, 246)
        self._player_labels[6].Name = 'label_p7'
        self._player_labels[6].Size = System.Drawing.Size(74, 18)
        self._player_labels[6].TabIndex = 49
        self._player_labels[6].Text = 'Player 7'
        # 
        # stack6
        # 
        self._stacks[5].Location = System.Drawing.Point(93, 210)
        self._stacks[5].Name = 'stack6'
        self._stacks[5].Size = System.Drawing.Size(111, 27)
        self._stacks[5].TabIndex = 48
        self._stacks[5].Text = '1500'
        # 
        # label_p6
        # 
        self._player_labels[5].AutoSize = True
        self._player_labels[5].Location = System.Drawing.Point(6, 213)
        self._player_labels[5].Name = 'label_p6'
        self._player_labels[5].Size = System.Drawing.Size(74, 18)
        self._player_labels[5].TabIndex = 47
        self._player_labels[5].Text = 'Player 6'
        # 
        # stack5
        # 
        self._stacks[4].Location = System.Drawing.Point(93, 177)
        self._stacks[4].Name = 'stack5'
        self._stacks[4].Size = System.Drawing.Size(111, 27)
        self._stacks[4].TabIndex = 46
        self._stacks[4].Text = '1500'
        # 
        # label_p5
        # 
        self._player_labels[4].AutoSize = True
        self._player_labels[4].Location = System.Drawing.Point(6, 180)
        self._player_labels[4].Name = 'label_p5'
        self._player_labels[4].Size = System.Drawing.Size(74, 18)
        self._player_labels[4].TabIndex = 45
        self._player_labels[4].Text = 'Player 5'
        # 
        # stack4
        # 
        self._stacks[3].Location = System.Drawing.Point(93, 144)
        self._stacks[3].Name = 'stack4'
        self._stacks[3].Size = System.Drawing.Size(111, 27)
        self._stacks[3].TabIndex = 44
        self._stacks[3].Text = '1500'
        # 
        # label_p4
        # 
        self._player_labels[3].AutoSize = True
        self._player_labels[3].Location = System.Drawing.Point(6, 147)
        self._player_labels[3].Name = 'label_p4'
        self._player_labels[3].Size = System.Drawing.Size(74, 18)
        self._player_labels[3].TabIndex = 43
        self._player_labels[3].Text = 'Player 4'
        # 
        # stack3
        # 
        self._stacks[2].Location = System.Drawing.Point(93, 111)
        self._stacks[2].Name = 'stack3'
        self._stacks[2].Size = System.Drawing.Size(111, 27)
        self._stacks[2].TabIndex = 42
        self._stacks[2].Text = '1500'
        # 
        # label_p3
        # 
        self._player_labels[2].AutoSize = True
        self._player_labels[2].Location = System.Drawing.Point(6, 114)
        self._player_labels[2].Name = 'label_p3'
        self._player_labels[2].Size = System.Drawing.Size(74, 18)
        self._player_labels[2].TabIndex = 41
        self._player_labels[2].Text = 'Player 3'
        # 
        # stack2
        # 
        self._stacks[1].Location = System.Drawing.Point(93, 78)
        self._stacks[1].Name = 'stack2'
        self._stacks[1].Size = System.Drawing.Size(111, 27)
        self._stacks[1].TabIndex = 40
        self._stacks[1].Text = '1500'
        # 
        # label_p2
        # 
        self._player_labels[1].AutoSize = True
        self._player_labels[1].Location = System.Drawing.Point(6, 81)
        self._player_labels[1].Name = 'label_p2'
        self._player_labels[1].Size = System.Drawing.Size(74, 18)
        self._player_labels[1].TabIndex = 39
        self._player_labels[1].Text = 'Player 2'
        # 
        # stack1
        # 
        self._stacks[0].Location = System.Drawing.Point(93, 45)
        self._stacks[0].Name = 'stack1'
        self._stacks[0].Size = System.Drawing.Size(111, 27)
        self._stacks[0].TabIndex = 38
        self._stacks[0].Text = '1500'
        # 
        # label_p1
        # 
        self._player_labels[0].AutoSize = True
        self._player_labels[0].Location = System.Drawing.Point(6, 48)
        self._player_labels[0].Name = 'label_p1'
        self._player_labels[0].Size = System.Drawing.Size(74, 18)
        self._player_labels[0].TabIndex = 37
        self._player_labels[0].Text = 'Player 1'
        # 
        # eq1
        # 
        self._equities[0].AutoSize = True
        self._equities[0].Location = System.Drawing.Point(210, 48)
        self._equities[0].Name = 'eq1'
        self._equities[0].Size = System.Drawing.Size(38, 18)
        self._equities[0].TabIndex = 56
        self._equities[0].Text = 'eq1'
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
        # 
        # eq2
        # 
        self._equities[1].AutoSize = True
        self._equities[1].Location = System.Drawing.Point(210, 81)
        self._equities[1].Name = 'eq2'
        self._equities[1].Size = System.Drawing.Size(38, 18)
        self._equities[1].TabIndex = 61
        self._equities[1].Text = 'eq2'
        # 
        # eq3
        # 
        self._equities[2].AutoSize = True
        self._equities[2].Location = System.Drawing.Point(210, 114)
        self._equities[2].Name = 'eq3'
        self._equities[2].Size = System.Drawing.Size(38, 18)
        self._equities[2].TabIndex = 62
        self._equities[2].Text = 'eq3'
        # 
        # eq4
        # 
        self._equities[3].AutoSize = True
        self._equities[3].Location = System.Drawing.Point(210, 147)
        self._equities[3].Name = 'eq4'
        self._equities[3].Size = System.Drawing.Size(38, 18)
        self._equities[3].TabIndex = 63
        self._equities[3].Text = 'eq4'
        # 
        # eq5
        # 
        self._equities[4].AutoSize = True
        self._equities[4].Location = System.Drawing.Point(210, 180)
        self._equities[4].Name = 'eq5'
        self._equities[4].Size = System.Drawing.Size(38, 18)
        self._equities[4].TabIndex = 64
        self._equities[4].Text = 'eq5'
        # 
        # eq6
        # 
        self._equities[5].AutoSize = True
        self._equities[5].Location = System.Drawing.Point(210, 213)
        self._equities[5].Name = 'eq6'
        self._equities[5].Size = System.Drawing.Size(38, 18)
        self._equities[5].TabIndex = 65
        self._equities[5].Text = 'eq6'
        # 
        # eq7
        # 
        self._equities[6].AutoSize = True
        self._equities[6].Location = System.Drawing.Point(210, 246)
        self._equities[6].Name = 'eq7'
        self._equities[6].Size = System.Drawing.Size(38, 18)
        self._equities[6].TabIndex = 66
        self._equities[6].Text = 'eq7'
        # 
        # eq8
        # 
        self._equities[7].AutoSize = True
        self._equities[7].Location = System.Drawing.Point(210, 279)
        self._equities[7].Name = 'eq8'
        self._equities[7].Size = System.Drawing.Size(38, 18)
        self._equities[7].TabIndex = 67
        self._equities[7].Text = 'eq8'
        # 
        # eq9
        # 
        self._equities[8].AutoSize = True
        self._equities[8].Location = System.Drawing.Point(210, 312)
        self._equities[8].Name = 'eq9'
        self._equities[8].Size = System.Drawing.Size(38, 18)
        self._equities[8].TabIndex = 68
        self._equities[8].Text = 'eq9'
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
        # label_payouts[0]
        # 
        self._payout_labels[0].AutoSize = True
        self._payout_labels[0].Location = System.Drawing.Point(6, 24)
        self._payout_labels[0].Name = 'label_payouts[0]'
        self._payout_labels[0].Size = System.Drawing.Size(34, 18)
        self._payout_labels[0].TabIndex = 0
        self._payout_labels[0].Text = '1st'
        # 
        # label_payouts[1]
        # 
        self._payout_labels[1].AutoSize = True
        self._payout_labels[1].Location = System.Drawing.Point(6, 59)
        self._payout_labels[1].Name = 'label_payouts[1]'
        self._payout_labels[1].Size = System.Drawing.Size(38, 18)
        self._payout_labels[1].TabIndex = 1
        self._payout_labels[1].Text = '2nd'
        # 
        # label_payouts[2]
        # 
        self._payout_labels[2].AutoSize = True
        self._payout_labels[2].Location = System.Drawing.Point(6, 94)
        self._payout_labels[2].Name = 'label_payouts[2]'
        self._payout_labels[2].Size = System.Drawing.Size(34, 18)
        self._payout_labels[2].TabIndex = 2
        self._payout_labels[2].Text = '3rd'
        # 
        # label_payouts[3]
        # 
        self._payout_labels[3].AutoSize = True
        self._payout_labels[3].Location = System.Drawing.Point(6, 131)
        self._payout_labels[3].Name = 'label_payouts[3]'
        self._payout_labels[3].Size = System.Drawing.Size(35, 18)
        self._payout_labels[3].TabIndex = 3
        self._payout_labels[3].Text = '4th'
        # 
        # label_payouts[4]
        # 
        self._payout_labels[4].AutoSize = True
        self._payout_labels[4].Location = System.Drawing.Point(6, 164)
        self._payout_labels[4].Name = 'label_payouts[4]'
        self._payout_labels[4].Size = System.Drawing.Size(35, 18)
        self._payout_labels[4].TabIndex = 4
        self._payout_labels[4].Text = '5th'
        # 
        # payout1
        # 
        self._payouts[0].Location = System.Drawing.Point(66, 21)
        self._payouts[0].Name = 'payout1'
        self._payouts[0].Size = System.Drawing.Size(100, 27)
        self._payouts[0].TabIndex = 5
        self._payouts[0].Text = '0.5'
        # 
        # payout2
        # 
        self._payouts[1].Location = System.Drawing.Point(66, 56)
        self._payouts[1].Name = 'payout2'
        self._payouts[1].Size = System.Drawing.Size(100, 27)
        self._payouts[1].TabIndex = 6
        self._payouts[1].Text = '0.3'
        # 
        # payout3
        # 
        self._payouts[2].Location = System.Drawing.Point(66, 91)
        self._payouts[2].Name = 'payout3'
        self._payouts[2].Size = System.Drawing.Size(100, 27)
        self._payouts[2].TabIndex = 7
        self._payouts[2].Text = '0.2'
        # 
        # textBox4
        # 
        self._payouts[3].Location = System.Drawing.Point(66, 128)
        self._payouts[3].Name = 'textBox4'
        self._payouts[3].Size = System.Drawing.Size(100, 27)
        self._payouts[3].TabIndex = 8
        self._payouts[3].Text = '0.0'
        # 
        # payout5
        # 
        self._payouts[4].Location = System.Drawing.Point(66, 161)
        self._payouts[4].Name = 'payout5'
        self._payouts[4].Size = System.Drawing.Size(100, 27)
        self._payouts[4].TabIndex = 9
        self._payouts[4].Text = '0.0'
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
        self._tabs[1].ResumeLayout(False)
        self._tabs[1].PerformLayout()
        self._tabs[2].ResumeLayout(False)
        self.ResumeLayout(False)
    
    @accepts(Self(), System.Object, System.EventArgs)
    @returns(None)
    def _textBox6_TextChanged(self, sender, e):
        pass
    
form = SimpleICMForm()
Application.EnableVisualStyles()
Application.Run(form)

