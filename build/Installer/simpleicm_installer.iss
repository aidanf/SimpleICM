; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{7169FAE3-6E88-4F9B-83F6-13A8ED4C5C7D}
AppName=SimpleICM
AppVerName=SimpleICM version 0.1
AppPublisher=PokerKernel
AppPublisherURL=http://pokerkernel.com
AppSupportURL=http://pokerkernel.com
AppUpdatesURL=http://pokerkernel.com
DefaultDirName={pf}\SimpleICM
DefaultGroupName=SimpleICM
LicenseFile=Z:\Code\WindowsApps\SimpleICM\build\simpleicm\LICENCE.txt
OutputDir=Z:\Code\WindowsApps\SimpleICM\build\Installer
OutputBaseFilename=simpleicm_setup
SetupIconFile=Z:\Code\WindowsApps\SimpleICM\build\simpleicm\icons\simple_icm.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "Z:\Code\WindowsApps\SimpleICM\build\simpleicm\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "Z:\Code\WindowsApps\SimpleICM\build\simpleicm\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\SimpleICM"; Filename: "{app}\main.exe"; IconFilename: "{app}\icons\simple_icm.ico"
Name: "{group}\{cm:ProgramOnTheWeb,SimpleICM}"; Filename: "http://pokerkernel.com"
Name: "{group}\{cm:UninstallProgram,SimpleICM}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\SimpleICM"; Filename: "{app}\main.exe"; IconFilename: "{app}\icons\simple_icm.ico";Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,SimpleICM}"; Flags: nowait postinstall skipifsilent

