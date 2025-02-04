[Setup]
AppName=Chatbot AI
AppVersion=1.0
DefaultDirName={pf}\Chatbot AI
DefaultGroupName=Chatbot AI
OutputDir=output
OutputBaseFilename=ChatbotAIInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Chatbot AI"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,Chatbot AI}"; Flags: nowait postinstall skipifsilent
