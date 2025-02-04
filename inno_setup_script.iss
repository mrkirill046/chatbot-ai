[Setup]
AppName=ChatBot Application
AppVersion=1.0
DefaultDirName={pf}\ChatBot
OutputDir=output
OutputBaseFilename=chatbot_installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "output\*"; DestDir: "{app}"; Flags: ignoreversion
Source: "requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "main.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "src\**\*"; DestDir: "{app}\src"; Flags: ignoreversion

[Icons]
Name: "{group}\ChatBot"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,ChatBot}"; Flags: nowait postinstall skipifsilent
